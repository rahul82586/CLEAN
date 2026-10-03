[🏠 Document Start](..\README.md) / [Logs](README.md) / Maker Status

# Maker Status

Overview
The Maker Status component provides real-time health into the connectivity with Makers to ensure that Maker Sessions are connected at
all times in addition to providing statistical data about the connection in addition to prices and execution for each Maker on a per Symbols
basis.
Maker Status
The Maker Status monitoring tool provides real-time visibility over the different sessions i.e. Feeding and Trading of different Makers to
determine whether the session is connected or not. It also provides statistical data in terms of exchange from and into the Centroid Bridge.
Maker The Maker's name can be configured either as a single session encompassing both Feeding and Trading, or as two
separate sessions—Feeding and Trading—depending on the specifications of the Maker.
Status Indicates the status of the connection:
Enabled: If the Maker is enabled from the Maker section.
Disabled: If the Maker is disabled from the Maker section.
STime Indicates whether the connection is within the defined time session:
Within Time: If the connection falls within the specified time session.
Outside Time: If the connection extends beyond the defined time session. For instance, if the Time Session is set from
Monday to Friday, Saturday would be categorized as Outside Time.
Logged
in
Specifies the session's connection status:
Connected: If there is an established connection between the Maker and the Centroid Bridge.
Disconnected: If there is no established connection between the Maker and the Centroid Bridge.
Receive
d
Count
The count of messages received by the Centroid Bridge from the Maker.
Sent
Count
The count of messages sent by the Centroid Bridge to the Maker.
Field Description

Maker Symbol Status
The Maker Symbol status is a very useful real-time tool that allows checking of statistical data with each Maker on a per Symbol basis.
Data are related to prices obtained from the Makers in addition to Orders that are routed to the Makers.
You need to select a combination of at least one Maker and Symbol for the report to be generated.
The report is reset every five minutes where the Centroid Bridge starts counting all over again until the next reset.
Within this module, you have the capability to:
Filter: Click on the four lines next to the Maker and select the desired Maker.
Select/Tick Security or Symbol: Choose a Security or Symbol by selecting or ticking the desired ones.
Export Report (Excel/CSV): Save the report by exporting it to an Excel or CSV file.
Maker The name of the Maker.
Symbol The name of the Symbol under a specific security.
Sub ID The Symbol’s market data subscription ID that is sent to the Maker upon subscription.
Subscribed Indicates whether we are subscribed to the Symbol with the Maker or not.
If ticked, it means we are subscribed to the Symbol.
If un-ticked, it means we are not subscribed to the Symbol.
Ticks Count The number of Ticks or prices updates received for that Symbol during the 5-minute time interval.
Note: If Ticks says “0” that means the respective Maker is not pricing.
Avg Spread The Average Spread of the Symbol in decimal.
Avg Spread
in Points
The Average Spread of the Symbol in points.
Spread Ticks
Count
The number of Ticks or prices updates received for that Symbol based on which the average spread was calculated
during the current time interval.
Delayed
Ticks Count
The number of Ticks or prices updated that were delayed.
Orders Count The total number of Orders executed with the Maker during the time interval irrespective of the Order Size. In other
words, if executed Order is counted as 1 no matter what the Volume is.
Long Orders The total number of Long Orders executed with the Maker during the time interval irrespective of the Order Size.
Short Orders The total number of Short Orders executed with the Maker during the time interval irrespective of the Order Size.
Avg Fill Time The Average Fill Time in microseconds of all Orders that were executed during the current time interval.
Field Description

Avg Travel
Time
The Average Time in microseconds it takes the Order to travel from the Centroid Bridge to the Maker.
Rejected
Count
The number of rejected Orders.
Partial Fills
Count
The number of Orders that resulted in partial fills.
Fully Fills
Count
The number of Orders that were fully filled.
Total Till
Volume
The total notional Volume executed with the Maker during the 5 minute time interval.
Average
Slippage
The Average Slippage in decimals of all executed Orders.
Average
Slippage
Points
The Average Slippage in points of all executed Orders.

