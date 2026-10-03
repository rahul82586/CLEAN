[🏠 Document Start](..\README.md) / [Orders](README.md) / Maker Orders

# Maker Orders

Overview
The Maker Orders Report offers a comprehensive view of all STP Orders sent to the Maker(s), encompassing relevant execution details.
Additionally, it includes orders that have been internalized within the Centroid Bridge as “B Book”
Request Maker Report
To request a Maker Order Report
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
Risk
Account
Risk Account through which the Order was executed, if any
Field Description

Display Maker Report
After generating the Maker Orders Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Maker Order Details
Maker Select one or multiple Makers you wish to check Orders with
Grid
Columns
Columns or data fields that will be available in the report
Cen Client
Ord ID
The Leg ID of the Order which shows the Order and Leg number in the format OrderID_LegID
Maker The Maker responsible for processing the order:
If the order is STP, the displayed name of the Maker will be as configured in the Maker
If the order is B Book, "B_BOOK" will be displayed
Price The raw price advertised by the maker during the time of execution.
Avg Price The price after including the markup on top of the raw price.
Raw Avg
Price
The raw price at which the Maker filled the Order.
Volume The requested Volume of the Order
Fill Volume The actual filled Volume which could be equal or less than the requested Volume above
Notional The Notional Volume of the filled order in USD
Filled State The State of the Order:
Filled: Indicates a full fill of the Order
Partial: Indicates a partial fill of the Order
Rejected: Indicates an Order rejection
Field Description

Order Details
Exporting the Maker Order Report
To Export the Maker Order Report
Click on “Export to CSV” or “Export to Excel” to export the report


Client
Ord ID
Client Order ID received in the Bridge
Cen Ord
ID
Centroid unique Order ID recorded in the Bridge
Recv
Time
The time at which the Order was received in the Bridge
Taker The taker that initiated the Order
Symbol The traded Symbol
Side The side of the Order; Buy or Sell
Volume The requested Volume of the Order
Price Requested or Desired Price, in case of Limit or Stop Orders.
For Market Orders, it will be 0 as the Order is executed at the Market Price
Fill
Volume
The actual filled Volume of the Order.
Fully Filled Orders have Full Volume equal to Volume
Partially Filled Orders have Fill Volume less than Volume
Rejected Orders have 0 Volume as no Volume was executed
Avg Price The Weighted Average Price in case the Order was split into multiple legs
Filled
State
The State of the Order:
Filled: Indicates a full fill of the Order
Partial: Indicates a partial fill of the Order
Rejected: Indicates an Order rejection
Field Description


