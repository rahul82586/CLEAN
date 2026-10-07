"""Phase 1b — a master process that starts everything, config-driven.

THE MODEL, FROM MT5
-------------------
`IMTConPlugin` has a `Server` field: *"A server on which the plugin is running"*, and
`Plugins.md` says the platform manages *"configurations of plugins in the platform and process
events of configuration changes"*. So MT5's trade server does exactly this: it reads a
configuration, and starts a process per configured plugin. It does not hard-code them.

This module is that master, in Python. It is deliberately SMALL and deliberately knows
nothing about any plugin:

    plugins.yaml
      plugins:
        - name: lp_mt5
          type: gateway          # gateway | feed | report
          module: plugins.gateway.lp_mt5
          port: 9101
          params: {ws_url: "...", login: "50080"}

    master.py
      reads the file, spawns `python -m <module> --port N --config '<json>'`, restarts a
      plugin that dies, and stops everything on shutdown.

Adding a gateway or a feed is then a new file plus one YAML entry. The master never changes.

WHAT THIS DELIBERATELY DOES NOT DO YET
--------------------------------------
* It does NOT yet move the existing MT5 LP server (port 8000) behind a plugin. That box is
  currently a single process doing feed AND gateway together, and it is working. Migrating it
  is Phase 2; this file proves the mechanism works first, with a no-op-safe dry run.
* It does NOT choose ports. Each plugin names its own.

SAFETY
------
`--dry-run` prints the plan and starts nothing. That is the default behaviour worth using
until the plugin contract exists.

Writes: master.py, plugins.yaml
"""
from __future__ import annotations

import json
import pathlib
import signal
import subprocess
import sys
import time

try:
    import yaml
except ImportError:  # pragma: no cover - depends on how the interpreter was launched
    # The master is spawned by an operator, not by the app, so it must not depend on the
    # app's venv being on sys.path. PyYAML ships with the interpreter here, but PYTHONPATH
    # is not always inherited - and a master that dies on a missing import cannot start the
    # thing that would have fixed it.
    sys.stderr.write(
        "[master] PyYAML is not importable. Run this with the same interpreter as the\n"
        "          server, or set PYTHONPATH. (python -m pip install pyyaml)\n"
    )
    raise SystemExit(3)

ROOT = pathlib.Path(__file__).resolve().parent
CONFIG = ROOT / "plugins.yaml"
LOG_DIR = ROOT / "logs" / "plugins"

VALID_TYPES = {"gateway", "feed", "report", "core"}


def load_config(path: pathlib.Path = CONFIG) -> list[dict]:
    """Read the plugin list. A missing or malformed file is reported, never a bare crash.

    The file is documentation as much as configuration, so it carries a long comment block.
    That makes two failure shapes likely: an empty file (no `plugins:` key at all) and a
    document whose top level is a list rather than a mapping. Both are handled here rather
    than as an AttributeError from deep inside `main`.
    """
    if not path.exists():
        print(f"[master] {path} does not exist; nothing to start")
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:                                # noqa: BLE001
        print(f"[master] {path.name} is not valid YAML: {exc}")
        return []
    if data is None:
        return []
    if isinstance(data, list):
        # Tolerated: a bare YAML list is read as the plugin list.
        return [x for x in data if isinstance(x, dict)]
    if not isinstance(data, dict):
        print(f"[master] {path.name} must be a mapping with a `plugins:` list, "
              f"got {type(data).__name__}")
        return []
    plugins = data.get("plugins") or []
    if not isinstance(plugins, list):
        print(f"[master] `plugins:` must be a list, got {type(plugins).__name__}")
        return []
    return [p for p in plugins if isinstance(p, dict)]


def validate(plugins: list[dict]) -> list[tuple[dict, str]]:
    """Return the problems, so a typo is reported before anything is spawned."""
    problems = []
    seen_names, seen_ports = set(), set()
    for p in plugins:
        name = p.get("name")
        where = f"plugin {name!r}"
        if not name:
            problems.append((p, "no `name`"))
            continue
        if name in seen_names:
            problems.append((p, f"duplicate name {name!r}"))
        seen_names.add(name)
        if p.get("type") not in VALID_TYPES:
            problems.append((p, f"{where}: type must be one of {sorted(VALID_TYPES)}"))
        if not p.get("module"):
            problems.append((p, f"{where}: no `module` to run"))
        port = p.get("port")
        if port is None:
            problems.append((p, f"{where}: no `port`"))
        else:
            if port in seen_ports:
                problems.append((p, f"{where}: port {port} already used by another plugin"))
            seen_ports.add(port)
    return problems


def command_for(p: dict) -> list[str]:
    """`python -m <module> --port N --config '<json>'`.

    `-m` rather than a script path, so the plugin is a normal importable package and shares
    the repo's virtualenv - which is what makes a third party able to add one.
    """
    cfg = {
        "name": p.get("name"),
        "type": p.get("type"),
        "port": p.get("port"),
        "params": p.get("params") or {},
    }
    return [
        sys.executable, "-u", "-m", str(p["module"]),
        "--port", str(p["port"]),
        "--config", json.dumps(cfg),
    ]


class Master:
    """Spawn, watch, restart, stop. Knows nothing about what a plugin does."""

    def __init__(self, plugins: list[dict], dry_run: bool = False):
        self.plugins = plugins
        self.dry_run = dry_run
        self.procs: dict[str, subprocess.Popen] = {}
        self._stopping = False

    def start_all(self) -> None:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        for p in self.plugins:
            self._spawn(p)

    def _spawn(self, p: dict) -> None:
        name = p.get("name") or "<unnamed>"
        cmd = command_for(p)
        if self.dry_run:
            print(f"[dry-run] would start {name:16} type={p.get('type'):8} "
                  f"port={p.get('port')}\n           {' '.join(cmd)}")
            return
        log_path = LOG_DIR / f"{name}.log"
        log = open(log_path, "a", encoding="utf-8", buffering=1)
        log.write(f"\n=== started {time.strftime('%Y-%m-%dT%H:%M:%S')} ===\n")
        log.flush()
        proc = subprocess.Popen(cmd, cwd=str(ROOT), stdout=log, stderr=subprocess.STDOUT)
        self.procs[name] = proc
        print(f"[master] started {name:16} pid={proc.pid} port={p.get('port')} -> {log_path}")

    def supervise(self, poll: float = 2.0) -> None:
        """Restart anything that dies. A crashed plugin must not take the broker down."""
        while not self._stopping:
            for name, proc in list(self.procs.items()):
                rc = proc.poll()
                if rc is None:
                    continue
                if self._stopping:
                    return
                p = next((x for x in self.plugins if x.get("name") == name), None)
                print(f"[master] {name} exited rc={rc}; restarting in 5s")
                time.sleep(5)
                if p:
                    self._spawn(p)
            time.sleep(poll)

    def stop_all(self) -> None:
        self._stopping = True
        for name, proc in self.procs.items():
            if proc.poll() is None:
                print(f"[master] stopping {name} (pid={proc.pid})")
                try:
                    proc.terminate()
                except Exception as exc:
                    print(f"[master] terminate {name} failed: {exc}")
        deadline = time.time() + 10
        for name, proc in self.procs.items():
            remaining = max(0.0, deadline - time.time())
            try:
                proc.wait(timeout=remaining)
            except Exception:
                proc.kill()
        print("[master] all plugins stopped")


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv
    plugins = load_config()
    print(f"[master] config: {CONFIG}")
    print(f"[master] {len(plugins)} plugin(s) declared{'  (DRY RUN - nothing started)' if dry_run else ''}")

    problems = validate(plugins)
    if problems:
        print("[master] CONFIG ERRORS:")
        for p, why in problems:
            print(f"   - {why}")
        return 1

    for p in plugins:
        print(f"   {p.get('name'):16} type={p.get('type'):8} port={p.get('port')} "
              f"module={p.get('module')}")

    m = Master(plugins, dry_run=dry_run)
    if dry_run:
        return 0

    def _sig(_signum, _frame):
        m.stop_all()
        sys.exit(0)

    signal.signal(signal.SIGINT, _sig)
    signal.signal(signal.SIGTERM, _sig)

    m.start_all()
    try:
        m.supervise()
    except KeyboardInterrupt:
        pass
    finally:
        m.stop_all()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))