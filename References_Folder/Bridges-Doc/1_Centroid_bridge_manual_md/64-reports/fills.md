[🏠 Document Start](..\README.md) / [Detailed Leg Report](README.md) / Fills

# Fills

Overview
The Fills Report presents a detailed overview into each Legs in terms of how the Order got executed along with the relevant execution
details. The relationship between Order and Leg is one to many as a single Order can be split into multiple Legs in the event in filling the
Order in more than one attempt. The report is split into Leg Details and Order Details which relevant fields for each.
Request Fill Report
To request a Fill Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty, apart from dates, implies that all values are included in the search
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval
Ext Client
Group
MT4/MT5 Group number for Takers of type MT4/MT5
Ext Client
Login
MT4/MT5 Login number for Takers of type MT4/MT5
Ext Order
ID
MT4/MT5 Ticket Number for Takers of type MT4/MT5
Cen Ord Id Centroid Order ID
Symbol Select one or multiple Symbols from the list of Symbols
TEM Taker Execution Model(s) through which the Order was executed
Taker The Taker(s) configured in the Centroid Bridge such as FIX, MT4, MT5 and Centroid’s Trading Platform
Field Description

Display Fill Report
After generating the Fills Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Leg Details
Risk
Account
Risk Account through which the Order was executed, if any
Maker Select one or multiple Makers you wish to check Orders with
Maker B This is relevant to B Book Orders only where you can check the Makers who provided the quote at the time the B Book
Order was executed
Grid
Columns
Columns or data fields that will be available in the report
Cen Client
OrdId
The ID of the Leg. For instance, an Order split into three legs will have Leg IDs of 0, 1 and 2
Maker The name of the Maker the Leg got it executed with
If A Book: The name of the LP that processed the Order will be displayed as configured in the bridge
If B Book: B_BOOK will be displayed
Maker B This is relevant to B Book Orders only and discloses the Maker that provided the quote at the time the B Book Order
was executed
Time The Date and Time at which the Leg was executed
Side The side of the Order; Buy or Sell
Volume The requested Leg Volume
Fill Volume The actual filled Leg Volume which could be equal or less than the requested Volume above
Notional The Notional Volume of the filled Leg in USD
Field Description

Order Details
Maker Symbol The name of the Symbol on the Maker’s side
Maker
OrderID
The assigned ID of the Order returned by the Maker
Maker Cat The Maker Category or Type
Maker ExecID The Execution ID of the Leg assigned by the Maker
Fill Price The fill Price the Leg got executed at including Markup
Markup Defined Markup in decimal on top of the Price, if any
Raw Fill Price The fill Price the Leg got executed at excluding Markup
Exec Time
(ms.mic)
Order Execution Time in milliseconds and microseconds
Client Ord ID Client Order ID received in the bridge
Cen Ord ID Centroid unique Order ID recorded in the bridge
Ext Client
Login
Login number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise, value will
be 0
Ext Client
Group
Group name of the MT4/MT5 Login from which the order was generated, if the order is originated from a Taker of
type MT4 or MT5. Otherwise, the field will display an empty value
Ext Order ID Ticket Number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise, value will
be 0
TEM The Taker Execution Model through which the Order was processed
Symbol The traded Symbol
Liquidity
Model
The Liquidity Model used for execution
Side The side of the Order; Buy or Sell
Ord Type The type of the Order; Market, Limit or Stop
Volume The requested Volume of the Order
Fill Volume

The effective filled Volume of the Order.
Fully Filled: Orders exhibit a Full Volume equivalent to the specified Volume.
Partially Filled: Orders have a Fill Volume that is less than the specified Volume.
Rejected: Orders show 0 Volume since no Volume was executed.
Notional The Notional Volume of the filled order in USD
Avg Price The Weighted Average Price in case the Order was split into multiple legs
Field Description

To Export the Fills Report
Click on “Export to CSV” or “Export to Excel” to export the report

Slippage The Slippage in decimal value which results due to price difference between request price and filled price. Slippage is
the difference between the fill price and the requested price
State

The status of the Order:
Filled: Denotes complete fulfillment of the Order
Partial: Denotes a partial fulfillment of the Order
Rejected: Denotes rejection of the Order


