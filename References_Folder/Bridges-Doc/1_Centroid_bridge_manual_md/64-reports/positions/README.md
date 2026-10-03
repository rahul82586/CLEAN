[🏠 Document Start](..\..\README.md) / [Reports](..\README.md) / Positions

# Positions

Overview
The Positions report offers an up-to-the-minute summary of the aggregate open positions within one or more Risk Accounts, Taker
Execution Models, or a combination thereof. The report presents positions on a per-Account and per-Symbol basis.
This report allows Brokers to effortlessly monitor all net open positions and employ filtering options to examine those associated with a
specific Risk Account or Taker Execution Model.
Request a Position Report
To request a Position Report:
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Click on the "Search" button to execute the report.
Note: Use the Reset button to clear the pre-defined filters
Note: If the above fields are left empty, all values pertaining to the above fields will be included in the search
Display Position Report
After generating the Position Report, you can perform the following actions
The Positions Report is displayed on a per Risk Account/Taker Execution Model and Symbol basis.
Symbol Select one or multiple Symbols
Taker Select one of multiple Takers
Type The Type of Account
Taker Execution Model: To check the Open Positions of one or multiple Taker Execution Models and/or Makers
Risk Account: To Check the Open Positions of a Risk Account which may contain one or multiple Taker/Taker
Execution Models
All Models: A combination of both Risk Accounts and Taker Execution Models and/or Makers
Taker
Execution
Model
Select one or multiple Risk Accounts, Taker Execution Models, Makers or a combination of all, depending on the Type
selected in the previous field
Field Description

Within the Position Report, you have the capability to:
1. Click the "Columns" button to add and display additional columns related to Positions, which are initially hidden.
2. Apply various arithmetic and logical conditions to filter columns.
3. Export the Maker Positions Report to identify any disparities between actual Trades and Net Positions on the Maker's side, potentially
resulting from a Centroid Bridge crash or unplanned restart.
4. Verify discrepancies between Trades and Net Open Positions on the Maker's side.
5. Export the Taker Positions Report to examine any inconsistencies between actual Trades and Net Positions on the Taker's side,
possibly stemming from a Centroid Bridge crash or unplanned restart.
6. Verify discrepancies between Trades and Net Open Positions on the Taker's side.
7. Export the list of Open Positions to an Excel or CSV file.
8. Click the arrow button to view the list of Orders comprising the Positions. This feature is relevant to Risk Accounts only.
9. Click the "Refresh" or the right arrow button to update the Positions and access real-time information.
Pos ID The ID number of the Position
Symbol The Symbol that has the open position
Taker
Execution
Model
The Taker Execution Model that has the open position.
Note: All B Book orders that were not processed by any Makers will display B_BOOK in this column
Taker The Taker under which the Taker Execution Model is set up.
Field Description

Risk
Account
The name of the Risk Account that holds the open position
Note: This column would appear only if requested Type is Risk Account. If Type is Taker Execution Model or All Models,
this column would display an empty value
Account
Type
The type of Account that holds the open position
Client: If position belongs to a client, Taker/Risk Account
Provider: If the position belongs to a Maker or B Book
Liquidity
Model
The Liquidity Model assigned to the Trading Account which specifies the Maker(s) the open position is held with
Net Volume The Net Open Positions in notional value.
Short Symbols show a negative value and are highlighted in Red
Long Symbols show a positive value and are highlighted in Blue
ANet
Volume
The Net Open Positions of all STP trades in notional value
BNet
Volume
The Net Open Positions of all B Book trades in notional value
Avg Price The Weighted Average Price of all deals that form the position
AAvg Price The Weighted Average Price of STP Position
BAvg Price The Weighted Average Price of B Book Position
Last Time The Last Time the real-time data of the Position were updated
Close Price The current Market Price
PL The current floating (unrealized) P/L which is the difference between Close Price and Avg Price multiplied by Net
Volume
Margin The current Blocked Margin of the Position
Swaps This is relevant to Position pertaining to a Risk Account and shows accumulated Swap charges that have been charged
on Open Positions
Commission

This is relevant to Position pertaining to a Risk Account and shows commission charges that have been charged on
Open Positions
Base
Exposure
The Notional Volume in Base Currency
Quote
Exposure
The Notional Volume in Quote Currency
Base Cur
Exposure
This Base Volume converted into Risk Account Currency
Note: For Positions that do not correspond to a Risk Account, it will show exactly the same value as Base Exposure
Quote Cur
Exposure
The Quote Volume converted into Risk Account Currency
Note: For Positions that do not correspond to a Risk Account, it will show exactly the same value as Quote Exposure
BBase
Exposure
The Notional Volume in Base Currency of the B Book Positions

As indicated in the preceding step, you have the option to expand the Position further to inspect the various Orders beneath that constitute
the Position.
BQuote
Exposure
The Notional Volume in Quote Currency of the B Book Positions
BBase Cur
Exposure
This Base Volume of the B Book Positions converted into Risk Account Currency
Note: For Positions that do not correspond to a Risk Account, it will show exactly the same value as BBase Exposure
BQuote Cur
Exposure
The Quote Volume of the B Book Positions converted into Risk Account Currency
Note: For Positions that do not correspond to a Risk Account, it will show exactly the same value as BQuote Exposure
Markup The Markup in decimal, if any, that was applied to the Open Positions
Margin
Conv Rate
The Margin Conversion rate from Base Currency into USD
PL Conv
Rate
The Profit Conversion rate from Quote currency into USD
Actions Allows to check the Orders that make up the Position, in the event of having an aggregated position, and perform
closing actions and adjustments for accounting purposes
Note: This is only relevant to Positions pertaining to Risk Accounts
Seq ID A sequential ID number of the Order
Cen Ord ID The Centroid Bridge Order ID of the Order
Price The Price at which the Order was opened
Volume The Notional Volume in Base Currency of the Order. The Volume decreases when another Order of opposite side is
placed using the FIFO mode
Time The Date and Time at which the Order was opened
Actions Allows to close an Order to decrease the overall Position. This does not send the Order to processing. It merely closes
it on the Centroid Bridge for Accounting purposes
Field Description

Position Upload
The functionality to upload positions is provided for Risk Account and the Taker Execution Model (TEM).
Risk Account:
The Risk Account Position Upload feature can be utilized when you want to increase or decrease the exposure or volume.
TEM:
The TEM Position Upload feature can be utilized to replace the existing values with new ones.
For more detailed information, please refer to the following pages within the Positions section:
Exporting the Positions Report
To Export the Position Report
Click on “Export to CSV” or “Export to Excel” to export the report





