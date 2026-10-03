Absolutely. I’ll keep **all critical details, commands, URLs, credentials, ports, endpoints, and examples unchanged**, while improving only the structure and readability.

 MT5 Manager & Trade Server — Commands and Documentation

# MT5 Manager & Trade Server Documentation

 ## 1\. Start the Manager Service

 **Swagger Docs:** Broker Platform API

 Start the Manager service on port `8001`:

```
$env:SERVICE_MODE="manager"
python -m uvicorn api.main:app --reload --port 8001
```

---

 ## 2\. Start the Trade Server — LP MT5 Server

 Start the Trade Server on port `8000`:

```
python -m uvicorn api.main:app --port 8000
```

 ### MT5 Terminal Configuration

```
"path": "",
"login": "",
"password": "",
"server": ""
```

---

 # 3\. Manager API — Order Commands

 The following commands use the Manager API running on:

```
http://127.0.0.1:8001
```

 ## Authentication

 The commands below use this authorization token:

```
xxxxxxxxxxxxxxxxxxxxx
```

---

 ## 4\. Place A-Book Market BUY Order

 **Symbol:** BTCUSD\
 **Volume:** 0.01 lot\
 **Routing:** A-Book

```
curl.exe -s -X POST -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxx" \
  "http://127.0.0.1:8001/api/v1/manager/OrderSend?id=1&login=744209&symbol=BTCUSD&operation=buy&lots=0.01&price=84000&comment=market_buy_abook&fill_type=IOC&routing=A-Book"
```

---

 ## 5\. Place A-Book Market SELL Order

 **Symbol:** BTCUSD\
 **Volume:** 0.01 lot\
 **Routing:** A-Book

```
curl.exe -s -X POST -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
  "http://127.0.0.1:8001/api/v1/manager/OrderSend?id=1&login=744209&symbol=BTCUSD&operation=sell&lots=0.01&price=84000&comment=market_sell_abook&fill_type=IOC&routing=A-Book"
```

---

 ## 6\. Place B-Book Market BUY Order

 **Purpose:** Internalized Risk\
 **Symbol:** BTCUSD\
 **Volume:** 0.01 lot\
 **Routing:** B-Book

```
curl.exe -s -X POST -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxx" \
  "http://127.0.0.1:8001/api/v1/manager/OrderSend?id=1&login=744209&symbol=BTCUSD&operation=buy&lots=0.01&price=84000&comment=market_bbook_test&fill_type=IOC&routing=B-Book"
```

---

 # 7\. Close an Open Market Position

 ### `/OrderClose`

 Replace:

```
<TICKET_OR_POS_ID>
```

 with your actual position ticket.

 Examples:

```
5311316
```

 or:

```
pos_744209_BTCUSD_f19f62
```

 Command:

```
curl.exe -s -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
  "http://127.0.0.1:8001/api/v1/manager/OrderClose?ticket=<TICKET_OR_POS_ID>&lots=0.01&price=84500"
```

---

 # 8\. Delete / Close A-Book Order

 Replace the ticket ID at the end of the URL.

 Example:

```
curl.exe -s -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" "http://127.0.0.1:8001/api/v1/manager/OrderDelete?ticket=5311321"
```

---

 # 9\. Market Order Close Command

 Example using ticket:

```
5311326
```

```
curl.exe -s -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" "http://127.0.0.1:8001/api/v1/manager/OrderClose?ticket=5311326"
```

---

 # 10\. Additional Reference

 All details have also been logged into:

```
# 🟢 Ram #-87:
# 🔵 Gemini #-87:
```

 Reference file:

```
chat/chat2.md
```

 Relevant section:

```
chat2.md:1850-1879
```

---

 # 11\. Create a `.bundle` File

 A `.bundle` file is a **Git repository bundle**.

 It can be uploaded/shared and later extracted using Git.

 ## Important

 The folder must first be a Git repository.

 If `MetaTrader5Manager` is already a Git repository:

```
EXAMPLE
cd /d E:\references-for-AIs-to-read-main\bundle\m18\m18-references-for-AIs-to-read\MetaTrader5Manager
git bundle create MetaTrader5Manager.bundle --all
```

 This creates:

```
MetaTrader5Manager.bundle
```

---

 # 12\. Extract the `.bundle`

 To extract/clone the bundle:

```
git clone MetaTrader5Manager.bundle MetaTrader5Manager
```

 This will create:

```
MetaTrader5Manager
```

 containing the Git repository from the bundle.

---

 # 13\. Quick Reference

 | Component | Port | Command |
| --- | --- | --- |
| Manager Service | `8001` | `python -m uvicorn api.main:app --reload --port 8001` |
| Trade Server / LP MT5 | `8000` | `python -m uvicorn api.main:app --port 8000` |
| Manager API | `8001` | `http://127.0.0.1:8001` |
| Bundle Extraction | — | `git clone MetaTrader5Manager.bundle MetaTrader5Manager` |

## Main Manager Endpoints

```
POST /api/v1/manager/OrderSend
GET  /api/v1/manager/OrderClose
GET  /api/v1/manager/OrderDelete
```

 > **Note:** The endpoint methods shown in this quick reference are based on the commands above; use the Swagger documentation as the authoritative API definition.

---
