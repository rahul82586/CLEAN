[🏠 Document Start](..\README.md) / [MT5 Centroid DOM Feeder Manual](README.md) / MT5 Centroid Gateway Manual

# MT5 Centroid Gateway Manual

Before initiating the setup for the Centroid MT5 Gateway, you'll need to provide the following information to whitelist your IPs:
1. Provide the IP or DNS of all MT5 Live Servers where the MT5 Gateway will be installed.
2. Supply the IP or DNS of all MT5 Live Backup Servers.
To configure the Centroid MT5 Gateway, follow the instructions below:
1. Remotely log in to the server where the MT5 Server is installed using RDP or another tool.
2. Copy the Centroid MT5 Gateway folder into the "Gateway" directory of your MT5 History Server installation. “The path will resemble
D or C:\MetaTrader 5 Platform\History\Gateway.”
Note:
1. The installation process does not necessitate stopping the MT5 Service.
2. The Centroid MT5 Gateway will be automatically duplicated to the MT5 Backup Server.
To set up the Centroid MT5 Gateway:
1. Log into MT5 Administrator and navigate to Gateways.
2. Add a new Gateway.
3. Customize the newly added Gateway as follows:
Name: Specify the configured Gateway's name.
Module: Locate the Gateway file within the uploaded folder.
Select: Choose "Trade Only" from the dropdown.
Trading Server: Provide the DNS and Port details given by Centroid.
Trading Login: Enter the trading login ID provided by Centroid.
Password: Input the trading password provided by Centroid.
Essential Setup Information
Installation
Configuration

Note: Make certain that all the Groups and Symbols intended for processing by the Gateway are appropriately listed in the Groups and
Symbols tabs, respectively.


When upgrading the Centroid MT5 Gateway to a newer version, adhere to the following steps, ensuring the new folder supersedes the old
one for simplicity:
To enhance the Centroid MT5 Gateway, proceed with the following instructions:
1. Access the Server: Remotely access the server where the MT5 Server is installed, using RDP or any other tool.
2. Backup the Old Version: Safeguard your current Centroid MT5 Gateway folder by copying it into a separate folder. This backup
facilitates a seamless reversion to the previous version if necessary.
3. Disable the Centroid Gateway: Before replacing the file, it is recommended to disable the “Centroid Gateway” from the MT5
Administrator.
4. Replace the File: Overwrite the existing Centroid MT5 Gateway folder in the MT5 History Installation with the new one.
5. Enable the Centroid Gateway: Re-enable the Gateway using the MT5 Administrator.
To Set-Up the Centroid Gateway in your MT5, please follow the steps outlined below:
Updating the Gateway
Setting up the “Centroid Gateway”


Let's categorize the parameters into two groups:
General Parameters
Facilitating the connection of your "Centroid Gateway" (MT5) to the "Centroid Bridge” (Bridge).
Define the "Execution Rules."
The routing rules determine how trades from various MT5 Groups, Logins, Groups of Symbols, or Symbols are directed to specific
accounts or Taker Execution Models (TEM) on the Centroid Bridge.
Explanation:
sec = group of symbols (Example: Forex\Major)
sy = symbols
g = groups
ac= accounts / logins
tem = Taker Execution Model on the “Centroid Bridge”
dir = direction of the order (close/open)
1. No Filters
2. Group Filter
Sender Example: TD_Username This is available in the 'Centroid Bridge' Taker -> Config -> SenderCompID. Please
note: The format is supposed to be TD_Username.
Account Example: TEM-1, Test_TEM,
Plain_TEM
This Account will represent that, you wish to target this Account while executing your
trades, this is available in the "Centroid Bridge" under Taker -> Taker Execution
Model (TEM) and this will be further used while establishing the "Execution Rules".
Parameter Value Description
AccCfg.1 sec=*;g=*;tem=Test_TEM This rule defines all the securities and all the groups will target one Taker
Execution Model “TEM” i.e. Test_TEM
Parameter Value Description


3. Symbol and Group Filter
4. Account Filter
AccCfg.1 sec=*;g=ABC\USD;tem=TEM-1 This rule defines all the securities from a specific group i.e. “ABC/USD” will
target to TEM → TEM-1
AccCfg.2 sec=*;g=ABC\USD,Testonly\A-
1,Testonly\B-2;tem=TEM-1
This rule defines Multiple Groups Targeting one TEM
AccCfg.3 sec=*;g=Testonly\*;tem=5points_TEM This rule defines All the Groups under Testonly\ Targeting one TEM
Parameter Value Description
AccCfg.1 sy=EURUSD.test;g=NYZ\USD;tem=TEM-
2
This rule defines only symbol “EURUSD.test” from the group
“NYZ\USD” will target to TEM → TEM-2
AccCfg.2 sy=EURUSD.test,GBPUSD.test;g=NYZ\
USD;tem=TEM-2
This rule defines Multiple Symbols from the group “NYZ\USD”
will target to TEM → TEM-2
AccCfg.3 sy=EUR*;g=NYZ\USD,Testonly\A1;tem=
TEM-2
This rule defines All EUR symbols from specific two groups will
target TEM → TEM-2
Parameter Value Description
AccCfg.1 sy=*;ac=100012;tem=Plain_TEM This rule defines all the symbols available in the account 100012 will
target to TEM → Plain_TEM
Note: Account rules should always be placed at the Top of all the
Group rules, as the “Gateway” follows Top-Down Approach.
Parameter Value Description

5. Entry Direction Filter
Additional Parameters
Configure these parameters to utilize the add-on features provided by the "Centroid Bridge."
1. EnGiveUp
Configuration Guide →
Assign the configured "Centroid Gateway" to the "Slave Account" to establish a seamless connection.
AccCfg.2 sy=*;ac=100012,100015,102256;tem
=Plain_TEM
This rule defines Multiple Accounts/Logins Targeting one TEM
AccCfg.3 ac=501265,511456;tem=TEM-2 This rule defines Multiple Accounts/Logins Targeting one TEM
AccCfg.1 sec=*;g=real/fx-
1;tem=Plain_TEM;dir=in
This rule defines all the symbols available in the group real/fx-1 from
any account with deal entry as IN or opening orders will be directed to
Plain_TEM
AccCfg.2 sec=*;g=real/fx-
1;tem=Slip_TEM;dir=out
This rule defines all the symbols available in the group real/fx-1 from
any account with deal entry as OUT or closing orders will be directed
to Slip_TEM
Parameter Value Description

2. EnTradeCopy
Configuration Guide →
1. Add a parameter in the "Centroid Gateway" for optimal settings.
2. Assign the configured "Centroid Gateway" to the "Slave Account" to establish a seamless connection.
EnTradeCopy Y The Parameter is enabled and it allows to send copy trades to the
“Slave Account”
EnTradeCopy N The Parameter is disabled
Parameter Value Explanation

3. EnReturnFillPolicy
4. Configuration of Limit Orders
EnReturnFillPolicy Y This parameter is pertinent to pending orders in MT5. When enabled, it
permits MT5 to resend the remaining volume in case of full or partial
order cancellation.
EnReturnFillPolicy N The Parameter is disabled, and the pending order will be cancelled.
Parameter Value Explanation

5. Limit Order Deviation Configuration
lmt Y: Yes (Send as a Limit Order)
Not specified (Send as a
Market Order)
Enabling the "lmt" parameter by setting it to "Y" facilitates the transmission of pending
orders, specifically Sell Limit and Buy Limit types, to the Bridge as Limit orders upon
activation.
Ordinarily, these order types are sent as Market orders by default.
Sample Rule: sec=*;g=Testonly\A-1;tem=TEM-1;lmt=Y
stp Y: Yes (Send as a Limit Order)
Not specified (Send as a
Market Order)
Enabling the "stp" parameter by setting it to "Y" enables the transmission of pending
orders, specifically Sell Stop and Buy Stop types, to the Aggregator as Limit orders upon
activation.
Ordinarily, these order types are sent as Market orders by default.
Sample Rule: sec=*;g=Testonly\A-1;tem=TEM-1;stp=Y
sl Y: Yes (Send as a Limit Order)
Not specified (Send as a
Market Order)
Enabling the "sl" parameter by setting it to "Y" enables the transmission of Stop Loss
triggered orders to the Aggregator as Limit orders upon activation.
Ordinarily, these order types are sent as Market orders by default.
Sample Rule: sec=*;g=Testonly\B-1;tem=TEM-1;sl=Y
tp Y: Yes (Send as a Limit Order)
Not specified (Send as a
Market Order)
Enabling the "tp" parameter by setting it to "Y" enables the transmission of Take Profit
triggered orders to the Aggregator as Limit orders upon activation.
Ordinarily, these order types are sent as Market orders by default.
Sample Rule: sec=*;g=Testonly\B-2;tem=TEM-1;tp=Y
Paramet
er
Value Explanation


6. Configuration to Force Price for Trading Accounts when a trade placed by a Manager

dev 10, 5, 7, 3 (In Points) Enabling the "dev" parameter by setting it to the desired value (in points), hence allowing
for the acceptance of deviation concerning Limit Orders. Deviation is consistently
measured in points. It's essential to note that for deviation to function, your limit
configurations must be in place; deviation operates in conjunction with Limit orders and
cannot function independently.
Parameter Value Explanation
ForceManagerPx Y: Yes (Manager can Force
Prices)
Not specified (Manager
cannot Force Prices)
Enabling the "ForceManagerPx" parameter by setting it to 'Y' grants authority to
managers listed in "ListForceManagerPx" to force prices against the current
market price for the trading accounts.
ListForceManagerPx 1012, 1013, 1015 The authority to force prices is exclusive to the manager number specified in
the "ListForceManagerPx" parameter.
Parameter Value Explanation

