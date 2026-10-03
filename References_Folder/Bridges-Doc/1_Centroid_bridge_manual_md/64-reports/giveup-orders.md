[🏠 Document Start](..\README.md) / [Maker Orders](README.md) / Giveup Orders

# Giveup Orders

Overview
The Giveup Orders Report offers a summary of all giveup orders recorded on MT4 or MT5 giveup accounts specified in the Giveup Rule
module.
Request Giveup Orders Report
To request a Giveup Orders Report
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
Ext Order ID MT4/MT5 Ticket Number for Takers of type MT4/MT5
Cen Ord Id Centroid Order ID
Symbol Select one or multiple Symbols from the list of Symbols
Taker The Taker(s) configured in the Centroid Bridge such as FIX, MT4, MT5 and Centroid’s Trading Platform
TEM Taker Execution Model(s) through which the Order was executed
Grid
Columns
Columns or data fields that will be available in the report
Field Description

After generating the Giveup Orders Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Risk Account Risk Account through which the Order was executed, if any
Client Ord ID Client Order ID received in the Centroid Bridge of the Giveup Order
Cen Ord ID Centroid unique Order ID recorded in the Centroid Bridge of the Giveup Order
Ext Client
Login
Login number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise, value will
be 0
Ext Client
Group
Group name of the MT4/MT5 Login from which the order was generated, if the order is originated from a Taker of type
MT4 or MT5. Otherwise, the field will display an empty value
Ext Order ID Ticket Number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise, value will
be 0
Send Time The Time at which the Oder was sent to the Maker
Maker The Maker that processed the Order
If Order is STP, the name of the Maker would be displayed as configured in Maker Sessions
If Order is B Book, B_BOOK will be displayed
TEM The Taker Execution Model through which the Order was processed
Symbol The traded Symbol
Liquidity
Model
The Liquidity Model used for execution
Side The side of the Order; Buy or Sell
Ord Type The type of the Order; Market, Limit or Stop
Volume The requested Volume of the Order
Fill Volume

The actual filled Volume of the Order.
Fully Filled Orders have Full Volume equal to Volume
Partially Filled Order have Fill Volume less than Volume
Rejected Orders have 0 Volume as no Volume was executed
Notional The Notional Volume of the filled order in USD
Avg Price The Weighted Average Price in case the Order was split into multiple legs
Field Description

Exporting the Giveup Order Report
To Export the Giveup Order Report
Click on “Export to CSV” or “Export to Excel” to export the report

Slippage The Slippage in decimal value which results due to price difference between request price and filled price. Slippage is
the difference between the fill price and the requested price
State The State of the Order:
Filled: Indicates a full fill of the Order
Partial: Indicates a partial fill of the Order
Rejected: Indicates an Order rejection


