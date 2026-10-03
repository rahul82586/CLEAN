[🏠 Document Start](..\README.md) / [Maker Rejection](README.md) / Slippage Report

# Slippage Report

Overview
The Slippage Report facilitates the identification of slippage on orders, arising from the variance between the requested price and the
actual filled price on an individual order basis. Slippage may favor the client when positive (indicating a better fill) or favor the broker when
negative (indicating a worse fill).
Request Slippage Report
Request Slippage Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty, except for Start and End Dates, implies that all values are included in the selection
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
Taker The Taker(s) configured in the Centroid Bridge such as FIX, MT4, MT5 and Centroid’s Trading Platform
Risk
Account
Risk Account through which the Order was executed, if any
Field Description

After generating the Slippage Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Primary Details
Limit Order Slippage
Grid
Columns
Columns or data fields that will be available in the report
Note: To determine the reason and comments for rejections, ensure you include both filters when running the report.
Client Ord ID Client Order ID received in the Centroid Bridge
Cen Ord ID Centroid unique Order ID recorded in the Centroid Bridge
Recv Time The timestamp indicating when the Order was received and processed in the Centroid Bridge.
Taker The Taker that initiated the Order
TEM The trading execution model within the Taker from which the Order originated.
Symbol The Symbol that was traded.
Taker Symbol The Symbol that was traded on the Taker's end.
Side The direction of the Order: Buy or Sell.
Ord Type The classification of the Order: Market, Limit, Stop, etc.
Fill Volume The volume that has been filled for the Order.
Notional The notional volume of the Order, expressed in USD.
Avg Price The VWAP (Volume Weighted Average Price) fill price communicated to the client after the Order has been
successfully filled.
Field Description

Order Slippage Broker
Client Order Slippage Ext
Exporting the Slippage Report
To Export the Slippage Report
Click on “Export to CSV” or “Export to Excel” to export the report
Expected
Price
The specified price sent with the Limit Order.
Fill Price The actual fill price achieved by the broker, which is either equal to or better than the expected price.
Slippage The slippage, expressed in decimal format, is the difference between the requested price and the actual fill price. It is
either 0 or a positive number.
Slippage
USD
The slippage, converted into USD, is either 0 or a positive value since there is no worse fill in the case of a Limit Order.
Field Description
Expected
Price
The price at which the Centroid Bridge processed the Order request.
Fill Price The actual price at which the broker's Order is filled.
Slippage The slippage, in decimal form, represents the difference between the requested price and the actual fill price.
Slippage
USD
The slippage, when converted into USD
Positive slippage indicates the Order was filled at a better price.
Negative slippage indicates the Order was filled at a worse price.
A slippage of 0 means the Order was filled without any slippage.
Field Description
Expected
Price
The request price from a client's perspective is equivalent to the available price on the client's platforms at the time the
Order was placed. This encompasses all markups, including those from Centroid and MT4/MT5.
Fill Price The actual fill price reported back to the client includes all markups, such as those from Centroid and MT4/MT5.
Slippage The slippage, expressed in decimal form for the client, is the difference between the client's requested price and the
actual fill price.
Slippage
USD
The slippage, when converted into USD, is interpreted as follows:
Positive slippage indicates the Order was filled at a better price.
Negative slippage indicates the Order was filled at a worse price.
A slippage of 0 means the Order was filled without any slippage.
Field Description




