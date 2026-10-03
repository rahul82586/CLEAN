[🏠 Document Start](..\README.md) / [Maker API link](README.md) / Maker Scaling

# Maker Scaling

Overview
The Maker scaling acts as a multiplier for the Prices and Volumes provided by the Maker. This can be applied to both incoming (IN) and
outgoing (OUT) Prices, as well as Volumes.
It's crucial to emphasize that this scaling operates on a symbol basis at the Maker Level.
Within this module, you have the capability to:
Create a New Maker Scaling Rule: Initiate the setup for a new Maker Scaling Rule.
Filter Rules: Categorize Maker Scaling Rules based on various criteria for easier identification.
Enable/Disable Rule: Manage the active status of a Maker Scaling Rule.
Edit Rule: Modify an existing Maker Scaling Rule by adjusting configurable parameters.
Delete Rule: Remove an existing Maker Scaling Rule.
Export Rules: Save the list of Maker Scaling Rules to an Excel/CSV file.
Creating a Maker Scaling Rule
To create a Maker Scaling Rule:
1. Click on Maker Scaling and then click the “Add” button.
2. Fill out the Wizard. You may refer to the field descriptions below.
3. Click “Submit” to submit the changes.
Symbol No EURUSD Select the Symbol to be scaled up or down
Field Editabl
e
Possible
Values
Description

To configure or modify an existing Maker Scaling Rule
1. Select the desired Maker Scaling Rule.
2. Configure the desired fields.
3. Click the “Save” button on the top left to deploy the changes.
Deleting a Maker Scaling Rule
To delete a Maker Scaling rule
1. Click the “Delete” icon next to the desired Rule.
2. To confirm the Deletion, type in the confirmation text.
3. Click the “Delete” button in the pop-up window.
Note: Only one symbol can be selected per rule.
Maker No LP1 Select the Maker from the drop-down.
Note: Only one Maker can be selected per rule.
Price In Yes 0.1, 1, 10,
100
The Multiplier value to be applied on the incoming prices.
Example: An incoming price of 101.555 with scaling of 0.1, then the received price on bridge
will be 10.1555.
Price Out Yes 0.1, 1, 10,
100
The Multiplier value to be applied on the outgoing prices. This will only work for LIMIT orders
as for MARKET orders the price request is not being sent.
Example: A limit price of 101.555 with a price scale of 0.1 will be sent to the Maker as
10.1555.
Volume In Yes 1, 10,
100000
The Multiplier value to be applied on the incoming volumes.
Example: A volume of 10 with a scaled volume of 100000 will be processed by the bridge as
1000000.
Volume
Out
Yes 0.00001, 1,
10, 100
The Multiplier value to be applied on the outgoing volumes.
Example: A traded volume of 1000000 with a scaled volume of 0.00001 will be sent to the
Maker as 10.
Description Yes A short description for reference purposes.
Enable Yes Enabled,
Disabled
Indicates whether the Maker Scaling Rule is enabled or disabled.
If ticked, the Maker Scaling Rule is enabled.
If unticked, the Maker Scaling Rule is disabled.


To export a Maker Scaling rule
1. Filter the desired Maker Scaling from the list; otherwise, leave it unfiltered to select all
2. Click “Export” and select “Export to Excel” or “Export to CSV”
Uploading a Maker Scaling Rule
To upload multiple maker scaling rules via the exported file “Excel” or “CSV”
1. Click on the “Upload”.
2. Click on “Drop File”.
3. To upload the Liquidity Model values, click on “Upload”.


4. You also have the option to discard the bulk upload by clicking on the “Close” Button.



