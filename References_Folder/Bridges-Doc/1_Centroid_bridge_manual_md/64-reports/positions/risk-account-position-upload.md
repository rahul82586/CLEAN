[🏠 Document Start](..\..\README.md) / [Reports](..\README.md) / [Positions](README.md) / Risk Account Position Upload

# Risk Account Position Upload

Overview
In this module, you will learn how to upload positions using the Upload Feature for Risk Accounts. Also when uploading positions, it is
strongly recommended to use the correct template to prevent errors.
Guide to Uploading Positions in Risk Accounts
1. Select the Risk Account Template from the drop-down list.
2. Click the Download icon to obtain the template.
3. Complete the Excel file using the field descriptions below.
4. Upload the completed file to the Bridge.
Symbol EURUSD The name of the Symbol as defined under Symbols
Taker Symbol EURUSD.a
ma
The name of Taker Symbol which is allocated for the particular Taker
Taker Execution
Model
TEM-1 The name of the Taker Execution Model where the exposure needs to be adjusted & is linked to
the specific Risk Account
Taker Centroid_M
T5
The name of the Taker for which the exposure needs to be adjusted & is linked to the specific Risk
Account
Taker Feed Test_Feed The name of the Taker Feed linked to this Risk Account
Risk Account The name of the Risk Account for which the exposure needs to be adjusted
Liquidity Model Liquidity_M
odel
The Liquidity Model linked to the Execution Model
Net Volume 10,000 The Net Open Positions must be the sum of ANet and BNet Volumes
ANet Volume 5,000 The volumes to be adjusted (added/deducted) for the A Book Positions.
BNet Volume 5,000 The volumes to be adjusted (added/deducted) for the B Book Positions.
Field Possible
Values
Description

Notes:
To increase exposure or volume: Enter the amount to be Added in the Excel sheet.
To decrease exposure or volume: Enter the amount to be Deducted using a negative value.
Avg Price 1.08644 The Weighted Average Price of all deals that form the position
AAvg Price 1.08114 The Weighted Average Price of A Book Position
BAvg Price 1.08644 The Weighted Average Price of B Book Position
Close Price 1.07094 The expected close price for this position.
Note: The close price will be overridden by the current market price. This field will be useful during
market close hours to provide an estimated P&L.
Please exercise caution, as changes made after the upload cannot be undone.

