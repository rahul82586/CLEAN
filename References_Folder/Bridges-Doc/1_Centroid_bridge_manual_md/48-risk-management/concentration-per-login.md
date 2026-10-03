[🏠 Document Start](..\README.md) / [Risk Management](README.md) / Concentration Per Login

# Concentration Per Login

Overview
Concentration Per Login facilitates exposure management, this feature allows the brokers to customize exposure settings for every
MT4/MT5 login at the symbol level. It also assists in crucial decision-making, by offering the option to Manage or Limit the allowed
exposure in terms of traded volume.
Note: Concentration per login works only with BBook Trades.
Manage (By Default): When referring to ‘Manage,' it entails that if the MT4/MT5 Login surpasses the exposure set at the symbol level, all
incoming trades for that symbol should be redirected to the Maker.
Limit (Macro Rule): When referring to 'Limit,' it means that if the MT4/MT5 Login surpasses the exposure set at the symbol level, all
incoming trades for that symbol should be automatically 'Rejected’.
* Macro Rule → #reject#
Within this module, you have the capability to:
Add a New Concentration Per Login Rule: Create and implement a new rule for the Concentration Per Login functionality.
Filter Concentration Per Login Rules by Different Criteria: Utilize filters to sort and view Concentration Per Login rules based on
specified criteria.
Enable/Disable a Particular Concentration Per Login Rule: Toggle the active status of a specific Concentration Per Login rule on or
off.
Configure a Particular Concentration Per Login Rule: Modify and tailor the settings of a particular Concentration Per Login rule by
editing configurable parameters.
Delete a Concentration Per Login Rule: Remove a Concentration Per Login rule that is no longer needed.
Export the List of Concentration Per Login Rules to an Excel File / CSV File: Generate a downloadable file (Excel or CSV)
containing the comprehensive list of Concentration Per Login Rules for external reference or documentation purposes.
Creating a Concentration Per Login
To create a Concentration Per Login
1. Locate Concentration Per Login and then click the “Add” button


2. Fill out the Wizard. You may refer to the field descriptions below
3. Click “Submit” to submit the changes
ID A unique ID number for the configured rule
Taker The source Taker(s) You may select one or multiple Takers from the list or type a pattern manually by ticking the
Pattern tick-box
Note: You may use wildcards (*) for all and negations (!) for exclusion when typing a pattern
TEM Trades executed with this source TEM will adhere to the exposure rule, additionally following Source Login and
Group Filter criteria.
Securities Specifying a security here indicates that only the symbols falling under this security are eligible to adhere to the
concentration per login rule, either by managing or limiting the exposure.
Symbols The exposure limit will be exclusively applied to the symbols specified here. If no symbols are selected, it implies
that all symbols within the chosen security will adhere to the exposure rule.
Sides Default Value: * [meaning all] However, broker can further change the settings to either Buy or Sell trades.
Ord Types The additional filter for order types enables you to specify whether you want the exposure rule applied to market
orders, limit orders, stop orders, or all (*).
Source
ExtLogin
This parameter allows you to enter a specific MT4/MT5 Login number.
Note: You can add only one account at a time.
Note: Entering '0' means that all accounts will adhere to this exposure rule.
Source
ExtGroup
This parameter enables you to enter a specific MT4/MT5 Group to adhere to the exposure rule. Note: You can add
multiple groups by using a comma (',').
Limit This parameter empowers you to establish the exposure for the selected filters (Account, Symbol, Group, TEM). The
limit is specified in volumes.
Example:
Symbol: XAUUSD
MT5 Login: 12012
Limit: 100,000 volumes
In the given example, if the account 12012 surpasses the set exposure limit, subsequent incoming trades will be
either redirected to the Maker or rejected, depending on the specified rule.
Adjustment
Value
When set to 1, the purpose is to trigger a flag, allowing fractional volume to be counted towards 'B,' even if it
exceeds the limit for A-book routing.
Field Description

To configure a Concentration Per Login
1. Select the desired Concentration Per the Login rule.
2. Configure the desired fields.
3. Click the “Save” button on top to deploy the changes.
Priority This parameter applies in the event of having overlapping configurations. You can proceed to set the priority to
adjust the rules, On a scale 1-10, rule with priority 10 will be considered first.
Description This is the section where you can determine whether you want to manage the exposure or limit the exposure.
If you choose option 1, which is 'Manage,' you can add any value or text in the description box for reference purposes only.
On the other hand, if you choose option 2, which is 'Limit,' you must add a macro rule in the description box, and the value should be '#reject#.
By adding the macro rule, you have specified that if any filtered account/group/symbol/TEM exceeds the set exposure, subsequent incoming trades will be rejected.
Enable Indicates whether the Rule is enabled or disabled
If ticked, the Rule is enabled
If unticked, the Rule is disabled, hence no is applied
ID No 100, 1, 12 A unique ID number for the configured rule
Taker Yes Centroid_MT
5
The source Taker(s) You may select one or multiple Takers from the list or type a pattern
manually by ticking the Pattern tick-box
Note: You may use wildcards (*) for all and negations (!) for exclusion when typing a pattern
TEM Yes TEM-1 Trades executed with this source TEM will adhere to the exposure rule, additionally following
Source Login and Group Filter criteria.
Securities Yes CFD Specifying a security here indicates that only the symbols falling under this security are
eligible to adhere to the concentration per login rule, either by managing or limiting the
exposure.
Symbols Yes XAUUSD The exposure limit will be exclusively applied to the symbols specified here. If no symbols
are selected, it implies that all symbols within the chosen security will adhere to the exposure
rule.
Sides Yes *, Buy, Sell Default Value: * [meaning all] However, broker can further change the settings to either Buy
or Sell trades.
Ord Types Yes Market, Limit The additional filter for order types enables you to specify whether you want the exposure
rule applied to market orders, limit orders, stop orders, or all (*).
Field Editab
le
Possible
Values
Description

To delete a Concentration Per Login
1. Click the “Delete” icon next to the desired Concentration Per Login.
2. To confirm the Deletion, type in the specified text.
3. Click the “Delete” button in the pop-up window to confirm the deletion.
Source
ExtLogin
Yes 10012,
10013
This parameter allows you to enter a specific MT4/MT5 Login number.
Note: You can add only one account at a time.
Note: Entering '0' means that all accounts will adhere to this exposure rule.
Source
ExtGroup
Yes Testonly\A-
10
This parameter enables you to enter a specific MT4/MT5 Group to adhere to the exposure
rule. Note: You can add multiple groups by using a comma (',').
Limit Yes 100000,
350000
This parameter empowers you to establish the exposure for the selected filters (Account,
Symbol, Group, TEM). The limit is specified in volumes.
Example:
Symbol: XAUUSD
MT5 Login: 12012
Limit: 100,000 volumes
In the given example, if the account 12012 surpasses the set exposure limit, subsequent
incoming trades will be either redirected to the Maker or rejected, depending on the
specified rule.
Adjustment
Value
Yes 1 When set to 1, the purpose is to trigger a flag, allowing fractional volume to be counted
towards 'B,' even if it exceeds the limit for A-book routing.
Priority Yes 1, 2, 5, 10 This parameter applies in the event of having overlapping configurations. You can proceed to
set the priority to adjust the rules, On a scale 1-10, rule with priority 10 will be considered
first.
Description Yes This is the section where you can determine whether you want to manage the exposure or limit the exposure.
If you choose option 1, which is 'Manage,' you can add any value or text in the description box for reference purposes only.
On the other hand, if you choose option 2, which is 'Limit,' you must add a macro rule in the description box, and the value should be
'#reject#.
By adding the macro rule, you have specified that if any filtered account/group/symbol/TEM exceeds the set exposure, subsequent incoming
trades will be rejected.
Enable Yes Enabled,
Disabled
Indicates whether the Rule is enabled or disabled
If ticked, the Rule is enabled
If unticked, the Rule is disabled, hence no is applied


To Export a Concentration Per Login
1. Click “Export” and select “Export to Excel” or “Export to CSV”.



