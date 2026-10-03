[🏠 Document Start](..\README.md) / [Symbol Notional](README.md) / Markup Report

# Markup Report

Overview
The Markup Report functions as a pivotal tool for profitability analysis, granting brokers the ability to discern the financial impact of
markups on a per-order basis. By offering detailed insights into the relationship between markups and financial performance, this report
enables brokers to precisely evaluate how markups influence the profitability of each individual order.
Request Markup Report
To request a Markup Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty, apart from dates, implies that all values are included in the search
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
Field Description

After generating the Markup Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
TEM Taker Execution Model(s) through which the Order was executed
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
Recv Time The Time at which the Oder was received and processed in the Centroid Bridge
Taker The Taker that initiated the Order
TEM The Trading Execution Model within the Taker from where the Order was placed
Symbol The traded Symbol
Field Description

To Export the Markup Report
Click on “Export to CSV” or “Export to Excel” to export the report

Side The side of the Order; Buy or Sell
Fill Volume The filled Volume of the Order
Notional The Notional Volume in USD
Fill Price
Broker
The raw Fill Price of the Broker with the Maker (or B Book) excluding any markup
Fill Price
Client
The Fill Price reported back to Client which includes the markup, if any, defined in Markup Model
Markup The Markup in decimal which is the difference between Broker Fill Price and Client Fill Price
Markup
USD
The Markup converted into USD representing the Broker’s profitability on the Order
Markup WL
(%)
WL Markup in USD as per the defined WL Bid % and WL Ask %, if any, in Markup Model


