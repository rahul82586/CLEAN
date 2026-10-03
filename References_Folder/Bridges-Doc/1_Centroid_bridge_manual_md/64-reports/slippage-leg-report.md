[🏠 Document Start](..\README.md) / [Slippage Report](README.md) / Slippage Leg Report

# Slippage Leg Report

Overview
The Slippage Report enables the assessment of slippage on orders, considering the variance between the requested price and the actual
filled price on a per Leg basis. Slippage can be advantageous for the client if positive, indicating a better fill, or disadvantageous if
negative, favoring the broker. Additionally, the Slippage Leg feature allows tracking of slippages the client experiences from the Maker on a
per Leg basis, particularly relevant when an order is executed in multiple Legs.
Request Slippage Leg Report
To request a Slippage Leg Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty, except for Start and End Dates, implies that all values are included in the selection
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval
Ext Client
Group
MT4 / MT5 Group number for Takers of type MT4/MT5
Ext Client
Login
MT4 / MT5 Login number for Takers of type MT4/MT5
Ext Order ID MT4 / MT5 Order ID Number for Takers of type MT4/MT5
Cen Ord Id Centroid Order ID
Symbol Select one or multiple Symbols from the list of Symbols
Taker The Taker(s) configured in the Centroid Bridge such as FIX, MT4, MT5 and Centroid’s Trading Platform
TEM Taker Execution Model through which the Order was executed
Risk Account Risk Account through which the Order was executed, if any
Field Description

After generating the Slippage Leg Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Leg Details
Maker Slippage Leg
Maker Select one or multiple Makers from the list.
For B Book Orders, they will be under B_BOOK Maker
Grid Columns Columns or data fields that will be available in the report
Cen Client
OrdId
The ID of the Leg. For instance, an Order split into three legs will have Leg IDs of 0, 1 and 2
Maker The Maker Leg that was either executed or provided the quote for B Book Orders.
Send Time The timestamp indicating when the Leg was transmitted to the Maker.
Fill Volume The volume that has been filled for the Leg.
Notional The notional volume of the Leg, expressed in USD.
Raw Fill Price The raw price at which the Leg was filled with the Maker, excluding all markups.
Fill Price The fill price of the Leg, which includes the Centroid Bridge markup.
Price The request price of the Leg, originating from the Centroid Bridge to the Maker.
Maker
Symbol
The symbol name on the Maker's side.
Field Description
Field Description

Order Details
Exporting the Slippage Leg Report
To Export the Slippage Leg Report
Click on “Export to CSV” or “Export to Excel” to export the report
Expected
Price
The requested price of the Leg.
Fill Price The actual fill price of the Leg.
Slippage The slippage, expressed in decimal form, is the difference between the requested price and the actual fill price for the
Leg.
Slippage
USD
The slippage, when converted into USD, reflects the monetary difference between the requested price and the actual
fill price for the Leg.
The slippage, when converted into USD
Positive slippage indicates the Order was filled at a better price.
Negative slippage indicates the Order was filled at a worse price.
A slippage of 0 means the Order was filled without any slippage.
Client Ord ID Client Order ID received in the Centroid Bridge
Cen Ord ID Centroid unique Order ID recorded in the Centroid Bridge
Recv Time The timestamp indicating when the Order was received and processed in the Centroid Bridge.
Taker The Taker responsible for initiating the Order.
TEM The trading execution model within the Taker from which the Order was placed.
Symbol The Symbol that was traded.
Taker Symbol The Symbol that was traded on the Taker's end.
Side The direction of the Order: Buy or Sell.
Fill Volume The volume that has been filled for the Order.
Notional The notional volume of the Order, expressed in USD.
Avg Price The VWAP (Volume Weighted Average Price) fill price reported back to the client after the Order has been filled.
Field Description




