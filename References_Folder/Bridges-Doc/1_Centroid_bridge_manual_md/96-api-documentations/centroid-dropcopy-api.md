[🏠 Document Start](..\README.md) / [Centroid Database Specification](README.md) / Centroid Dropcopy API

# Centroid Dropcopy API

Centroid FIX 4.4 DropCopy API Specification v1.1
Changelogs
Messages
As defined in the FIX protocol, the Centroid FIX server uses two different data levels: Session and Application. The Session level handles
the delivery of data and the Application level defines the business-related data content. The following session and application messages
are supported by the Centroid FIX Engine:
* Standard messages
1. Standard header
2. Standard trailer
* Session messages
1. Heartbeat (Client Centroid)
2. Test Request (Client Centroid)
3. Logon (Client Centroid)
4. Logout (Client Centroid)
5. Resend Request (Client Centroid)
6. Reject (Client Centroid)
7. Business Reject (Client Centroid)
8. Sequence Reset (Client Centroid)
* Application messages- Trading Session
1. Execution Report (Client Centroid)
Important notes
All time formats in the system are UTC.
Session timings are to be communicated with the Broker.
IP address white-listing is required to obtain the connection to live server.
Timestamp precision is 3 or more (microseconds or milliseconds).
Trading Session is to reset sequence number on logon.
Giveup rule is required to be set up by centroid client.
08-02-2021 1.1 Enhanced Execution Report – Added available external information
13-08-2021 1.0 Enhanced Execution Report
Date Version Changes

For customized tags mentioned in the Execution report, Centroid support team can enable it upon request
Standard Messages
* Standard Header
A standard set of fields to form the header of the FIX message.
* Standard Trailer
A standard set of fields to form the trailer of the FIX message.

Session Messages (Admin Messages)
* Heartbeat (MsgType=0)
8 BeginString Y Identifies beginning of new message and protocol version (always first field in message)
9 BodyLength Y Message length (in bytes) forward to the Checksum field (always second field in
message)
35 MsgType Y Defines message type (always 3rd tag in message)
49 SenderCompID Y Assigned value used to identify the client sending messages (will be provided by
Centroid)
56 TargetCompID Y Assigned value used to identify receiving party (will be provided by Centroid)
34 MsgSeqNum Y Integer message sequence number
50 SenderSubID N Optional. Assigned value used to identify specific message originator (desk | trader |
etc.) (will be provided by Centroid if necessary)
52 SendingTime Y Message transmission time in UTC/GMT
Tag Field name Require
d
Description
10 Checksum Y Three-digit character representing the checksum value of the message
Tag Field name Require
d
Description
Standard
Header
Y MsgType=0
112 TestReqID N Required when the heartbeat is the result of a Test Request message
Standard Trailer Y
Tag Field name Require
d
Description

* Test Request (MsgType=1)
It is intended to test the connectivity and responsiveness of the other party.
* Logon (MsgType=A)
Handshake logon initiated by the client and confirmed by Centroid.
* Logout (MsgType=5)
* Resend Request (MsgType=2)
Standard
Header
Y MsgType=1
112 TestReqID Y A unique identifier for this test message
Standard Trailer Y
Tag Field name Require
d
Description
Standard
Header
Y MsgType=A
98 EncryptMethod Y Use of Encryption set to 0
108 HeartBtInt Y Heart beat interval in seconds
141 ResetSeqNumF
lag
N Indicates both sides of a FIX session should reset sequence numbers
553 Username Y Username
554 Password Y Password
Standard Trailer Y
Tag Field name Require
d
Description
Standard
Header
Y MsgType=5
58 Text Y Reason for logout
Standard Trailer Y
Tag Field name Require
d
Description
Standard
Header
Y MsgType=2
Tag Field name Required Description

* Reject (MsgType=3)
* Business Reject (MsgType=j)
* Sequence Reset (MsgType=4)
7 BeginSeqNo Y
16 EndSeqNo Y
Standard Trailer Y
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
Tag Field name Required Description
Standard
Header
Y MsgType=j
45 RefSeqNum N MsgSeqNum (34) of rejected message.
371 RefTagID Y The tag number of the FIX field being referenced.
372 RefMsgType Y Message Type being referenced.
380 BusinessReject
Reason
Y Code to identify reason for a Business Message Reject (j) message.
58 Text Y Where possible, message to explain the rejection reason
Standard Trailer Y
Tag Field name Required Description
Standard Header Y MsgType=4
123 GapFillFlag N Gap fill flag to determine the need to fill the gap of sequence or not.
36 NewSeqNo Y The new sequence number requested
Standard Trailer Y
Tag Field name Required Description

* Execution Report (MsgType=8)
Order Execution Report
C - Conditionally required
Y - Required
N - Not required
Standard Header Y MsgType=8
1 Account N Name of the trading account
11 ClOrdID Y Must be unique identifier sent by the client. Used for response
17 ExecID Y Unique identifier of execution message assigned by Centroid Gateway
150 ExecType Y The execution report type. [2 = Filled]
55 Symbol Y Symbol name
54 Side Y Side of order [1 = Buy] [2 = Sell]
38 OrderQty Y Order Quantity
40 OrdType Y [1 = Market], [2 = Limit], [3 = Stop]
32 LastQty C Fill Quantity
59 TimeInForce Y TimeInForce [1 = GTC], [3 = IOC], [4 = FOK]
37 OrderID Y Centroid Gateway order ID
39 OrdStatus Y Current order state. [1 = Partially filled] [2 = Filled]
31 LastPx C Price of this fill.
151 LeavesQty C Remaining quantity open for execution
14 CumQty C Cumulative quantity executed
6 AvgPx C Average price of executed quantity
44 Price N Price of the Limit order
58 Text Y Free format text string
60 TransactTime Y Time of the transaction
90001 Login N External Login/Account from MT4/MT5
90002 Group N External Group from MT4/MT5
90003 Order N External OrderID/Ticket number
90006 Position ID N External Position number from MT4/MT5
90010 B Filled N BBook Filled Volume
90011 External Markup N External added Markup from the Taker
132 Bid Price N External Bid
Tag Field name Required Description


Notes: the example messages below are client views on how the messages are expected to be received when sent by the dropcopy.
Execution Report (MsgType=8)
* Fully Filled:
20210810-21:44:27.038873000 [in] : 8=FIX.4.4 | 9=290 | 35=8 | 34=909 | 49=CENTROID_SOL | 52=20210810-21:44:27.036905 |
56=DC_Centroid | 1=test_tem | 6=1.17218000 | 11=4797_1-12 | 14=1000.00000000 | 17=507114-12 | 31=1.17218000 |
32=1000.00000000 | 37=507114-12 | 38=1000.00000000 | 39=2 | 40=1 | 54=2 | 55=EURUSD | 58=N/A | 59=3 | 60=20210810-21:44:27 |
150=2 | 151=0.00000000 | 10=041 |
* Fully Filled through multiple Partial Fills:
20210810-22:49:19.866761000 [in] : 8=FIX.4.4 | 9=303 | 35=8 | 34=1043 | 49=CENTROID_SOL | 52=20210810-22:49:19.865676 |
56=DC_Centroid | 1=test_tem | 6=1.17213000 | 11=4801_1-12 | 14=20000000.00000000 | 17=507118-12 | 31=1.17213000 |
32=20000000.00000000 | 37=507118-12 | 38=20000000.00000000 | 39=2 | 40=1 | 54=2 | 55=EURUSD | 58=N/A | 59=3 | 60=20210810-
22:49:19 | 150=2 | 151=0.00000000 | 10=154 |
* Partially Filled
20210810-22:49:16.693604000 [in] : 8=FIX.4.4 | 9=308 | 35=8 | 34=1042 | 49=CENTROID_SOL | 52=20210810-22:49:16.692405 |
56=DC_Centroid | 1=test_tem | 6=1.17213000 | 11=4800_1-12 | 14=24750000.00000000 | 17=507117-12 | 31=1.17213000 |
32=24750000.00000000 | 37=507117-12 | 38=25000000.00000000 | 39=1 | 40=1 | 54=2 | 55=EURUSD | 58=N/A | 59=3 | 60=20210810-
22:49:16 | 150=2 | 151=250000.00000000 | 10=164 |
* With Customized Tags
20220208-08:45:16.155807000 [in] : 8=FIX.4.4 | 9=411 | 35=8 | 34=16 | 49=CENTROID_SOL | 52=20220208-08:45:16.151684 |
56=DC_Centroid_DropCopy | 1=test_tem | 6=1.14029000 | 11=32867651006464-12 | 14=1000.00000000 | 17=3566625-12 |
31=1.14029000 | 32=1000.00000000 | 37=3566625-12 | 38=1000.00000000 | 39=2 | 40=1 | 54=2 | 55=EURUSD | 58=Execution | 59=4 |
60=20220208-08:45:16 | 132=1.14023000 | 133=1.14035000 | 150=2 | 151=0.00000000 | 90001=1014 | 90002=real\test\a-book |
90003=2970554 | 90006=2970553 | 90011=-0.00006000 | 10=122 |
Logon (MsgType=A)
20210720-14:31:59.705542000 [in] : 8=FIX.4.4 | 9=128 | 35=A | 34=1 | 49=DC_Centroid | 52=20210720-14:31:59.703 |
56=CENTROID_SOL | 98=0 | 108=30 | 141=Y | 553=Username | 554=Password | 10=140 |
20210720-14:31:59.707057000 [out] : 8=FIX.4.4 | 9=96 | 35=A | 34=1 | 49=CENTROID_SOL | 52=20210720-14:31:59.707021 |
56=DC_Centroid | 98=0 | 108=30 | 141=Y | 10=026 |
Logout (MsgType=A)
20210720-14:32:40.749544000 [in] : 8=FIX.4.4 | 9=87 | 35=5 | 34=3 | 49=DC_Centroid | 52=20210720-14:32:40.747 |
56=CENTROID_SOL | 58=disabled | 10=021 |
133 Offer Price N External Ask
Standard Trailer Y
Examples of FIX Messages

20210720-14:32:40.750004000 [out] : 8=FIX.4.4 | 9=78 | 35=5 | 34=3 | 49=CENTROID_SOL | 52=20210720-14:32:40.749980 |
56=DC_Centroid | 10=213 |
Heartbeat (MsgType=0)
20210720-14:32:29.734267000 [out] : 8=FIX.4.4 | 9=78 | 35=0 | 34=2 | 49=CENTROID_SOL | 52=20210720-14:32:29.734216 |
56=DC_Centroid | 10=200 |
20210720-14:32:29.742891000 [in] : 8=FIX.4.4 | 9=75 | 35=0 | 34=2 | 49=DC_Centroid | 52=20210720-14:32:29.735 |
56=CENTROID_SOL | 10=045 |
Business Reject (MsgType=j)
20210720-14:40:35.990273000 [in] : 8=FIX.4.4 | 9=122 | 35=j | 34=2 | 49=CENTROID_SOL | 52=20210720-14:40:35.989175 |
56=DC_Centroid | 45=2 | 58=Invalid Session | 371=35 | 372=D | 380=11 | 10=029 |
Reject (MsgType=3)
20210720-14:40:35.990389000 [out] : 8=FIX.4.4 | 9=141 | 35=3 | 34=3 | 49=DC_Centroid | 52=20210720-14:40:35.990 |
56=CENTROID_SOL | 45=2 | 58=Tag not defined for this message type | 371=371 | 372=j | 373=2 | 10=069 |


