[🏠 Document Start](..\README.md) / [Taker Execution Model](README.md) / Taker API link

# Taker API link

Overview
The Taker API link is a versatile functionality capable of serving multiple purposes. For every order that the bridge receives to broker can
control the flow and modify the order. It can redirect trades to another Taker Execution Model based on predetermined conditions, add
custom tags for the Maker API Link, identify scalpers and trade patterns, and redirect them accordingly. The Bridge performs Taker API
Link verification among its initial checks before trade execution.
In this component, you will be able to do the following:
1. Create a new Taker API Link
2. Filter the current configured Taker API Links by different criteria
3. Enable/Disable a particular rule
4. View and edit a current configured Taker API Link
5. Delete a Taker API Link rule
6. Click “Export” and select “Export to Excel” or “Export to CSV”
Creating a Taker API Link rule
To create a Taker API Link rule
1. Click “Add” button to create a new Taker API Link rule
2. Fill out the Wizard. You may refer to the field descriptions below
3. Click “Submit” to submit the changes


ID 1,2,3,10 A unique ID number for the configured rule
Takers Centroid_M
T5,
Centroid_M
T4
Select one or multiple Takers to be included in the configuration as source(s) You may select
the Takers from the available list of Takers or enter comma separated values manually by
ticking the “Pattern” tick box
Taker Execution
Models
TEM-1,
TEM-2,
Test_TEM
Select one or multiple Taker Execution Models to be included in the configuration as source(s)
You may select the Taker Execution Models from the available list of Taker Execution Models or
enter comma separated values manually by ticking the “Pattern” tick box
Securities FX, CFD Select one or multiple Securities from the available Securities in the Centroid Bridge to be
included in the configuration.
You may select the Securities from the available list of Securities or enter comma separated
values manually by ticking the “Pattern” tick box
Symbols EURUSD,
XAUUSD
Select one or multiple Securities from the available Symbols in the Centroid Bridge to be
included in the configuration.
You may select the Symbols from the available list of Symbols or enter comma separated
values manually by ticking the “Pattern” tick box
Makers Liquidity
Provider
Select one or multiple Makers to be included as a Target to which the Orders are routed.
You may select the Makers from the available list of Makers or enter comma separated values
manually by ticking the “Pattern” tick box
Sides Buy, Sell, All Select the side of the Order if you need to pass on values for a particular side, such as Buy or
Sell. Otherwise, just select “*” to include all Order sides
Ord Types Market,
Limit
Select the type of the Order if you need to pass on values for a particular execution type, such
as Market, Limit or Stop. Otherwise, just select “*” to include all Order types
Source ExtLogin MT4/MT5 Login number for Takers of type MT4/MT5
Default Value = 0 (all logins)
Field Possible
Values
Description

Note: Below are the available macros that can be used for Rule Macros.
Source ExtGroup Name of MT4/MT5 Group for Takers of type MT4/MT5
Rule Macro #tem# Select the predefined Macros from the dropdown by inputting #. In the subsequent table, we will
outline the definitions for the available macros.
Rule Value tem_b The value to be assigned to the Rule Macro.
For example: If the Rule Macro is #tem# then the Rule Value = tem_b.
Priority 1-10 The priority is essential in the event of having overlapping configurations and defines which
configuration should supersede. The configuration with the highest Priority always supersedes.
Min Size 0 Min size sets the lower limit in Volume for the Scalping threshold. Trades falling below Min Size
won't qualify for the scalping threshold.
Note: Minimum Size, Maximum Size, and Scalping Threshold are interrelated and function
together.
Default Value = 0
Max Size 1000 Max size sets the upper limit in Volume for the Scalping threshold. Trades falling above Max
Size won't qualify for the scalping threshold.
Note: Minimum Size, Maximum Size, and Scalping Threshold are interrelated and function
together.
Default Value = -1 (disabled)
Scalping Threshold
(ms)
300 Threshold in milliseconds to qualify for the Scalping threshold. It will be the time interval
between opening & closing a trade.
Note: Minimum Size, Maximum Size, and Scalping Threshold are interrelated and function
together.
Default Value = -1 (disabled)
Order Repetition
Interval (sec)
20 This component is used to detect the interval between two or more order with same volume,
same symbol, same side and same login.
Order Repetition
Counter
3 In this component you can input the number of time you will allow the repetition of same
volume, same symbol, same side and same login.
Description A short description for reference purposes
Enable Enabled,
Disabled
Indicates whether the configuration is enabled or disabled
If ticked, the Taker API Link is enabled upon creation
If unticked, the Taker API Link is disabled upon creation, hence no Tags or Values would be
passed on
#taker# The name of the Taker through which the Order was initiated
#tem# The name of the Taker Execution Model through which the Order was routed
#login# The MT4/MT5 Login number that placed the Order, in case it was initiated via an MT4/MT5 Taker
#order
#
This is relevant to Orders originated from a Taker of type MT4 or MT5.
MT4: Order will send the Ticket Number of the MT4 trade
MT5: Order will send the Order Number of the MT5 trade
Value Description

To configure a Maker API Link configuration
1. Double-click the desired column(s) in the Taker API Link Configuration.
2. For some columns, you are presented with a pop-up Window where you can edit and click submit as seen below. This process needs
to be done separately for each column or parameter
3. Click on “Save” to save the changes.
Delete a Taker API Link Rule
To delete a Maker API Link configuration
1. Click the “Delete” icon next to the desired Taker API Link configuration
2. To confirm deletion, type the ID of the Taker API Link in the field.
3. Click on the "Delete" button to confirm deletion.
Exporting a Taker API Link Rule
To export a Maker API Link configuration
1. Select the desired Taker API Link from the list
#pos# This is relevant to Orders originated from a Taker of type MT5. It sends the Position Number of the MT5 trade
#group
#
The name of the MT4/MT5 Group of the Account that placed the Order, in case it was initiated via an MT4/MT5 Taker
#deal# This is relevant to Orders originated from a Taker of type MT5. It sends the Deal Number of the MT5 trade
#____# This can be utilized to create any custom rule macro


2. Click “Export” and select “Export to Excel” or “Export to CSV”
Case Studies:
Case 1. Route Trades based on Filters.
In the below case study, we'll demonstrate how to route LIMIT orders to a different Taker Execution Model (TEM).
Set the filters as per the requirement and you must configure the Ord Types, Rule Macro and Rule Value.
Taker Execution Model → tem_a
Ord Types → LIMIT
Rule Macro → #tem#
Rule Value → tem_confirm
Explanation: If there are any LIMIT trades to be executed using tem_a, they will be rerouted to a different TEM - tem_confirm
Case 2. Modify Maker API link tags using Taker API link
In this case study, we will understand the process of modifying tag1 values before sending them to the Maker for a specific MT4/5 group.
For example, If you have a second account with your liquidity provider and desire to forward trades from a specific MT4/5 group to that
account, you can achieve this by utilizing both the Taker and Maker API links together.
Taker API Link:
Set the filters as per the requirement and you may configure the Source Ext Group, Rule Macro and Rule Value.
Source ExtGroup → real\VIP
Source ExtLogin
To redirect trades to another TEM, ensure that the Rule Macro is set to #tem#, and the Rule Value contains the name of the
specific Taker Execution Model (TEM) where the trades should be rerouted.

Rule Macro → #LPAccount#
Rule Value → 371294
Maker API Link:
Review the Maker API Link page on creating new rules.
Explanation: All trades executed from login “10001” will contain #LPAccount#=371294 where this value will be sent to the maker
“LIQUIDITY_PROVIDER” via FIX tag 526 as stated in the Maker API Links rule.
Case 3. Route trades using Scalping Threshold.
Set the filters as per the requirement and you may configure the Min Size, Max Size, Scalping Threshold, Rule Macro and Rule Value.
Symbols → XAUUSD
Min Size → 1000
Max Size → 10,000
Scalping Threshold → 2000ms
Rule Macro → #tem#
Rule Value → tem_scalpers
Explanation: If there are any XAUUSD trades executed within the specified Volume Range of 1000 to 10,000, both opened and closed
within 2000ms by the same login, they will be rerouted to a different TEM - tem_scalpers.
The Rule Macro can be any unused keyword within the bridge, enclosed by "#" at the beginning and end. The Rule Value will be
the tag value to be passed on to the Maker API link.


To redirect trades to another TEM, ensure that the Rule Macro is set to #tem#, and the Rule Value contains the name of the
specific Taker Execution Model (TEM) where the trades should be rerouted.

