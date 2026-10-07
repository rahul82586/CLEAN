# Basic usage (auto-named output)
# python project_to_md.py "D:\glm crawl\project-folder-for-claw\CLEAN\Forex-Backend-CLEAN"


# Custom output path
# python project_to_md.py "C:\Users\DELL\Downloads\backend_code-main (1)\backend_code-main\broker-platform" -o "C:\Users\DELL\Desktop\my_project.md"

#!/usr/bin/env python3
"""
Project to Markdown Converter
Generates a structured .md file with:
- Title & metadata
- Table of Contents with clickable links
- Directory tree view
- All files in fenced code blocks with language tags
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime


class ProjectToMarkdown:
    def __init__(self, project_path, output_path=None):
        self.project_path = Path(project_path).resolve()
        self.project_name = self.project_path.name or "Project"
        
        if output_path is None:
            self.output_path = self.project_path.parent / f"{self.project_name}.md"
        else:
            self.output_path = Path(output_path)
        
        self.exclude = {
            '__pycache__', '.git', '.venv', 'venv', 'node_modules',
            '.pytest_cache', '.mypy_cache', '.idea', '.vscode', '.DS_Store',
            'Thumbs.db', '*.pyc', '*.pyo', '*.class', '*.o', '*.obj',
            '.egg-info', 'dist', 'build', '.tox', '.coverage', 'htmlcov'
        }
        
        self.collected_files = []
        
        # Map extensions to markdown code fence languages
        self.lang_map = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
            '.jsx': 'jsx', '.tsx': 'tsx', '.java': 'java', '.c': 'c',
            '.cpp': 'cpp', '.h': 'cpp', '.cs': 'csharp', '.go': 'go',
            '.rs': 'rust', '.rb': 'ruby', '.php': 'php', '.swift': 'swift',
            '.kt': 'kotlin', '.scala': 'scala', '.r': 'r', '.m': 'matlab',
            '.sh': 'bash', '.bash': 'bash', '.zsh': 'zsh', '.ps1': 'powershell',
            '.bat': 'batch', '.cmd': 'batch', '.sql': 'sql', '.yaml': 'yaml',
            '.yml': 'yaml', '.json': 'json', '.xml': 'xml', '.html': 'html',
            '.htm': 'html', '.css': 'css', '.scss': 'scss', '.sass': 'sass',
            '.less': 'less', '.md': 'markdown', '.rst': 'rst', '.tex': 'latex',
            '.dockerfile': 'dockerfile', '.makefile': 'makefile', '.mk': 'makefile',
            '.cmake': 'cmake', '.gradle': 'groovy', '.pl': 'perl', '.lua': 'lua',
            '.vim': 'vim', '.el': 'emacs-lisp', '.clj': 'clojure', '.hs': 'haskell',
            '.erl': 'erlang', '.ex': 'elixir', '.fs': 'fsharp', '.pas': 'pascal',
            '.dart': 'dart', '.ini': 'ini', '.toml': 'toml', '.cfg': 'ini',
            '.conf': 'nginx', '.properties': 'properties', '.env': 'bash',
            '.gitignore': 'gitignore', '.gitattributes': 'gitattributes',
            '.pipfile': 'toml', '.lock': 'json', '.ipynb': 'json'
        }

    def should_exclude(self, path):
        name = path.name
        if name in self.exclude:
            return True
        if any(name.endswith(ext.lstrip('*')) for ext in self.exclude if ext.startswith('*')):
            return True
        # Skip hidden files/folders optionally (uncomment next line if desired)
        # if name.startswith('.') and name not in {'.gitignore', '.env', '.dockerignore'}:
        #     return True
        return False

    def collect_files(self):
        print(f"Scanning: {self.project_path}")
        for root, dirs, files in os.walk(self.project_path):
            root_path = Path(root)
            dirs[:] = [d for d in dirs if not self.should_exclude(root_path / d)]
            
            for file in sorted(files):
                file_path = root_path / file
                if self.should_exclude(file_path):
                    continue
                
                try:
                    # Skip known binary extensions
                    if file_path.suffix.lower() in {'.exe', '.dll', '.so', '.dylib', '.bin', 
                                                     '.dat', '.db', '.sqlite', '.sqlite3', 
                                                     '.jpg', '.jpeg', '.png', '.gif', '.ico',
                                                     '.pdf', '.zip', '.tar', '.gz', '.rar',
                                                     '.7z', '.mp3', '.mp4', '.avi', '.mov'}:
                        continue
                    
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    self.collected_files.append({
                        'path': file_path,
                        'relative': file_path.relative_to(self.project_path),
                        'content': content,
                        'ext': file_path.suffix.lower()
                    })
                except Exception as e:
                    print(f"  Skipping {file_path}: {e}")
        
        print(f"Found {len(self.collected_files)} files")
        return self.collected_files

    def get_lang(self, ext):
        return self.lang_map.get(ext, '')

    def make_anchor(self, text):
        """Create GitHub-style markdown anchor link"""
        anchor = str(text).lower()
        for char in ' ./\\`~!@#$%^&*()-+=[]{}|;:\'",<>?':
            anchor = anchor.replace(char, '-')
        while '--' in anchor:
            anchor = anchor.replace('--', '-')
        return anchor.strip('-')

    def build_tree(self):
        lines = [f"{self.project_name}/"]
        
        def walk(path, prefix="", is_last=True):
            try:
                entries = sorted([e for e in path.iterdir() if not self.should_exclude(e)])
            except PermissionError:
                return
            
            for i, entry in enumerate(entries):
                last = (i == len(entries) - 1)
                connector = "└── " if last else "├── "
                lines.append(f"{prefix}{connector}{entry.name}" + ("/" if entry.is_dir() else ""))
                if entry.is_dir():
                    ext = "    " if last else "│   "
                    walk(entry, prefix + ext, last)
        
        walk(self.project_path)
        return "\n".join(lines)

    def escape_code_fence(self, content, lang=''):
        """Ensure content doesn't break out of code fences"""
        # If content contains ```, use ~~~~ instead or more backticks
        if '```' in content:
            # Use 4 backticks fence
            fence = '````'
            # If even that exists, keep adding
            while fence in content:
                fence += '`'
            return f"{fence}{lang}\n{content}\n{fence}"
        return f"```{lang}\n{content}\n```"

    def generate(self):
        lines = []
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        total = len(self.collected_files)
        
        # ===== HEADER =====
        lines.append(f"# 📁 {self.project_name}")
        lines.append("")
        lines.append(f"- **Generated:** {now}")
        lines.append(f"- **Total Files:** {total}")
        lines.append(f"- **Source:** `{self.project_path}`")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # ===== TABLE OF CONTENTS =====
        lines.append("## 📑 Table of Contents")
        lines.append("")
        for i, f in enumerate(self.collected_files, 1):
            rel = str(f['relative']).replace('\\', '/')
            anchor = self.make_anchor(rel)
            lines.append(f"{i}. [{rel}](#{anchor})")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # ===== DIRECTORY TREE =====
        lines.append("## 🌲 Project Structure")
        lines.append("")
        lines.append("```")
        lines.append(self.build_tree())
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # ===== FILE CONTENTS =====
        lines.append("## 📄 Files")
        lines.append("")
        
        for f in self.collected_files:
            rel = str(f['relative']).replace('\\', '/')
            anchor = self.make_anchor(rel)
            lang = self.get_lang(f['ext'])
            content = f['content']
            
            # File header with anchor
            lines.append(f"<a id='{anchor}'></a>")
            lines.append(f"### {i}. `{rel}`")
            lines.append("")
            
            if not content.strip():
                lines.append("*Empty file*")
                lines.append("")
            else:
                lines.append(self.escape_code_fence(content, lang))
                lines.append("")
            
            lines.append("---")
            lines.append("")
        
        # Write output
        md_content = "\n".join(lines)
        self.output_path.write_text(md_content, encoding='utf-8')
        print(f"✅ Markdown saved to: {self.output_path}")
        return self.output_path


def main():
    parser = argparse.ArgumentParser(description='Convert project folder to structured Markdown')
    parser.add_argument('project_path', help='Path to the project folder')
    parser.add_argument('-o', '--output', help='Output .md path (optional)')
    args = parser.parse_args()
    
    if not os.path.isdir(args.project_path):
        print(f"Error: '{args.project_path}' is not a valid directory")
        sys.exit(1)
    
    converter = ProjectToMarkdown(args.project_path, args.output)
    converter.collect_files()
    converter.generate()


if __name__ == "__main__":
    main()