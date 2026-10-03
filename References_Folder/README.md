# 📚 References Folder — AI & Developer Index

Welcome to the **References Directory**. This folder contains official MetaTrader 5 (MT5) specifications, live server exports, bridge manuals, binary decoders, and institutional trading open-source reference codebases.

---

## 🗂️ Master Reference Index

| Reference Category | Directory / File | Key Topics & Contents (What This Holds) |
| :--- | :--- | :--- |
| **MT5 SDK Specs** | [`MT5SDK-Doc/`](./MT5SDK-Doc/) | Native C++/Python SDK headers, interfaces (`IMTUser`, `IMTConGroup`, `IMTOrder`, `IMTDeal`, `IMTPosition`, `IMTConSymbol`), MT5 API docs, retcodes (`MT_RET_OK`), enumerations, full compiled single-file specification (`Include.md`), structure field maps. |
| **MT5 Admin Docs** | [`MT5Admin-Doc/`](./MT5Admin-Doc/) | Administrator user manual, server architecture, feeder configs, group setup, manager rights tabs, risk rules, trade routes, security, gateway configurations, cluster management. |
| **MT5 Manager Docs** | [`MT5Manager-Doc/`](./MT5Manager-Doc/) | Manager console manual, dealer execution, balance/credit operations, account creation, margin adjustments, group overrides, trade modifications, client management APIs. |
| **LP & Bridge Specs** | [`Bridges-Doc/`](./Bridges-Doc/) | Centroid Liquidity Bridge manuals (`1_Centroid_bridge_manual_md`), STP routing, FIX engine specs, LP bridge protocols, MatchTrader specs, uBridge user manual (`uBridge-Usermanual.pdf`). |
| **Live Server Configs** | [`MT5_Exported_files_reference/`](./MT5_Exported_files_reference/) | Real production MT5 JSON config exports (`Symbols`, `Groups`, `Routing`, `Gateways`, `Data Feeds`, `Subscriptions`, `Automation`, `Plugins`, `Reports`, `Security`). |
| **Deployed Server Layout** | [`1_MT5_Real_deployed_server_reference/`](./1_MT5_Real_deployed_server_reference/) | Real MT5 server installation file system (`mt5trade64.exe`, `bases/`, `config/`, `plugins/`, `logs/`, `FXConnect/`, `settings/`, `WebAPI/`, backup utilities). |
| **Binary File Decoders** | [`MT5__dat_idx_decode_files/`](./MT5__dat_idx_decode_files/) | Native MT5 database binary decoders (`.dat` / `.idx`), position analysis markdown, decoded order histories, deal logs, byte layouts. |
| **Security Certificates** | [`MT5_Certificates/`](./MT5_Certificates/) | SSL/TLS connection certificates, MT5 web API keys, cluster authentication files. |
| **Open-Source Trading Repos** | [`GitHub-repos-for-refernce/`](./GitHub-repos-for-refernce/) | 19 HFT & FX trading codebases: `nautilus_trader`, `matching-core`, `exchange-core`, `oms-order-management-system`, `DeFi-Arbitrage-Engine`, `otc-rfq`, `FastCharts`, `FinceptTerminal`, `OmniQuant`, `obscura`. |
| **Architectural Summaries** | [`opencode_summery.md`](./opencode_summery.md) & [`links-from-opencode-chat-file.md`](./links-from-opencode-chat-file.md) | Architectural plans, open-source reference breakdowns, external documentation URLs, and design notes. |

---

## 📁 Detailed Contents & Keyword Index

### 1. [`MT5SDK-Doc/`](./MT5SDK-Doc/)
* **`MetaTrader5SDK/`**: Per-class Markdown documentation. Holds: `IMTConGroup`, `IMTConSymbol`, `IMTUser`, `IMTOrder`, `IMTDeal`, `IMTPosition`, `IMTConRoute`, `IMTConManager`, `IMTGateway`, `IMTReportAPI`.
* **`mt5 sdk single md file/`**: Single compiled Markdown document containing the entire MT5 SDK surface in one place.
* **`mtapi-docs/`**: Native MT5 API method signatures, return codes, and memory management rules.

### 2. [`MT5Admin-Doc/`](./MT5Admin-Doc/)
* **`MetaTrader5Administrator/`**: Administrator console guide. Holds: Server cluster setup, routing rules, feeder configuration, group creation, leverage control, margin mode definitions, manager rights matrices.
* **`Single_MetaTrader5Administrator/`**: Monolithic single-page Administrator documentation reference.

### 3. [`MT5Manager-Doc/`](./MT5Manager-Doc/)
* **`MetaTrader5Manager/`**: Manager console guide. Holds: Dealer operations, manual order entry, account credit/deposit adjustments, client profile editing, trade modification, risk monitoring tools.

### 4. [`Bridges-Doc/`](./Bridges-Doc/)
* **`1_Centroid_bridge_manual_md/`** & **`2_Single_Centroid_bridge_manual_md/`**: Centroid Liquidity Bridge technical manuals (A-Book execution, FIX protocol specs, STP routing rules, LP aggregation).
* **`3_matchtarder/`**: MatchTrader bridge integration specs.
* **`4_uBridge-Usermanual.pdf`**: Complete uBridge technical manual.

### 5. [`MT5_Exported_files_reference/`](./MT5_Exported_files_reference/)
* Real production JSON configuration exports from `TCTrader-Live`:
  - `Symbols TCTrader-Live.json` (Real contract sizes, digits, margin calculations, swap modes)
  - `Groups TCTrader-Live.json` (Real group definitions, leverage tiers, commission structures)
  - `Routing TCTrader-Live.json` (Execution rules & condition maps)
  - `Gateways TCTrader-Live.json` & `Data Feeds TCTrader-Live.json`
  - `Subscriptions`, `Automation`, `Plugins`, `Reports`, `Security`

### 6. [`GitHub-repos-for-refernce/`](./GitHub-repos-for-refernce/)
Collection of 19 open-source trading repositories:
- **`nautilus_trader-develop`**: Production-grade algorithmic trading platform in Rust/Python.
- **`matching-core-master`** & **`exchange-core-master`**: Ultra-low latency LMAX Disruptor order matching engine.
- **`OMS-Ultra-Low-Latency-Order-Management-System-main`**: C++ Order Management System.
- **`FinceptTerminal-main`**, **`FastCharts-main`**, **`market-maker-rs-main`**, **`hurtrade-trading-platform-forex-master`**.

---

## 🤖 Guidance for AI Agents & Developers

* **Do not limit search by assumptions**: Each folder contains extensive technical details beyond short summaries.
* **Use relative paths**: All links in this document use relative paths (`./`) to remain portable.
* **Use `grep_search`**: Search for specific MT5 class names or keywords across these folders as needed.
