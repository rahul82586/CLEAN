[🏠 Document Start](..\README.md) / [Trading](README.md) / Market Watch

# Market Watch

Overview
The Market Watch allows Brokers to view prices coming through the different Taker Feeds defined in the Centroid Bridge including the full
depth of the market. This also allows Brokers to test price connectivity with Makers and the Taker Feed when a new Maker is added or
upon adding a new instrument with a Maker.
Within this module, you have the capability to:
Add or Remove Symbol from List: Include or exclude symbols from the list.
View Prices with Full Market Depth: Observe prices in panels with extensive market depth and adjustable based on Taker Feed and
Maker level.
View Prices as List with TOB: Explore prices presented as a list with the Top of Book (TOB) highlighted.
Adding a Symbol to the List
To add a Symbol to the Market Watch list
1. Click the dropdown button “Toggle here to add/remove Symbol”.
2. Fill it in with the relevant information. You may refer to the field descriptions hereafter.
3. Click the “Add / Remove Symbol” button to submit the changes.
Deleting a Symbol from the List
To delete a Symbol from the list
1. Click the dropdown button “Toggle here to add/remove Symbol”.
Taker
Feed
Select a Taker Feed from the list of available Taker Feeds. You can also add multiple Taker Feeds.
Symbol Select one or multiple Symbols pertaining to the selected Taker Feed for which you want to see the price.
Field Description

2. In the Symbol textfield, search and choose your desired Symbol. Once you hover your mouse to the selected symbol, you may click the
“x” button next to it if you wish to remove it from the list. Alternatively, you can simplify the deletion by clicking the “x” button on the top
right side of the panel.
3. Click the “Add / Remove Symbol” button to submit the changes.
Panel View
In the panel, you can view the price of each Symbol separately. Selected Symbols will appear in a separate panel on which all the pricing-
related information is shown.
Symbol name with configured suffix from Taker Feed
Bid and Ask indicator with green upward arrow for an increase and red downward arrow for a decrease
TOB quantity or available liquidity on the Bid and Ask side
TOB Bid price and TOB Ask price
Spread at TOB in decimals (e.g., 000002 for a 2 pip spread)
Time of the last received price
Full depth of available liquidity sizes on the Bid and Ask side (below TOB)
Full depth of available liquidity prices on the Bid and Ask side (below TOB)


List View
In the panel, you can view the TOB price of each Symbol along with other relevant information.
FAQ
What could be the reason why a particular symbol is not pricing on the Taker Feed level?
Symbol The selected Taker Feed Symbol(s).
Bid Price The Bid Price at the top of the book (TOB).
Ask Price The Ask Price at the top of the book (TOB).
Spread The Spread at the top of the book (TOB) expressed in decimal form. For instance, a spread of 0.00005 on a 5-digit
EURUSD symbol corresponds to 0.5 pips and 5 points.
Spread
Points
The spread at the top of the book (TOB) expressed in points. For instance, a spread points of 2 corresponds to
0.00002 on a 5-digit EURUSD symbol.
Bid Volume The Bid liquidity currently available at the top of the book (TOB).
Ask Volume The Ask liquidity currently available at the top of the book (TOB).
Bid Maker The Maker streaming the Bid liquidity.
Ask Maker The Maker streaming the Ask liquidity.
Last
Updated
The timestamp indicating when the price was last updated.
LTP Price The Last Traded Price.
LTP Volume The Last Traded Price Volume.
Field Description
To troubleshoot, follow these steps:
1. Ensure the Taker Feed is enabled.
2. Check if you have assigned a working Liquidity Model.
3. Check if the assigned Maker is sending prices for that particular Symbol to the Centroid Bridge. You can check this by navigating to
Monitoring -> Maker Status, as detailed in the manual.

