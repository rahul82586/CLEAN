[🏠 Document Start](..\README.md) / [Symbols Profile](README.md) / Stale Rules

# Stale Rules

Overview
Stale rules are a crucial aspect of the Maker Failover Mechanism. They aid in determining the maker to monitor based on symbol profile
settings and specify the Liquidity Models for which the "Switch To Failover" is applicable when activated. Additionally, they allow users to
apply rules during specific sessions, enabling them to skip checks or failovers during anticipated periods when no prices are expected.
Creating a Stale Rule
To create a Stale Rule
1. Click the “Stale Rules” component.
2. Click the “Add” button to create a new Liquidity Model.
3. Fill out the wizard with all relevant information. You may refer to the field descriptions hereafter.
4. Click the “Submit” button to submit the changes.
Enable Enabled,
Disabled
Indicates whether the stale rule is enabled or disabled
Field Possible
Values
Description

Deleting Stale Rule
To delete a Stale Rule
1. Click the “Delete” button next to the desired Stale Rule.
2. To confirm the Deletion, type in the specified text.
3. Click the “Delete” button in the pop-up window to confirm the deletion.
Exporting a Stale Rule
To Export a Stale Rule
1. Select the desired Stale Rule from the list.
2. Click “Export” and select “Export to Excel” or “Export to CSV”.
Maker Maker_1 The Maker into which the Stale Prices checkers will be applied on.
Symbol
Profile
StaleProfile1 The Symbol Profile into which the Stale Prices will base its settings on.
Liquidity
Models
LM_1,
AGG_Makers
The Liquidity Model to be monitored by the Stale Rule.
Session MON,00:00-
23:59
Defines the time of the day during which the Stale Prices will be checked on.
All days of the week should be included and separated by a semicolon “;” along with the time interval
during the day. 00:00-00:00 represents a closure during a particular day.
Priority 1-10 This parameter applies in the event of overlapping configurations where a Stale Rule with a higher
priority supersedes other overlapping Rules with lower priorities.
Description A short description for reference purposes




