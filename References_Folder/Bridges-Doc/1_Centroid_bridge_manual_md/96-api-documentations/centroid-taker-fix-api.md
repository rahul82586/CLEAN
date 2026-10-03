[🏠 Document Start](..\README.md) / [Centroid Maker FIX API](README.md) / Centroid Taker FIX API

# Centroid Taker FIX API

Centroid FIX 4.4 Trading API Specification v0.16.8
Changelogs
Messages
As defined in the FIX protocol, the Centroid FIX server is using two different data levels: Session and Application. The Session level
handles the delivery of data and the Application level defines the business-related data content. The following session and application
messages are supported by the Centroid FIX Engine
Standard messages
1. Standard header
2. Standard trailer
Session messages
1. Heartbeat (Client Centroid)
2. Test Request (Client Centroid)
3. Logon (Client Centroid)
4. Logout (Client Centroid)
5. Resend Request (Client Centroid)
6. Reject (Client Centroid)
7. Business Reject (Client Centroid)
8. Sequence Reset (Client Centroid)
Application messages- Market Data Session
1. Market Data Request (Client)
2. Market Data Request Reject (Centroid)
30-10-2024 v0.16.9 Added Optional tags under New Order: Security and Direction
24-01-2023 v0.16.8 Added Order Cancel Replace Request Details/ Enabled GTC Limit & Stop
14-10-2022 v0.16.7 OrigClOrdID tag 41 is now available in the FIX Execution report when requesting Limit Order
Cancel/Replace
23-05-2022 v0.16.6 Added trades allocation tags 78, 79, 80, and 661 in new order with example
25-08-2020 v0.16.5 MDEntryType tag269 added to MarketDataRequest message (V) as required
NoMDEntry tag267 added to MarketDataRequest message (V) as required
Validation on ClOrdID tag11 added in NewOrderSingle message (D)
Date Version Changes

3. Market Data Snapshot Full Refresh (Centroid)- Trading Session
1. New Order Single (Client)
2. Order Cancel Request (Client)
3. Order Cancel Replace Request (Client)
4. Order Cancel Reject (Centroid)
5. Order Status Request (Client)
6. Execution Report (Client)
Important notes
All time formats in the system are UTC.
Session timings are to be communicated with the Broker.
IP address white-listing might be required to obtain the connection.
Timestamp precision is 3 or more (microseconds or milliseconds).
Trading session is not to reset sequence number on logon.
Market data session is to reset sequence number on logon.
Standard Messages
* Standard Header
A standard set of fields to form the header of the FIX message.
* Standard Trailer
A standard set of fields to form the trailer of the FIX message.
8 BeginString Y Identifies beginning of new message and protocol version (always first field in message)
9 BodyLength Y Message length (in bytes) forward to the CheckSum field (always second field in
message)
35 MsgType Y Defines message type (always 3rd tag in message)
49 SenderCompID Y Assigned value used to identify the client sending messages (will be provided by
Centroid)
56 TargetCompID Y Assigned value used to identify receiving party (will be provided by Centroid)
34 MsgSeqNum Y Integer message sequence number
50 SenderSubID N Optional. Assigned value used to identify specific message originator (desk | trader | etc.)
(will be provided by Centroid if necessary)
52 SendingTime Y Message transmission time in UTC/GMT
Tag Field name Requir
ed
Description
Tag Field name Requir
ed
Description

Session Messages (Admin Messages)
* Heartbeat (MsgType=0)
To be sent/received on a predefined interval basis as mentioned in the Logon message (A). Otherwise, 30 seconds be default.
* Test Request (MsgType=1)
For the purpose of testing the connectivity and responsiveness of the other party.
* Logon (MsgType=A)
Handshake logon initiated by the client and confirmed by Centroid.
10 Checksum Y Three digit character representing the checksum value of the message
Standard
Header
Y MsgType=0
112 TestReqID N Required when the heartbeat is the result of a Test Request message
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=1
112 TestReqID Y A unique identifier for this test message
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=A
98 EncryptMethod Y Use of Encryption set to 0
108 HeartBtInt Y Heartbeat interval in seconds
141 ResetSeqNumFl
ag
N Indicates both sides of a FIX session should reset sequence numbers
553 Username Y Username
554 Password Y Password
Standard Trailer Y
Tag Field name Requir
ed
Description

* Logout (MsgType=5)
Handshake logout initiated by the Centroid/Client and confirmed by the other party.
* Resend Request (MsgType=2)
* Reject (MsgType=3)
Session Level reject message.
* Business Reject (MsgType=j)
Standard
Header
Y MsgType=5
58 Text N Reason for logout
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=2
7 BeginSeqNo Y
16 EndSeqNo Y
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=3
45 RefSeqNum Y MsgSeqNum of rejected message
371 RefTagID N The tag number of the FIX field being referenced
372 RefMsgType N The MsgType of the FIX message being referenced
373 SessionRejectR
eason
N Code to identify reason for a session-level
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=j
Tag Field name Requir
ed
Description

* Sequence Reset (MsgType=4)
Market Data Session Messages
* Market Data Request (MsgType=V)
Sent by the client to subscribe to a stream of market data pricing. This is to be sent a message per symbol.
45 RefSeqNum N MsgSeqNum (34) of rejected message.
371 RefTagID Y The tag number of the FIX field being referenced.
372 RefMsgType Y Message Type being referenced.
380 BusinessReject
Reason
Y Code to identify reason for a Business Message Reject (j) message.
58 Text Y Where possible, message to explain reason for rejection.
Standard Trailer Y
Standard
Header
Y MsgType=4
123 GapFillFlag N Gap fill flag to determine the need to fill the gap of sequence or no.
36 NewSeqNo Y The new sequence number requested
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard header Y MsgType=V
262 MDReqID Y Unique request id.
263 SubscriptionReq
uestType
Y [1 = Snapshot plus updates (subscribe)] [2 = Disable previous snapshot plus update
request (unsubscribe)]
264 MarketDepth N Specifies the number of layers requested [Should be > 0].
7533 StreamReferenc
e
N Specifies the stream. Only needed if a client is configured for more than one streams.
267 NoMDEntryType
s
Y required but not functional currently
269 MDEntryType Y [0: Bid] [1: Ask] required but not functional currently
146 NoRelatedSym Y Always set to 1
55 Symbol Y Name of the symbol
Tag Field name Requir
ed
Description

* Market Data Request Reject (MsgType=Y)
A reject response to an invalid market data request (V)
* Market Data Snapshot Full Refresh (MsgType=W)
Symbol-wise, a full refresh of the full depth of the book is to be sent by Centroid aggregator in real-time manner as a response to the
subscription request.
Trading Session Messages
* New Order Single (MsgType=D)
Sent by the client to request for a trade.
Standard Trailer Y
Standard
Header
Y MsgType=Y
262 MDReqID Y ID of the market data request
58 Text N Reason for market data request being rejected
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=W
262 MDReqID Y Refers to the MDReqID of the request
55 Symbol Y Symbol to trade on
268 NoMDEntries Y Number of entries following
269 MDEntryType Y [0: Bid] [1: Ask]
270 MDEntryPx N Price of the Market Data Entry.
271 MDEntrySize N Quantity or volume represented by the Market Data Entry.
273 MDEntryTime N Market Data Entry Time
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=D
Tag Field name Requir
ed
Description

* Order Cancel Request (MsgType=F)
Available if (MsgType=D, Tag”40”=2, Tag”59”=1”GTC”) is available.
11 ClOrdID Y Must be unique identifier sent by the client. Used for response.
Allowed characters A-Z, a-z, ., -, _
1 Account Y Account name as provided by Centroid
55 Symbol Y Symbol to trade on
54 Side Y Side of order: [1 = Buy] [2 = Sell]
38 OrderQty Y Order Quantity
40 OrdType Y Type of order: [1 = Market] [2=Limit] [3=Stop]
59 TimeInForce Y GTC, IOC, FOK
(Time in force execution may vary depending on the execution settings on the broker’s
interface)
44 Price C Required when OrdType”40” =2 (Limit). Otherwise, ignored.
60 TransactTime Y Timestamp of order request
78 NoAllocs N number of allocation accounts if using trades allocation
79 AllocAccount C TEM to allocate trade under – mandatory if using tag 78
80 AllocQty C quantity to be allocated – mandatory if using tag 78

661 AllocAcctIDSour
ce
C Allocation: [0=A Alloc] [1=B Alloc] (Default is 0) - Optional
90000 TTL N Time to live (milliseconds)
90001 Login N External trader’s login can be passed here
90002 Group N External trader's Group
90003 Ticket N External Order Ticket number
90008 Deviation N Should be decimal number
90009 Contract Size N External Contract size for instrument. e.g for EURUSD 100000
90013 Platform
Security
N Securities Folder Name
90014 Direction N Direction of the order: [1 = In] [2 = Out]
Including this tag specifies the direction of trades as either 'IN' or 'OUT' for the respective
order.
132 Bid N External trader's Bid Price
133 Ask N External trader's Ask Price
Standard Trailer Y

* Order Cancel Replace Request (MsgType=G)
Available if (MsgType=D, Tag”40”=2, Tag”59”=1”GTC”) is available.
* Order Cancel Reject (MsgType=9)
Available if (MsgType=F) is available.
Standard
Header
Y MsgType=F
11 ClOrdID Y Must be unique identifier sent by the client. Used for response
1 Account Y Account name as provided by Centroid
41 OrigClOrdID Y The ClOrdID of the order to be cancelled
54 Side Y Side of order:[1 = Buy] [2 = Sell]
60 TransactTime Y Timestamp of the cancel request
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=G
11 ClOrdID Y Must be unique identifier sent by the client. Used for response
1 Account Y Account name as provided by Centroid
41 OrigClOrdID Y The ClOrdID of the order to be replaced
54 Side N Side of order:[1 = Buy] [2 = Sell]
38 OrderQty N Order Quantity
40 OrdType N Type of order: [1 = Market] [2=Limit] [3=Stop]
59 TimeInForce N GTC, IOC, FOK
44 Price N Required when OrdType”40” =2 (Limit). Otherwise, ignored.
60 TransactTime Y Timestamp of the cancel request
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=9
Tag Field name Requir
ed
Description

* Order Status Request (MsgType=H)
To be sent by the client to request for the status of a trade
* Execution Report (MsgType=8)
A response to New Order Single Message (D).
Order Execution Report
C - Conditionally required
Y - Required
N - Not required
37 OrderID Y Centroid Order ID. Can be N/A or NONE indicating no order found.
11 ClOrdID Y Order Cancel Request (F) ClOrdID.
39 OrdStatus Y The Order Status of the order being cancelled.
41 OrigClOrdID Y The ClOrdID of the order to be cancelled.
102 CxlRejReason Y Reason of rejecting the Order Cancel Request.
434 CxlRejResponse
To
Y Order Cancel Request (F) message.
60 TransactTime Y Timestamp of reject response.
Standard Trailer Y
Standard
Header
Y MsgType=H
37 OrderID C Centroid Order ID.
11 ClOrdID Y The ClOrdID of the order to be requested.
1 Account Y The account initiated the requested order.
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=8
11 ClOrdID Y Must be unique identifier sent by the client. Used for response
17 ExecID Y Unique identifier of execution message assigned by Centroid Gateway
150 ExecType Y The execution report type. [0 = New] [1 = Partially Filled] [2 = Filled] [4 = Canceled] [8 =
Rejected]
Tag Field name Requir
ed
Description

Market Data Request (V)
20170321-11:51:32.201632000 : 8=FIX.4.4|9=151|35=V|34=8|49=TraderSender|52=20170321-
11:51:32.201|56=CENTROID_SOL|146=1|55=EURUSD|262=US1pip_feed||EURUSD|263=2|264=0|267=2|269=0|269=1|10=210|
Market Data Request Reject (Y)
20170321-11:51:24.201729000 : 8=FIX.4.4|9=134|35=Y|34=5|49=CENTROID_SOL|52=20170321-
11:51:24.201850|56=TraderSender|58=Failed to Unsubscribe Symbol: EURUSD|262=USplain_feed2||EURUSD|10=037|
Market Data Snapshot Full Refresh (W)
20170321-11:51:33.083494000 : 8=FIX.4.4|9=183|35=W|34=6|49=CENTROID_SOL|52=20170321-
11:51:33.083245|56=TraderSender|55=EURUSD_1|262=1|268=2|269=0|270=1.13882|271=1000000|273=11:51:33|269=1|270=1.13904|2
71=4000000|90007=1pip_feed|10=082|
20170321-11:55:43.514924000 : 8=FIX.4.4|9=182|35=W|34=16|49=CENTROID_SOL|52=20170321-
11:55:43.514831|56=TraderSender|55=EURUSD_1|262=1|268=2|269=0|270=1.13908|271=986000|273=11:55:43|269=1|270=1.1393|271
=2502000|10=069|
55 Symbol Y Symbol name
54 Side Y Side of order [1= Buy] [2= Sell]
38 OrderQty Y Order Quantity
40 OrdType Y [1= Market], [2= Limit], [3= Stop]
32 LastQty C Fill Quantity
59 TimeInForce Y TimeInForce
37 OrderID Y Centroid Gateway order ID
39 OrdStatus Y Current order state. [0 = New] [1 = Partially filled] [2 = Filled] [4 = Canceled] [8 =
Rejected]
41 OrigClOrdID C The ClOrdID of the order to be cancelled.
31 LastPx C Price of this fill.
151 LeavesQty C Remaining quantity open for execution
14 CumQty C Cumulative quantity executed
6 AvgPx C Average price of executed quantity
44 Price N Price of the Limit order
58 Text Y Free format text string
60 TransactTime Y Time of the transaction
Standard Trailer Y
Examples of FIX Messages

New Order Single (D)
20170321-11:51:40.225951000 : 8=FIX.4.4|9=186|35=D|34=10|49=TraderSender|52=20170321-
11:51:40.225|56=CENTROID_SOL|1=MT5_Plain|11=BI9NLJ5674FDPRD79NGG|38=1000|40=1|54=1|55=EURUSD_1|59=3|60=2017032
1-11:51:40.222|132=1.13882|133=1.13904|10=108|
New Order Single (D) with Trades Allocation
20220320-14:31:41.33651000 : 8=FIX.4.4|9=186|35=D|34=10|49=TraderSender|52=20220320-
14:31:41.336|56=CENTROID_SOL|1=tem_plain|11=DO9NLJ5674ASGJHASFHF|38=1000|40=1|54=1|55=EURUSD_1|59=3|60=2022032
0-14:31:41.330|78=1|79=tem_alloc_1|80=1000|10=108|
New Order Single (D) with Custom Tags
20170321-11:51:40.225951000 : 8=FIX.4.4|9=186|35=D|34=10|49=TraderSender|52=20170321-
11:51:40.225|56=CENTROID_SOL|1=tem_Plain|11=BI9NLJ5674FDPRD79NGG|38=1000|40=1|54=1|55=EURUSD_1|59=3|60=20170321
-11:51:40.222|132=1.13882|133=1.13904|90001=101112|90002=real\group\Standard|90003=7863455|90013=Forex|90014=1|10=108|
Execution Report (8)
20170321-11:51:40.228926000 : 8=FIX.4.4|9=277|35=8|34=8|49=CENTROID_SOL|52=20170321-
11:51:40.228846|56=TraderSender|1=MT5_Plain|6=0|11=BI9NLJ5674FDPRD79NGG|14=0|17=000120170321000000000000|31=0|32=0|
37=000120170321000000000000|38=1000|39=0|40=1|54=1|55=EURUSD_1|58=N/A|59=3|60=20170321-
11:51:40|150=0|151=1000|9999=CenSystem|10=213|
Logon (A)
20170321-11:54:01.992036000 : 8=FIX.4.4|9=117|35=A|34=1|49=TraderSender|52=20170321-
11:54:01.991|56=CENTROID_SOL|98=0|108=30|141=Y|553=Username|554=Password|10=063|
20170321-11:54:01.992804000 : 8=FIX.4.4|9=86|35=A|34=1|49=CENTROID_SOL|52=20170321-
11:54:01.992734|56=TraderSender|98=0|108=30|141=Y|10=076|
Heartbeat (0)
20170321-11:55:47.725747000 : 8=FIX.4.4|9=65|35=0|34=4|49=TraderSender|52=20170321-11:55:47.725|56=CENTROID_SOL|10=092|

