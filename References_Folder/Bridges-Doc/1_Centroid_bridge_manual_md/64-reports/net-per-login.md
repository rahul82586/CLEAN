[🏠 Document Start](..\README.md) / [Slippage Leg Report](README.md) / Net Per Login

# Net Per Login

Overview
The Per Net Login Report provides a detailed summary of the overall Net Open Positions, encompassing both A-Book and B-Book Net
Open Positions. This report aggregates the Net Open Positions on a per Symbol basis, delivering valuable insights into trading activities
for enhanced analysis and understanding.
When searching for Takers like MT4 and MT5, the report also furnishes external information in the form of Client Login details. This
additional feature enhances the comprehensiveness of the report by including pertinent data related to client logins associated with
platforms such as MT4 and MT5.
Request Net Per Login Report
To request a Net Per Login Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty implies that all values are included in the selection
Display Net Per Login Report
After generating the Net Per Login Report, you can perform the following actions
Ext Client
Login
The Login number of the MT4/MT5 Account. You may enter multiple comma separated Logins
Party
Symbol
Party Symbol is the Symbol name on the Taker’s side, as set up in the Taker Feeds.
You may select one or multiple Party Symbols from the list
Symbol Select one or multiple Symbols from the list of Symbols available in the Centroid Bridge
Hide Zero
Net
Choose whether to display the Logins with no Open Positions or not.
If ticked, the generated report will hide all rows with zero net open positions
If un-ticked, the generated report will still display the rows showing logins with zero net open positions
Field Description

1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
Ext Client
Login
Login number of the MT4/MT5 Taker
Party
Symbol
The Symbol name on the Taker’s side
Ext Client
Login
The Symbol name as configured in Symbols
Net The Total Net Open Position in Notional Volume denominated in the Base Currency consolidates both buy and sell
positions, effectively offsetting each other. It's important to note that a negative value signifies a short net open position
(sell), whereas a positive value indicates a long net open position (buy).
Net Buy The Buy Net Open Position signifies the combined Notional Volume in the Base Currency for all buy positions. This
metric is specifically designed to highlight the volume of open positions where clients have adopted a long (buy)
position in the market. It provides a targeted insight into the overall volume associated with clients taking a bullish
stance.
Net Sell The Sell Net Open Position relates to the total Notional Volume in the Base Currency attributed to all sell positions. This
metric exclusively portrays the volume of open positions wherein clients have assumed a short (sell) position in the
market. It offers a focused perspective on the overall volume associated with clients adopting a bearish stance.
ANet The Comprehensive Net Open Position of A-Book Orders, denominated in Notional Volume in the Base Currency,
amalgamates both buy and sell A-Book positions, efficiently balancing each other out. It's crucial to recognize that a
negative value indicates a short net open position (sell), while a positive value signifies a long net open position (buy).
This metric offers an all-encompassing perspective on the overall A-Book exposure, presenting insights into volume
and directional bias.
ANet Buy The Buy Net Open Position for A-Book Orders, measured in Notional Volume in the Base Currency, represents the
aggregated volume of all buy positions within the A-Book. This metric specifically focuses on the cumulative volume
associated with clients taking a long (buy) position in the market within the A-Book segment.
ANet Sell The Sell Net Open Position for A-Book Orders, quantified in Notional Volume in the Base Currency, signifies the
combined volume of all sell positions within the A-Book. This metric exclusively reflects the aggregated volume of open
positions where clients have opted for a short (sell) stance in the market within the A-Book segment.
BNet The Total Net Open Position of B-Book Orders, expressed in Notional Volume in the Base Currency, consolidates both
buy and sell B-Book positions, effectively offsetting each other. It's important to note that a negative value signifies a
Field Description

To Export the Net Per Login Report
Click on “Export to CSV” or “Export to Excel” to export the report


short net open position (sell), while a positive value indicates a long net open position (buy). This metric provides a
comprehensive overview of the overall B-Book exposure in terms of volume and directional bias.
BNet Buy The Buy Net Open Position for A-Book Orders, measured in Notional Volume in the Base Currency, represents the
cumulative volume of all buy positions within the A-Book. This metric specifically focuses on the combined volume
associated with clients taking a long (buy) position in the market within the A-Book segment.
BNet Sell The Sell Net Open Position for B-Book Orders, quantified in Notional Volume in the Base Currency, signifies the
aggregated volume of all sell positions within the B-Book. This metric exclusively reflects the combined volume of open
positions where clients have chosen a short (sell) stance in the market within the B-Book segment.


