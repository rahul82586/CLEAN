[🏠 Document Start](..\..\README.md) / [Positions](..\README.md) / [Positions](README.md) / TEM Position Upload

# TEM Position Upload

Overview
In this module, you will learn how to upload positions using the Upload Feature for Taker Execution Model. Also when uploading positions,
it is strongly recommended to use the correct template to prevent errors.
Guide to Uploading Positions in TEM
1. Select the Taker Execution Model Template from the drop-down list.
2. Click the Download icon to obtain the template.
3. Complete the Excel file using the field descriptions below.
Upload the completed file to the Bridge.
Symbol EURUSD The name of the Symbol as defined under Symbols
Taker Execution
Model
TEM-1 The name of the Taker Execution Model where the exposure needs to be adjusted
Taker Centroid_M
T5
The name of the Taker for which the exposure needs to be adjusted
Liquidity Model Liquidity_M
odel
The Liquidity Model linked to the Execution Model
Net Volume 10,000 The Net Open Positions must be the sum of ANet and BNet Volumes
ANet Volume 5000 The volumes to be adjusted (added/deducted) for the A Book Positions.
BNet Volume 5000 The volumes to be adjusted (added/deducted) for the B Book Positions.
Avg Price 1.08644 The Weighted Average Price of all deals that form the position
AAvg Price 1.08114 The Weighted Average Price of A Book Position
BAvg Price 1.08644 The Weighted Average Price of B Book Position
Field Possible
Values
Description

Notes:
The uploaded file will overwrite all existing values for the TEM

Close Price 1.07094 The expected close price for this position.
Note: The close price will be overridden by the current market price. This field will be useful during
market close hours to provide an estimated P&L.
Please exercise caution, as changes made after the upload cannot be undone.

