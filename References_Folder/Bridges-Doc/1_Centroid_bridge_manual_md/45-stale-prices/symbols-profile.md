[🏠 Document Start](..\README.md) / [Stale Prices](README.md) / Symbols Profile

# Symbols Profile

Overview
The Symbols Profile plays a crucial role in the Maker Failover Mechanism. Here, you can set up the symbol's preferences, guiding the
system in recognizing when a symbol’s price becomes outdated or stale. These preferences are unique for each symbol. There are two
timeout levels: a warning threshold and an error threshold. If either is reached, an alert is generated and recorded in the logs. Beyond
timeouts and alerts, you can also configure the system to automatically switch if a particular symbol is identified as not pricing.
Creating a Symbol Profile
To create a Symbol Profile
1. Click the “Symbol Profile” component.
2. Click the “Add” button to create a new Symbol Profile.
3. Fill out the wizard with all relevant information. You may refer to the field descriptions hereafter.
4. Click the “Submit” button to submit the changes.
Configuring Symbol Profile
To configure or modify a newly added Symbol Profile on a per symbol basis
Name StaleProfile1 This is intended to recognize the Symbol Profile and determine the particular Maker being
utilized in this Symbol Profile.
Description A short description for reference purposes only.
Field Possible Values Description

1. Configure the Symbol Profile by modifying the editable fields. All editable fields are represented by a “Pen” icon.
2. Click the “Save” button on the top left to apply the changes.
3. Click the “Revert All” button if you want to revert to the previous values.
Deleting Symbol Profile
To delete a Symbol Profile
1. Click the “Delete” button next to the desired Symbol Profile.
2. To confirm the Deletion, type in the specified text.
3. Click the “Delete” button in the pop-up window to confirm the deletion.
Symbol EURUSD,
XAUUSD
The Symbol to be tracked and to be applied with succeeding settings.
Symbols Profile StaleProfile1 Different Symbols Profiles can have distinct timeout setups, linked within the Stale Rules.
Warning Timeout
(sec)
5,10 Initial threshold tracking the time elapsed in seconds since the last update before issuing
warning alerts.
Error Timeout (sec) 10,15 Final threshold tracking the time elapsed in seconds since the last update before issuing
alerts and initiating failover mechanism.
Check LM other
makers
Enabled,
Disabled
During aggregation, this verifies other available makers in the Liquidity model before initiating
failover. If other makers in the same liquidity model are pricing, Switch To Failover is ignored.
Switch To Failover Enabled,
Disabled
Determines if the liquidity model(s) will shift from Primary to Failover. This collaborates with
Check LM other makers, enabled symbol profile, and an active stale rule.
Enable Enabled,
Disabled
Indicates whether the symbol profile is enabled or disabled.
Field Possible
Values
Description


Exporting a Symbol Profile
To Export a Symbol Profile
1. Select the desired Symbol Profile from the list.
2. Click “Export” and select “Export to Excel” or “Export to CSV”.



