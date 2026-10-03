[🏠 Document Start](..\README.md) / [Legs](README.md) / Detailed Leg Report

# Detailed Leg Report

Overview
A Detailed Leg Report provides a brief analysis of slippage at the Maker, Broker, and Client levels, along with profitability (resulting from
markups) on a per-leg basis.
Request Detailed Leg Report
To request a Detailed Leg Report
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
MT4 Group number for Takers of type MT4/MT5
Ext Client
Login
MT4 Login number for Takers of type MT4/MT5
Ext Order
ID
MT4 Ticket Number for Takers of type MT4/MT5
Cen Ord Id Centroid Order ID
Symbol Select one or multiple Symbols from the list of Symbols
Taker The Taker(s) configured in the Centroid Bridge such as FIX, MT4, MT5 and Centroid’s Trading Platform
TEM Taker Execution Model(s) through which the Order was executed
Risk
Account
Risk Account through which the Order was executed, if any
Field Description

The Detailed Leg Report is divided into two sections, Leg Details and Order Details. When Order is split into multiple Legs, different Legs
will be shown on one side whereas on the other side the same Order will be shown multiple times depending on the number of Legs it was
split into.
Once the Detailed Leg Report has been generated, you can do the following:
1. Sort columns by ascending or descending order
2. Filter columns using a variety of arithmetic and logical conditions
3. Navigate through pages by accessing first, last, previous and next pages
4. Fit the entire report into the page
5. Auto size columns based on the column data
Leg Details
Order Details
Maker Select one or multiple Makers from the list.
For B Book Orders, they will be under B_BOOK Maker
Grid
Columns
Columns or data fields that will be available in the report
Cen Client
OrdId
The ID of the Leg. For instance, an Order split into three legs will have Leg IDs of 0, 1 and 2
Maker The Maker Leg got executed with or that provided the quote for B Book Orders
Send Time The Time at which the Leg was sent to the Maker
Fill Volume The filled Volume of the Leg
Notional The Notional Volume of the Leg in USD
Maker
Symbol
The Symbol name on Maker’s side
Maker
OrderID
The assigned ID of the Order returned by the Maker
Field Description
Client Ord
Id
Client Order ID received in the Centroid Bridge
Cen Ord Id Centroid unique Order ID recorded in the Centroid Bridge
Recv Time The Time at which the Oder was received and processed in the Centroid Bridge
Taker The Taker that initiated the Order
TEM The Trading Execution Model within the Taker from where the Order was placed
Symbol The traded Symbol
Field Description

Ord Type The type of the Order; Market, Limit or Stop
Side The side of the Order; Buy or Sell
Fill Volume The filled Volume of the Order
Avg Price The VWAP Fill Price reported back to Client after the Order has been filled

