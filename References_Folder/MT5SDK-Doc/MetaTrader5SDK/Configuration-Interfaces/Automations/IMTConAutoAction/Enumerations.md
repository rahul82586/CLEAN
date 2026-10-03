[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / Enumerations

[Previous](../IMTConAutoAction.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConAutoAction](../IMTConAutoAction.md) class contains the following enumerations:

  * [IMTConAutoAction::EnActions (#enactions)](Enumerations.md#enactions)



<a id="enactions"></a>
## IMTConAutoAction::EnActions (#enactions)

The IMTConAutoAction::EnActions enumeration contains the [actions](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) which are performed upon the triggering of an automation task.

ID | Value | Description  
ACTION_MESSAGE_PUSH | 0 | Send a push message.  
ACTION_MESSAGE_INTERNAL | 1 | Send a message by internal mail.  
ACTION_MESSAGE_SMS | 2 | Send an SMS message.  
ACTION_MESSAGE_EMAIL | 3 | Send a message by email.  
ACTION_MESSAGE_CHANNEL | 4 | Send a message to the selected channel via an instant messenger.  
ACTION_MESSAGE_JOURNAL | 5 | Send a message to the journal of the trading server on which the automation task is running.  
ACTION_MESSAGE_FIRST | 0 | Beginning of enumeration of [user notification (#message)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#message) actions.  
ACTION_MESSAGE_LAST | 1000 | End of enumeration of user notification actions.  
ACTION_ACCOUNT_DISABLE | 1001 | Disable account.  
ACTION_ACCOUNT_ENABLE | 1002 | Enable account.  
ACTION_ACCOUNT_DISABLE_TRADE | 1003 | Disable trading on the account.  
ACTION_ACCOUNT_ENABLE_TRADE | 1004 | Enable trading on the account.  
ACTION_ACCOUNT_DISABLE_EXPERT | 1005 | Disable the use of Expert Advisors on the account.  
ACTION_ACCOUNT_ENABLE_EXPERT | 1006 | Allow the use of Expert Advisors on the account.  
ACTION_ACCOUNT_DISABLE_TRAILING | 1007 | Disable the use of trailing stops in the client terminal for the account.  
ACTION_ACCOUNT_ENABLE_TRAILING | 1008 | Allow the use of trailing stops in the client terminal for the account.  
ACTION_ACCOUNT_FORCE_CHANGE_PASS | 1009 | Enable forced password change for the account during the next connection.  
ACTION_ACCOUNT_CHANGE_GROUP | 1010 | Change account group.  
ACTION_ACCOUNT_CHANGE_COLOR | 1011 | Change account color.  
ACTION_ACCOUNT_ARCHIVE | 1012 | Move the account to the archive.  
ACTION_ACCOUNT_COMMENT | 1013 | Add a comment to the account.  
ACTION_ACCOUNT_CLIENT_COMMENT | 1014 | Add a comment to the client.  
ACTION_ACCOUNT_LEVERAGE | 1015 | Change the account leverage.  
ACTION_ACCOUNT_ENABLE_REPORTS | 1016 | Allow the receipt of daily reports for the account.  
ACTION_ACCOUNT_DISABLE_REPORTS | 1017 | Disable the receipt of daily reports for the account.  
ACTION_ACCOUNT_ENABLE_VPS | 1018 | Enable the sponsored VPS option, i.e. allow the client to use hosting paid by the broker ([IMTUser::USER_RIGHT_SPONSORED_HOSTING (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).  
ACTION_ACCOUNT_DISABLE_VPS | 1019 | Disable the sponsored VPS option.  
ACTION_ACCOUNT_FIRST | 1001 | Beginning of enumeration of [account settings management (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account) actions.  
ACTION_ACCOUNT_LAST | 2000 | End of enumeration of account settings management actions.  
ACTION_FINANCE_DEPOSIT | 2001 | Deposit money.  
ACTION_FINANCE_BONUS | 2002 | Add bonus to to account.  
ACTION_FINANCE_CREDIT | 2003 | Add credit funds to the account.  
ACTION_FINANCE_DEPOSIT_PAYOFF | 2004 | Write off the entire account balance.  
ACTION_FINANCE_CREDIT_PAYOFF | 2005 | Write off all credit funds from the account.  
ACTION_FINANCE_BONUS_PERCENT | 2006 | Add a bonus as a percentage of the deposit amount.  
ACTION_FINANCE_BONUS_PAYOFF | 2007 | Remove all bonus funds from the account.  
ACTION_FINANCE_FIRST | 2001 | Beginning of enumeration of [account balance operation actions (#finance)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finance).  
ACTION_FINANCE_LAST | 3000 | End of enumeration of account balance operation actions.  
ACTION_TRADE_CLOSE_POSITIONS | 3001 | Close positions on the account.  
ACTION_TRADE_CLEAR_SL | 3002 | Clear Stop Loss levels of open positions and active pending orders.  
ACTION_TRADE_CLEAR_TP | 3003 | Clear Take Profit levels of open positions and active pending orders.  
ACTION_TRADE_CLEAR_SL_TP | 3004 | Clear Stop Loss and Take Profit levels of open positions and active pending orders.  
ACTION_TRADE_CLOSE_ORDERS | 4000 | Cancel pending orders on the account.  
ACTION_TRADE_FIRST | 3001 | Beginning of the enumeration of actions for [performing trading operation on accounts (#trading)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#trading).  
ACTION_TRADE_LAST | 5000 | End of the enumeration of actions for performing trading operation on accounts.  
ACTION_CONFIG_GROUP_UPDATE | 5001 | Update a [group configuration](../../Groups/IMTConGroup.md).  
ACTION_CONFIG_SYMBOL_UPDATE | 5002 | Update a [symbol configuration](../../Symbols/IMTConSymbol.md).  
ACTION_CONFIG_SYMBOL_MOVE | 5003 | Move a symbol in the list.  
ACTION_CONFIG_ROUTING_UPDATE | 5004 | Edit [routing rules](../../Routing/IMTConRoute.md).  
ACTION_CONFIG_SERVER_UPDATE | 5005 | Edit [server configuration](../../Network/IMTConServer.md).  
ACTION_CONFIG_GATEWAY_UPDATE | 5006 | Edit [gateway configuration](../../Gateways/IMTConGateway.md).  
ACTION_CONFIG_DATAFEED_UPDATE | 5007 | Edit [data feed configuration](../../Data-Feeds/IMTConFeeder.md).  
ACTION_CONFIG_FIRST | 5001 | Beginning of the enumeration of [platform settings management (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration) actions.  
ACTION_CONFIG_LAST | 6000 | End of the enumeration of platform settings management actions.  
ACTION_PLATFORM_RESTART_SERVER | 6001 | Restart the server.  
ACTION_PLATFORM_RESTART_FEED | 6002 | Restart data feeds.  
ACTION_PLATFORM_RESTART_GATEWAY | 6003 | Restart gateways.  
ACTION_PLATFORM_SYNC_HISTORY | 6004 | Start price data synchronization.  
ACTION_PLATFORM_LIVE_UPDATE | 6005 | Check and install platform updates.  
ACTION_PLATFORM_FIRST | 6001 | Beginning of the enumeration of [platform management (#platform)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#platform) actions.  
ACTION_PLATFORM_LAST | 7000 | End of the enumeration of platform management actions.  
ACTION_EXTERNAL_APPLICATION | 7001 | Running an external file.  
ACTION_EXTERNAL_PLUGIN | 7002 | Run a plugin. Currently not used.  
ACTION_EXTERNAL_HTTP_REQUEST | 7003 | Send a web request.  
ACTION_EXTERNAL_FINTEZA_EVENT | 7004 | Send an event to the Finteza analytics system.  
ACTION_EXTERNAL_FIRST | 7001 | Beginning of the enumeration of actions used for [platform integration with external systems (#external)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#external).  
ACTION_EXTERNAL_LAST | 8000 | End of the enumeration of actions for integrating the platform with external systems.  
ACTION_FIRST |  | Beginning of enumeration. Corresponds to ACTION_MESSAGE_FIRST.  
ACTION_LAST |  | End of enumeration. Corresponds to ACTION_EXTERNAL_LAST.  
  
This enumeration is used in the [IMTConAutoAction::Action](Action.md) method.
