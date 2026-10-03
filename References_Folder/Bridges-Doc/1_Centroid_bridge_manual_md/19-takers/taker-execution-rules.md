[🏠 Document Start](..\README.md) / [Taker API link](README.md) / Taker Execution Rules

# Taker Execution Rules

Overview
The Taker Execution Rules is an advanced feature that gives brokers enhanced control over the flow and execution of trades across
multiple platforms, including MT4, MT5, FIX, and REST API. This functionality enables brokers to define and implement various execution
strategies using key parameters such as tag 1, login, group, symbols, and other unique identifiers. Brokers can automate trade routing
based on specific criteria, giving them greater control over order flow from different platforms.
One of the standout features of Taker Execution Rules is the ability to modify rules in real-time without the need to restart the bridge or
platform plugins. This flexibility allows brokers to respond quickly to changing market conditions or trading behaviors, and seamlessly
onboard new execution strategies. The real-time adaptability helps optimize execution flow, ensuring brokers can react instantly,
maximizing efficiency and control in trade management.
With this feature, brokers can dynamically route orders to different execution models based on pre-set conditions—whether routing trades
to a maker via Straight Through Processing (STP) or internalizing them within the Centroid Bridge. Another key benefit is its ability to
enhance broker privacy. By eliminating the need to disclose tag 1 accounts to clients, it adds an extra layer of confidentiality, preventing
clients from identifying how their trades are being executed.
Taker Execution Rules enhances operational flexibility, enabling brokers to manage trades more effectively and privately, while
maintaining compliance with established trading conditions.

Within this module, you have the capability to:
Define Custom Execution Strategies: Set up tailored execution strategies across MT4, MT5, FIX, and REST API platforms.
Automate Trade Routing: Automatically route trades based on key parameters like tag 1, login, group, symbols, and other identifiers.
Modify Execution Rules in Real-Time: Update execution rules instantly without restarting the bridge or platform plugins.
Optimize Execution Flow: Respond to changing market conditions or trading behaviors efficiently by modifying execution strategies
on the fly.
Route Orders Dynamically: Direct orders to various execution models, such as STP or internalizing them within the Centroid Bridge.
Enhance Broker Privacy: Conceal tag 1 accounts from clients, adding an extra layer of confidentiality to the trade execution process.


Enabling Use Execution Rules
To enable the “Use Execution Rules” for a specific taker:
1. Navigate to the Taker Section
2. Enable the option "Use Execution Rules" for the desired taker
Creating Taker Execution Rules
To create a Taker Execution Rules
1. Click the “Add” button on the top right corner
2. Fill out the Wizard. You may refer to the field descriptions hereafter
3. Click “Submit” to submit the changes


For FIX Connections applying filters like Logins, Groups, Securities, or Directions, ensure that the required FIX tags are included
with each trade to ensure proper execution.
Rules won't be active unless 'Use Execution Rules' is enabled for the specific taker in the Taker section.
Enabled Yes Enabled,
Disabled
Indicates whether the Taker Execution Rule is enabled or disabled
If ticked, the Taker Execution Rule is enabled.
If unticked, the Taker Execution Rule is disabled.
Rule ID No 1,2,3 A unique ID number for the configured rule
Taker No Centroid_MT
5, Taker_FIX
When creating a rule, you must specify the Taker, as each rule is applied to one platform or
Taker.
Source
TEM
Yes TEM_A,
TEM_B
The Source TEM is the Tag 1 configured at the Taker level, where all trades are sent to the
bridge and then redirected to the Target TEM based on Taker Execution Rules. The Tag 1
account also acts as a filter available within the Source TEM for more precise trade routing.
Field Edita
ble
Possible
Values
Description

Bridge
Securities
Yes Bridge
Securities:
FX

Platform
Securities:
Forex\*

This option allows you to select or manage securities at the bridge level. When the 'Platform'
toggle is activated, the label changes to 'Platform Securities,' indicating that the configuration
will apply to platform-specific securities.
Explanation:
Bridge Securities: If you specify a Bridge Security here, only the symbols associated with that
security will be allowed for execution according to the defined rule.
Platform Securities: You can specify the securities available on your taker end or platform.
Once this is done, only symbols associated with those securities will be allowed for execution
according to the defined rules.
Note: For FIX connections, if a Platform Security filter is applied in the rule, FIX Tag 90013
must be included with each trade to ensure it follows the correct rule and execution flow.
Bridge
Symbols
Yes Bridge
Symbols:
EURUSD,XA
UUSD

Platform
Symbols:
EURUSD.x,E
URUSD.p
This field allows for symbol managing at the bridge level. If the 'Platform' toggle is enabled, it
updates to 'Platform Symbols,' reflecting that the symbol is now managed at the platform level.
Explanation:
Bridge Symbols: The 'Bridge Symbols' field allows you to configure symbols at the bridge level.
This option is applicable when the 'Platform' toggle is disabled, meaning symbol configuration
will follow the bridge-specific settings for routing and execution.
Platform Symbols: The 'Platform Symbols' field is displayed when the 'Platform' toggle is
enabled. This field allows you to manage the symbols that are available on the Taker side or
platform end. The mappings configured here will take precedence over bridge-level settings,
ensuring that the platform-specific symbols are used for routing and execution.
Side Yes Buy, Sell The trade side can be specified by selecting either "Buy" or "Sell." Additionally, the use of a
wildcard (*) allows for the inclusion of both sides, providing greater flexibility in trade execution.
Order Type Yes Market, Limit,
Stop
The type of order can be specified by selecting from options such as "Limit," "Market," or
"Stop." Additionally, the use of a wildcard (*) allows for the inclusion of all order types, providing
greater flexibility in trade execution.
ExtPartyId
1 (Login)
Yes 10012,10015 This parameter serves as the unique login identifier for the external party involved in trade
execution, enabling accurate order tracking and management.
MT5: Specify the MT5 logins in this field.
FIX: Specify the logins here, but ensure the corresponding FIX tag 90001 is included when
sending the order to follow the correct rule.
Note: Multiple accounts can be specified by separating them with a comma (",")
ExtPartyId
2 (Group)
Yes RetailGroup\*
,StandardGro
up\*
This parameter identifies the group associated with the external party, enabling trade execution
based on specific rules applicable to that group.
MT5: Specify the MT5 group here.
FIX: Specify the group here, but ensure the corresponding FIX tag 90002 is included when
sending the order to apply the correct grouping rule.
Note: Multiple groups can be specified by separating them with a comma (",")
Time in
Force (TIF)
Yes FOK, IOC,
GTC
You can choose from the available options i.e. Day, FOK, GTC, GTD and IOC and orders will
execute according to your selected settings.
Direction Yes IN, OUT You can select “IN”, “OUT” or “IN_OUT” to execute trades based on the directions.

To configure or modify an existing Taker Execution Rules
1. Track the desired Taker Execution Rules
2. Configure the desired fields
3. Click the “Save” button on top to deploy the changes
Adjusting Taker Execution Rules Order
How to adjust the order of Taker Execution Rules
Execution rules are read from top to bottom. Brokers can adjust the order using the drag-and-drop feature, allowing them to control which
rules take priority.
Delete Taker Execution Rules
To delete a Taker Execution Rules
Note: For FIX connections, if a Direction filter is applied in the rule, FIX Tag 90014 must be
included with each trade to ensure it follows the correct rule and execution flow.
Min Size Yes 1000 Min Size is the minimum trade volume for the rule to apply, ensuring trades below this are not
routed by the rule, but it doesn't limit the overall trade size.
Max Size Yes 50000 Max Size is the largest trade volume allowed for the rule to apply, ensuring trades above this
limit are excluded, but it doesn't restrict smaller trades.
Target TEMYes CentroidExec
ution_TEM
This is the TEM configured on the bridge where trades are directed. Trades coming from the
default account or TEM will be routed to the Target TEM based on the settings you’ve defined
above. This ensures that all trades are managed according to your specified rules, allowing for
precise execution and control.
Description Yes A short description for reference purposes
All changes made at the settings level take effect immediately and do not require restarting the bridge.


2. Enter the ID in the pop-up window & Click on “Delete” button to confirm the deletion
Exporting Taker Execution Rules
To Export Taker Execution Rules
1. Click “Export” and select “Export to Excel” or “Export to CSV”
Uploading Taker Execution Rules
To Upload Takers Execution Rules
1. Click on “Upload”
2. Click on “Drop File” and select the File or drag the file to this section to upload.


Replace All - Checked
Replace All - Unchecked
4. You also have the option to discard the bulk upload by clicking on the “Close” Button
When uploading Taker Execution Rules, the "Replace All" option allows you to control how new rules are applied:
Replace All - Checked If checked, this will overwrite all existing
rules with the new rules in the uploaded
file. The final set of rules will only include
those present in the uploaded file.
Replace All - Unchecked If unchecked, the system will append new
rules from the file to the existing ones. This
may result in duplicate entries if the file
contains rules already present in the
system.
Replace All Description Result


Sample Rules and Trade Processing with Execution Rules
Scenario 1: For MT5 Takers
As shown in the snapshot, the rule specifies that if a trade comes through Tag 1 "Centroid_TEM_A", from MT5 Login ID 10012, and is a
Market Order, it will be redirected to the Centroid_TEM_C account.
Additionally, there's a filter for Min Size and Max Size:
Min Size: 2000
Max Size: 5,000,000
(Both in volumes)
If the trade volume is below 2000, it won’t execute with Centroid_TEM_C. Instead, the system will move to the next rule to check its
conditions. But if the trade volume falls between 2000 and 5,000,000, it will be executed with Centroid_TEM_C.
Additionally, if no rules match the trade’s criteria and filters, the trade will be rejected by Centroid Bridge.

Scenario 2: For FIX Takers
As shown in the snapshot, the rule specifies that if a trade comes through Tag 1 "Centroid_TEM_1", with the symbol "XAUUSD" and is
an IOC Order, it will be redirected to the Centroid_TEM_2 account.
This rule applies only to XAUUSD trades as IOC orders. If a trade involves a different symbol, the bridge will move to the next rule and
check its conditions. If no rules match the trade's criteria and filters, the trade will be rejected by Centroid Bridge.



