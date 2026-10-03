[🏠 Document Start](..\README.md) / [Balance Transaction](README.md) / Taker Risk Filter

# Taker Risk Filter

Overview
Taker Risk Filter allows you to set up filters or rules to link existing risk account(s) using the available filters such as Taker Execution
Model, Liquidity Model, Group, Login, etc.
In this component, you will be able to do the following:
1. Add a New Taker Risk Filter rule: Create and implement a new rule for the Taker Risk Filter.
2. Filter Taker Risk Filter Rules by Different Criteria: Utilize filters to sort and view Taker Risk Filters based on specified criteria.
3. Enable/Disable a Particular Taker Risk Filter Rule: Toggle the active status of a specific Taker Risk Filter rule on or off.
4. Configure a Particular Taker Risk Filter Rule: Modify and tailor the settings of a particular Taker Risk Filter rule by editing
configurable parameters.
5. Delete a Taker Risk Filter Rule: Remove a Taker Risk Filter rule that is no longer needed.
6. Export the List of Taker Risk Filter Rules to an Excel File / CSV File: Generate a downloadable file (Excel or CSV) containing the
comprehensive list of Taker Risk Filter Rules for external reference or documentation purposes.
Creating a Taker Risk Filter
To create a Taker Risk Filter
1. Click the “Add” button on the top right corner

2. Fill out the Wizard. You may refer to the field descriptions hereafter
3. Click “Submit” to submit the changes


Risk Account FIX_RA Name of the risk account to which the filters need to be applied.
Takers Centroid_MT
5,
Centroid_MT
4
Select one or multiple Takers to be included in the filter as source(s) You may select the
Takers from the available list of Takers.
Taker Execution
Models
TEM-1, TEM-
2, Test_TEM
Select one or multiple Taker Execution Models to be included in the filter as source(s) You
may select the Taker Execution Models from the list, separating them with commas.
Liquidity Models LP1_LM Select one or multiple Liquidity Models to be included in the filter as source(s) You may select
the Liquidity Models from the list.
Securities FX, CFD Select one or multiple Securities to be included in the filter as source(s) You may select the
Securities from the list, separating them with commas.
Field Possible
Values
Description

Configuring a Taker Risk Filter
To configure/modify an existing Taker Risk Filter
1. Double-click the desired column(s) in the Taker Risk Filter.
2. You will be presented with a pop-up Window where you can edit and click submit as seen below.
3. Click on “Save” to save the changes.
Deleting a Taker Risk Filter
To delete a Taker Risk Filter
1. Click the “Delete” icon next to the desired Taker API Link configuration
2. Enter the ID in the pop-up window & Click on “Delete” button to confirm the deletion
Exporting a Taker Risk Filter
To export a Taker Risk Filter configuration
1. Filter the desired Taker Risk Filter rules using the available filters.
Symbols EURUSD,
XAUUSD
Select one or multiple Symbols to be included in the filter as source(s) You may select the
Symbols from the list, separating them with commas.
Groups real\vip Name of MT4/MT5 Group for Takers of type MT4/MT5
Logins 0, 100002,
500005
MT4/MT5 Login number for Takers of type MT4/MT5
Default Value = 0 (all logins)
Sides BUY, SELL,
ALL
Select the side of the Order to be included as a filter, such as Buy or Sell. Otherwise, just
select “*” to include all Order sides
Order Types LIMIT,
MARKET
Select the Type of the Order to be included as a filter, such as Market, Limit or Stop.
Otherwise, just select “*” to include all Order types.
Mode ALL, A, B Select the Mode to be included as a filter:
A Book: Only considers A Book trades that are routed to the Maker
B Book: Only considers B Book trades that are internalized in the Centroid Bridge
All: Considers all trades.
Priority 1,2,10 This parameter applies in the event of having overlapping configurations. You can proceed to
set the priority to adjust the rules, On a scale 1-10, rule with priority 10 will be considered first.
Description A short description for reference purposes


2. Click “Export” and select “Export to Excel” or “Export to CSV”



