[🏠 Document Start](..\README.md) / [Centroid Dropcopy API](README.md) / Centroid Maker FIX API

# Centroid Maker FIX API

Centroid FIX 4.4 Maker API Specification v1.0.0
Changelogs
Messages
As defined in the FIX protocol, the Centroid FIX server is using two different data levels: Session and Application. The Session level
handles the delivery of data and the Application level defines the business-related data content. The following session and application
messages are supported by the Centroid FIX Engine
* Standard messages
1. Standard header
2. Standard trailer
* Session messages
1. Heartbeat (Centroid Bridge)
2. Test Request (Centroid Bridge)
3. Logon (Centroid Bridge)
4. Logout (Centroid Bridge)
5. Resend Request (Centroid Bridge)
6. Reject (Maker)
7. Business Reject (Maker)
8. Sequence Reset (Centroid Bridge)
* Application messages- Market Data Session
1. Market Data Request (Centroid Bridge)
2. Market Data Request Reject (Maker)
3. Market Data Snapshot Full Refresh (Maker)- Trading Session
1. New Order Single (Centroid Bridge)
2. Order Cancel Request (Centroid Bridge)
3. Order Cancel Replace Request (Centroid Bridge)
4. Order Cancel Reject (Maker)
5. Order Status Request (Centroid Bridge)
25-04-2023 1.0.0 Document Creation
Date Version Changes

6. Execution Report (Maker)
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
Session Messages (Admin Messages)
* Heartbeat (MsgType=0)
To be sent/received on a predefined interval basis as mentioned in the Logon message (A). Otherwise, 30 seconds be default.
8 BeginString Y Identifies beginning of new message and protocol version (always first field in message)
9 BodyLength Y Message length (in bytes) forward to the CheckSum field (always second field in
message)
35 MsgType Y Defines message type (always 3rd tag in message)
49 SenderCompID Y Assigned value used to identify the sending messages (will be provided by the Maker)
56 TargetCompID Y Assigned value used to identify receiving party (will be provided by the Maker)
34 MsgSeqNum Y Integer message sequence number
50 SenderSubID N Optional. Assigned value used to identify specific message originator (desk | trader | etc.)
(will be provided by the Maker if necessary)
52 SendingTime Y Message transmission time in UTC/GMT
Tag Field name Requir
ed
Description
10 Checksum Y Three digit character representing the checksum value of the message
Tag Field name Requir
ed
Description
Tag Field name Requir
ed
Description

* Test Request (MsgType=1)
For the purpose of testing the connectivity and responsiveness of the other party.
* Logon (MsgType=A)
Handshake logon initiated by the Centroid Bridge and confirmed by Maker.
* Logout (MsgType=5)
Handshake logout initiated by the Centroid Bridge/Maker and confirmed by the other party.
Standard
Header
Y MsgType=0
112 TestReqID N Required when the heartbeat is the result of a Test Request message
Standard Trailer Y
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
Standard
Header
Y MsgType=5
58 Text N Reason for logout
Tag Field name Requir
ed
Description

* Resend Request (MsgType=2)
* Reject (MsgType=3)
Session Level reject message.
* Business Reject (MsgType=j)
Standard Trailer Y
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
45 RefSeqNum N MsgSeqNum (34) of rejected message.
371 RefTagID Y The tag number of the FIX field being referenced.
372 RefMsgType Y Message Type being referenced.
380 BusinessReject
Reason
Y Code to identify reason for a Business Message Reject (j) message.
58 Text Y Where possible, message to explain reason for rejection.
Tag Field name Requir
ed
Description

* Sequence Reset (MsgType=4)
Market Data Session Messages
* Market Data Request (MsgType=V)
Sent by Centroid Bridge to the Maker to subscribe to a stream of market data pricing. This is to be sent a message per symbol.
* Market Data Request Reject (MsgType=Y)
A reject response to an invalid market data request (V)
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
264 MarketDepth Y Specifies the number of layers requested [Should be > 0].
7533 StreamReferenc
e
N Specifies the stream. Only needed if the Centroid Bridge is configured for more than one
streams.
267 NoMDEntryType
s
Y required but not functional currently
269 MDEntryType Y [0: Bid] [1: Ask] required but not functional currently
146 NoRelatedSym Y Always set to 1
55 Symbol Y Name of the symbol
Standard Trailer Y
Tag Field name Requir
ed
Description
Tag Field name Requir
ed
Description

* Market Data Snapshot Full Refresh (MsgType=W)
Symbol-wise, a full refresh of the full depth of the book is to be sent by the Maker to the Centroid Bridge in real-time manner as a response
to the subscription request.
Trading Session Messages
* New Order Single (MsgType=D)
Sent by Centroid Bridge to the Maker to request for a trade.
Standard
Header
Y MsgType=Y
262 MDReqID Y ID of the market data request
58 Text N Reason for market data request being rejected
Standard Trailer Y
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
11 ClOrdID Y Must be unique identifier sent by the Centroid Bridge. Used for response.
Allowed characters A-Z, a-z, ., -, _
1 Account Y Account name as provided by the Maker
55 Symbol Y Symbol to trade on
54 Side Y Side of order: [1 = Buy] [2 = Sell]
Tag Field name Requir
ed
Description

* Order Cancel Request (MsgType=F)
Available if (MsgType=D, Tag”40”=2, Tag”59”=1”GTC”) is available.
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
132 Bid N External trader's Bid Price
133 Ask N External trader's Ask Price
Standard Trailer Y
Standard
Header
Y MsgType=F
11 ClOrdID Y Must be unique identifier sent by the Centroid Bridge. Used for response
1 Account Y Target account name as provided by the Maker
41 OrigClOrdID Y The ClOrdID of the order to be cancelled
54 Side Y Side of order:[1 = Buy] [2 = Sell]
60 TransactTime Y Timestamp of the cancel request
Tag Field name Requir
ed
Description

* Order Cancel Replace Request (MsgType=G)
Available if (MsgType=D, Tag”40”=2, Tag”59”=1”GTC”) is available.

* Order Cancel Reject (MsgType=9)
Available if (MsgType=F) is available.
Standard Trailer Y
Standard
Header
Y MsgType=G
11 ClOrdID Y Must be unique identifier sent by the Centroid Bridge. Used for response
1 Account Y Target account name as provided by the Maker
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
37 OrderID Y Maker Order ID. Can be N/A or NONE indicating no order found.
11 ClOrdID Y Order Cancel Request (F) ClOrdID.
39 OrdStatus Y The Order Status of the order being cancelled.
41 OrigClOrdID Y The ClOrdID of the order to be cancelled.
102 CxlRejReason Y Reason of rejecting the Order Cancel Request.
434 CxlRejResponse
To
Y Order Cancel Request (F) message.
60 TransactTime Y Timestamp of reject response.
Tag Field name Requir
ed
Description

* Order Status Request (MsgType=H)
To be sent by Centroid to request for the status of a trade
* Execution Report (MsgType=8)
A response to New Order Single Message (D).
Order Execution Report
C - Conditionally required
Y - Required
N - Not required
Standard Trailer Y
Standard
Header
Y MsgType=H
37 OrderID C Maker Order ID.
11 ClOrdID Y The ClOrdID of the order to be requested.
1 Account Y The Target account initiated the requested order.
Standard Trailer Y
Tag Field name Requir
ed
Description
Standard
Header
Y MsgType=8
11 ClOrdID Y Unique identifier sent by the Centroid Bridge. Used for response
17 ExecID Y Unique identifier of execution message assigned by the Maker
150 ExecType Y The execution report type. [0 = New] [1 = Partially Filled] [2 = Filled] [4 = Canceled] [8 =
Rejected]
55 Symbol Y Symbol name
54 Side Y Side of order [1= Buy] [2= Sell]
38 OrderQty Y Order Quantity
40 OrdType Y [1= Market], [2= Limit], [3= Stop]
32 LastQty C Fill Quantity
59 TimeInForce Y TimeInForce
37 OrderID Y Maker order ID
Tag Field name Requir
ed
Description


Market Data Request (V)
20230424-13:56:40.788831000 : 8=FIX.4.4|9=140|35=V|34=2934|49=CENTROID_SOL|52=20230424-
13:56:40.788|56=TestMaker|146=1|55=EURUSD|262=EURUSD|263=1|264=5|265=0|267=2|269=0|269=1|10=139|
Market Data Request Reject (Y)
20230424-13:56:40.788831000: 8=FIX.4.4|9=134|35=Y|34=5|49=TestMaker|52=20230424-13:56:40.822|56=CENTROID_SOL|58=Failed
to Unsubscribe Symbol: EURUSD|262=USplain_feed2||EURUSD|10=037|
Market Data Snapshot Full Refresh (W)
20230425-11:22:17.090340000: 8=FIX.4.4|9=717|35=W|34=8292277|49=TestMaker|52=20230425-
11:22:17.082073|56=CENTROID_SOL|55=EURUSD|262=EURUSD|268=10|269=0|270=1.1021500000|271=23230000.0000000000|273=
11:22:17|269=1|270=1.1023200000|271=38267000.0000000000|273=11:22:17|269=0|270=1.1021300000|271=60138000.0000000000|27
3=11:22:17|269=1|270=1.1023400000|271=82791000.0000000000|273=11:22:17|269=0|270=1.1021000000|271=227976000.000000000
0|273=11:22:17|269=1|270=1.1023700000|271=229370000.0000000000|273=11:22:17|269=0|270=1.1020800000|271=437803000.00000
00000|273=11:22:17|269=1|270=1.1023900000|271=408756000.0000000000|273=11:22:17|269=0|270=1.1020300000|271=748278000.0
000000000|273=11:22:17|269=1|270=1.1024400000|271=601038000.0000000000|273=11:22:17|10=100|
New Order Single (D)
20230425-10:14:38.668706000 8=FIX.4.4|9=197|35=D|34=6988|49=CENTROID_SOL|52=20230425-
10:14:38.668|56=TestMaker|1=Test_tem|11=437033_1|15=EUR|21=1|38=1000|40=2|44=1.10309|54=1|55=EURUSD|59=3|60=20230425-
10:14:38.667|90008=5|10=153|
New Order Single (D) with Trades Allocation
20230425-10:14:38.668706000 8=FIX.4.4|9=197|35=D|34=6988|49=CENTROID_SOL|52=20230425-
10:14:38.668|56=TestMaker|1=Test_tem|11=437033_1|15=EUR|21=1|38=1000|40=2|44=1.10309|54=1|55=EURUSD|59=3|60=20230425-
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

10:14:38.667|90008=5|78=1|79=tem_alloc_1|80=1000|10=108|
Execution Report (8)
20230425-10:17:01.148752000: 8=FIX.4.4|9=323|35=8|34=6995|49=TestMaker|52=20230425-
10:17:01.145224|56=CENTROID_SOL|1=Test_tem|6=0.0000000000|11=437035_1|14=0.0000000000|17=239950|31=0.0000000000|32=
0.0000000000|37=239950|38=10000.0000000000|39=0|40=2|44=1.1030200000|54=1|55=EURUSD|58=New
Request|59=3|60=20230425-10:17:01|150=0|151=10000.0000000000|10=046|
Logon (A)
20230425-11:34:14.269361000: 8=FIX.4.4|9=126|35=A|34=1|49=CENTROID_SOL|52=20230425-
11:34:14.268|56=TestMaker|98=0|108=30|141=Y|553=Username|554=Password|10=032|
20230425-11:34:14.325168000: 8=FIX.4.4|9=95|35=A|34=1|49=TestMaker|52=20230425-
11:34:14.281412|56=CENTROID_SOL|98=0|108=30|141=Y|10=246|
Heartbeat (0)
20230425-11:32:01.259575000: 8=FIX.4.4|9=77|35=0|34=7143|49=CENTROID_SOL|52=20230425-11:32:01.259|56=TestMaker|10=165|

