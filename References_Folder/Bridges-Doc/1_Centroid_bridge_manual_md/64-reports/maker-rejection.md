[🏠 Document Start](..\README.md) / [Maker Symbol Spread History Chart](README.md) / Maker Rejection

# Maker Rejection

Overview
The Maker Rejection Report enables the examination of all orders that have been rejected by Makers on a per Leg basis. In instances of
Immediate or Cancel (IOC) execution, it is possible to have both accepted and rejected Legs within the same Order.
Request Maker Rejection Report
To request a Maker Rejection Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty, apart from dates, implies that all values are included in the search
Display Maker Rejection Report
Once the Maker Rejection Report has been generated, you can do the following:
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval
Symbol Select one or multiple Symbols from the list of Symbols
Maker The Maker that rejected/declined the Leg.
Field Description

To Export the Maker Rejection Report
Click on “Export to CSV” or “Export to Excel” to export the report
Cen Client
OrdId
The Leg ID of the Order which shows the Order and Leg number in the format OrderID_LegID
Note: An Order can be split into N Legs. The ID would look like Order_Leg1, Order_Leg2…LegN
Client Ord
Id
Client Order ID received in the Centroid Bridge
Cen Ord Id Centroid unique Order ID recorded in the Centroid Bridge which could be split into multiple Legs shown as different Cen
Client OrdId
Maker The Maker that rejected/declined the Leg
Symbol The Symbol that was traded in the rejected Order
Send Time The timestamp indicating when the rejected Order was transmitted to the Maker.
Maker
Recv Time
Sec
The timestamp indicating when the Order was received by the Maker.
Price The requested price of the Order.
Volume The requested volume of the Order.
Side The direction of the Order: Buy or Sell.
Ord Type The classification of the Order: Market, Limit, or Stop.
Time in
Force
The Fill Policy of the Order is defined as follows:
FOK: Fill or Kill, indicating that the Order can be fully filled in the requested volume.
IOC: Immediate or Cancel, indicating that the Order can be partially filled with the maximum available liquidity in the
market, and any remaining volume will be canceled.
Scale Size The Scale Size of the Order, as specified in the Maker Session Symbol Settings.
Field Description



