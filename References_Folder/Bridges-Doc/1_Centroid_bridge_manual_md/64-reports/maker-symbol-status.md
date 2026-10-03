[🏠 Document Start](..\README.md) / [Maker Symbol Chart](README.md) / Maker Symbol Status

# Maker Symbol Status

Overview
The Maker Symbol Status report offers a comprehensive look into various statistical data associated with pricing and trading with the
Maker, organized on a per-Symbol basis. The Centroid Bridge captures a snapshot every 5 minutes, consolidating the information into
records with all relevant statistics for each Symbol during the specified interval.
This report serves as a valuable tool for assessing the performance of each Maker in terms of pricing and execution. It plays a crucial role
in aiding Brokers in the decision-making process regarding Maker selection.
Request Maker Symbol Status Report
To request a Maker Symbol Status Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, if Maker and Symbol are left empty, this implies that all values are included in the selection
Display Maker Symbol Status Report
After generating the Maker Symbol Status, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval
Maker Select one or multiple Makers from the list of Makers configured in the Centroid Bridge
Symbol Select one or multiple Symbols from the list of Symbols available in the Centroid Bridge
Field Description

Maker The name of the Maker
Symbol The name of the Symbol
Sub ID The Symbol’s market data subscription ID that is sent to the Maker upon subscription
Time The timestamp indicating when the snapshot was captured and the record was generated.
Subscribed Specifies whether we are currently subscribed to the Symbol with the Maker.
If YES, it signifies that we are subscribed to the Symbol.
If NO, it indicates that we are not subscribed to the Symbol.
Ticks Count The count of ticks or price updates received for the Symbol within the 5-minute time interval.
Avg Spread The average spread of the Symbol, represented in decimal format.
Avg Spread in
Points
The average spread of the Symbol, expressed in points.
Spread Ticks
Count
The count of ticks or price updates received for the Symbol, which served as the basis for calculating the average
spread during the current time interval.
Delayed Ticks
Count
The count of ticks or price updates that experienced delays.
Orders Count The total count of orders executed with the Maker during the specified time interval, regardless of the order size.
Each executed order is treated as a single occurrence, irrespective of the volume involved.
Long Orders The overall count of Long Orders executed with the Maker during the specified time interval, regardless of the
order size. Each executed Long Order is considered as one occurrence, irrespective of the volume involved.
Short Orders The total count of Short Orders executed with the Maker during the specified time interval, regardless of the order
size. Each executed Short Order is considered as one occurrence, regardless of the volume involved.
Avg Fill Time The average fill time, measured in microseconds, for all orders executed during the current time interval.
Avg Travel Time The average travel time, measured in microseconds, for an order to journey from the Centroid Bridge to the Maker.
Rejected Count The count of rejected orders.
Partial Fills
Count
The count of orders that experienced partial fills.
Fully Fills Count The count of orders that were completely filled.
Total Till Volume The aggregate notional volume executed with the Maker within the 5-minute time interval.
Field Description

To Export the Maker Symbol Status Report
Click on “Export to CSV” or “Export to Excel” to export the report

Average
Slippage
The average slippage, expressed in decimals, for all executed orders.
Average
Slippage Points
The average slippage, measured in points, for all executed orders.


