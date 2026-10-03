[🏠 Document Start](..\README.md) / [TEM Position Upload](README.md) / Orders

# Orders

Overview
The Orders Report offers a summary of an order blotter, presenting a comprehensive view of all individual orders placed through the
Centroid Bridge, originating from various Takers like: MT4, MT5, FIX, and others.
Much like the Trading section, the Orders Report features two distinct views: Broker and Trader.
You have visibility over all Orders originating from different Takers connected to the Centroid Bridge. Brokers can search and retrieve
Orders using different search and filtration criteria.
Request Order Report
To request an Order Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty implies that all values are included in the search
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval.
Ext Client
Group
Name of MT4/MT5 Group for Takers of type MT4/MT5
Ext Client
Login
MT4/MT5 Login number for Takers of type MT4/MT5
Ext Order
ID
MT4/MT5 Ticket Number for Takers of type MT4/MT5
Cen Ord Id Centroid Order ID
Symbol Select one or multiple Symbols from the list of Symbols available in the Centroid Bridge
TEM Taker Execution Model(s) through which the Order was executed
Field Description

Display Order Report
After generating the Orders Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Taker The Taker(s) configured in the Centroid Bridge such as FIX, MT4, MT5 and Centroid’s Trading Platform
Risk
Account
Risk Account through which the Order was executed, if any
Grid
Columns
Columns or data fields that will be available in the report
Note: To determine the reason and comments for rejections, ensure you include both filters when running the report.
Client Ord
ID
Client Order ID received in the Centroid Bridge
Cen Ord ID Centroid unique Order ID recorded in the Centroid Bridge
Ext Client
Login
Login number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise, value will be
0
Ext Client
Group
Name of the MT4/MT5 Group from which the order was generated, if the order is originated from a Taker of type MT4 or
MT5. Otherwise, the field will show an empty value
Ext Order
ID
Ticket number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise, value will be
0
Recv Time The Time at which the Order was received and processed in the Centroid Bridge
Taker The Taker that initiated the Order
Taker
Execution
Model
The Trading Execution Model used for executing the order
Symbol The universal symbol in the bridge
Field Description

Exporting the Order Report
To Export the Order Report
Click on “Export to CSV” or “Export to Excel” to export the report
Taker
Symbol
The traded Symbol on Taker’s end
Liquidity
Model
The Liquidity Model used for execution
Side The side of the Order; Buy or Sell
Ord Type The type of the Order; Market, Limit or Stop
Volume The requested Volume of the Order
Price Requested or Desired Price, in case of Limit or Stop Orders.
For Market Orders, it will be 0 as the Order is executed at the Market Price
Fill Volume The actual filled Volume of the Order.
Fully Filled Orders have Full Volume equal to Volume
Partially Filled Orders have Fill Volume less than Volume
Rejected Orders have 0 Volume as no Volume was executed
Notional
Volume
The Notional Volume of the filled order in USD
Avg Price The Weighted Average Price in case the Order was split into multiple legs
Fill State

The State of the Order:
Filled: Indicates a full fill of the Order
Partial: Indicates a partial fill of the Order
Rejected: Indicates an Order rejection
Slippage The Slippage in decimal value which results due to price difference between request price and filled price. Slippage is
the difference between the fill price and the requested price
Ext
Markup
This is relevant to MT4/MT5 Takers and consists of the Markup at the level of MT4/MT5 group in decimal points
B% The B Book percentage of the Order
A Vol The requested A Book volume
B Vol The requested B Book volume
A Fill The filled A Book Volume
B Fill The filled B Book Volume
Sender The Taker through which the Order was initiated
Exec Time
(ms.mic)
Order Execution Time in milliseconds and microseconds




