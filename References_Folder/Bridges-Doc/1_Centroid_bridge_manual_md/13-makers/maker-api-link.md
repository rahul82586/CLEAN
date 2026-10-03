[🏠 Document Start](..\README.md) / [Guidelines for Receiving and Incorporating the Centroid Maker into Your Centroid Bridge](README.md) / Maker API link

# Maker API link

Overview
The Maker API Link component is an added feature for sending lists of values over FIX tags with order requests to the Maker. These lists
can be necessary for Makers or used to distinguish specific orders.
One of its useful cases is when targeting different Accounts in a Maker Session, the Account name is sent in tag 1 to ensure the Order is
booked into the correct Account on the Maker side.
The diagram below illustrates how the Maker API Link functions.
Rules to be applied/created under Maker API Link
Rule 1 → This rule will consist of filtered trades from Centroid_MT4 from any “Taker Execution Model” to be sent to the maker with Tag
1 (account) with value “Account-1” as a low priority of 1 which can be superseded by higher priority.
Rule 2 → This rule will consist of filtered trades from Centroid_MT4 from the Taker Execution Model of “TEM 2” to be sent to the maker
with Tag 1 (account) with value “Account-2” as a high priority of 2 which can supersede low priority such as 1.
To summarize, any trades incoming from TEM-2 will be re-directed to Account-2 as the rule priority is set to 2, which means Rule 2 will
take effect first followed by Rule 1.
As mentioned above, the Maker API Link can be configured down to the level of the Taker Execution Model and can be done for specific
Securities or Symbols as well.

In this component, you will be able to do the following:
1. Create a new Maker API Link.
2. Filter the currently configured Maker API Links by different criteria.
3. Enable/Disable a particular configuration.
4. View and edit a currently configured Maker API Link.


6. Click “Export” and select “Export to Excel” or “Export to CSV”.
Creating a Maker API Link Rule
To create a new Maker API Link:
1. Click the “Add” button to create a new Maker API Link.
2. Fill out the Wizard. You may refer to the field descriptions hereunder.
3. Click “Submit” to submit the changes.
Note: In the Values parameter, you can add multiple values depending on your requirements by clicking the “Add Values” button.
ID 1,2,3,10 A unique configuration ID number for reference purposes. When creating a new configuration,
make sure the ID does not exist already.
Takers Centroid_MT5
,
Centroid_MT4
Select one or multiple Takers to be included in the configuration as source(s). You may select the
Takers from the available list of Takers or enter comma-separated values manually by ticking the
“Pattern” tick box.
Taker Execution
Models
TEM-1, TEM-
2, Test_TEM
Select one or multiple Taker Execution Models to be included in the configuration as source(s).
You may select the Taker Execution Models from the available list of Taker Execution Models or
Field Possible
Values
Description

Note: For patterns, you may use wildcards “*” and negations “!” to include all or exclude certain values.
enter comma-separated values manually by ticking the “Pattern” tick box.
Liquidity Models Liquidity_Mod
el
Select one or multiple Liquidity Models to be included in the configuration as source(s). You may
select the Liquidity Model from the available list of Liquidity Models or enter comma-separated
values manually by ticking the “Pattern” tick box.
Securities FX, CFD Select one or multiple Securities from the available Securities in the Centroid Bridge to be
included in the configuration.
You may select the Securities from the available list of Securities or enter comma-separated
values manually by ticking the “Pattern” tick box.
Symbols EURUSD,
XAUUSD
Select one or multiple Securities from the available Symbols in the Centroid Bridge to be included
in the configuration.
You may select the Symbols from the available list of Symbols or enter comma separated values
manually by ticking the “Pattern” tick box.
Makers Liquidity
Provider
Select one or multiple Makers to be included as a Target to which the Orders are routed.
You may select the Makers from the available list of Makers or enter comma-separated values
manually by ticking the “Pattern” tick box.
Sides Buy, Sell, All Select the side of the Order if you need to pass on values for a particular side, such as Buy or
Sell. Otherwise, just select “*” to include all Order sides.
Ord Types Market, Limit Select the type of the Order if you need to pass on values for a particular execution type, such as
Market, Limit or Stop. Otherwise, just select “*” to include all Order types.
Priority 1-10 The priority is essential in the event of overlapping configurations and defines which configuration
should supersede. The configuration with the highest Priority always supersedes.
You may refer to the above diagram example to understand how the Priority works.
Enable Enabled,
Disabled
Indicates whether the configuration is enabled or disabled.
If ticked, the Maker API Link is enabled upon creation.
If unticked, the Maker API Link is disabled upon creation, hence no Tags or Values would be
passed on.
Description A short description for reference purposes.
Values Tag: 1, Value:
LP Account
Number
The Tags and Values to be passed on in the execution message. It is divided into two
parameters:
Tag: Enter the tag number you wish to send across. For example, if you select and put in the
value 1 under Tag, this means you are targeting a particular account.
Value: You can select any Value to be passed on for the selected Tag. It can be either entered
manually by typing in the value or passed on as a predefined value using the # key as
explained hereafter.
You may add as many Values (Tag and Value) as you want by clicking the “Add Value” button.
A common example is Tag 1 in case you are targeting different Accounts within a Maker Session.
Account is equivalent to Taker Execution Model in the Maker Class is Centroid. For instance, to
target an Account called “Acc001”, you simply add the Values: 1 in the Tag textbox and Acc001 in
the Value textbox.
Note: You can pass on some values using macros by putting the parameter name in between two
# keys. You may refer to the list of predefined values below.

Note: Below are some of the macros that can be passed across to the Maker while executing the Order using the hash “#” keys.
Available macros for sending prices based on the order type.
Configuring Maker API Link
To configure a Maker API Link configuration:
1. Double-click the desired column(s) in the Maker API Link Configuration.
2. For some columns, you are presented with a pop-up Window where you can edit and click submit as seen below. This process needs
to be done separately for each column or parameter.
3. Click the “Submit” button to apply the changes.
4. Click on “Save” to finally save the changes.
5. Click the “Revert All” button to undo the changes that have been made
#taker# The name of the Taker through which the Order was initiated.
#tem# The name of the Taker Execution Model through which the Order was routed.
#login# The MT4/MT5 Login number that placed the Order, in case it was initiated via an MT4/MT5 Taker.
#order# This is relevant to Orders originating from a Taker of type MT4 or MT5.
MT4: Order will send the Ticket Number of the MT4 trade.
MT5: Order will send the Order Number of the MT5 trade.
#pos# This is relevant to Orders originating from a Taker of type MT5. It sends the Position Number of the MT5 trade.
#group
#
The name of the MT4/MT5 Group of the Account that placed the Order, in case it was initiated via an MT4/MT5 Taker.
#deal# This is relevant to Orders originating from a Taker of type MT5. It sends the Deal Number of the MT5 trade.
Value Description
#ordpx# To include order price “limit/stop price”
#ordtobpxb# To include Agg Book raw ToB bid price to any defined FIX tag, while setting up the rule you might want to filter is as
Sell rule.
#ordtobpxa# To include Agg Book raw ToB ask price to any defined FIX tag, while setting up the rule you might want to filter is as
Buy rule.
#ordextpxb# To include Ext ToB bid price to any defined FIX tag, while setting up the rule you might want to filter is as Sell rule.
#ordextpxa# To include Ext ToB ask price to any defined FIX tag, while setting up the rule you might want to filter is as Buy rule.
#reqpx# To include request price “ToB or level book price” to any defined FIX tag
Macro Value Definition


To delete a Maker API Link configuration:
1. Click the “Delete” icon next to the desired Maker API Link configuration.
2. To confirm the Deletion, type in the specified text.
3. Click the “Delete” button in the pop-up window to confirm the deletion.
Exporting a Maker API Link
To export a Maker API Link configuration:
1. Filter the desired ID from the list to be able to export a specific Maker API Link rule.
2. Click “Export” and select “Export to Excel” or “Export to CSV”.


