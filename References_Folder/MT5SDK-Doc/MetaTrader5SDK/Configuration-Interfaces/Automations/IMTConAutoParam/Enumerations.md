[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / Enumerations

[Previous](../IMTConAutoParam.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConAutoParam](../IMTConAutoParam.md) class contains the following enumerations:

  * [IMTConAutoParam::EnParams (#enparams)](Enumerations.md#enparams)
  * [IMTConAutoParam::EnParamType (#enparamtype)](Enumerations.md#enparamtype)



<a id="enparams"></a>
## IMTConAutoAction::EnParams (#enparams)

The IMTConAutoAction::EnParams enumeration contains parameters of [actions](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) performed upon the triggering of automation tasks.

ID | Value | Description  
PARAM_ACTION_MESSAGE_PUSH_TO_LOGINS | 0 | List of accounts for sending Push messages.  
PARAM_ACTION_MESSAGE_PUSH_TO_GROUPS | 1 | List of groups for sending Push messages.  
PARAM_ACTION_MESSAGE_PUSH_TEXT | 2 | Text of the Push message to be sent.  
PARAM_ACTION_MESSAGE_PUSH_FIRST | 0 | Start of enumeration of action parameters related to [Push notification sending (#message)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#message).  
PARAM_ACTION_MESSAGE_PUSH_LAST | 50 | End of enumeration of action parameters related to Push notification sending.  
PARAM_ACTION_MESSAGE_INTERNAL_TO_LOGINS | 51 | List of accounts for sending messages by internal mail.  
PARAM_ACTION_MESSAGE_INTERNAL_TO_GROUPS | 52 | List of groups for sending messages by internal mail.  
PARAM_ACTION_MESSAGE_INTERNAL_SUBJ | 53 | Subject of the internal mail message.  
PARAM_ACTION_MESSAGE_INTERNAL_TEXT | 54 | Text of the internal mail message.  
PARAM_ACTION_MESSAGE_INTERNAL_FROM | 55 | Start of enumeration of action parameters related to [Push notification sending (#message)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#message).  
PARAM_ACTION_MESSAGE_INTERNAL_FIRST | 51 | Sender in the internal mail message.  
PARAM_ACTION_MESSAGE_INTERNAL_LAST | 100 | Start of enumeration of action parameters related to [internal mail sending (#message)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#message).  
PARAM_ACTION_MESSAGE_SMS_TO_LOGINS | 101 | End of enumeration of action parameters related to internal mail sending.  
PARAM_ACTION_MESSAGE_SMS_TO_GROUPS | 102 | List of groups for sending SMS.  
PARAM_ACTION_MESSAGE_SMS_TO_PHONES | 103 | List of phone numbers for sending SMS.  
PARAM_ACTION_MESSAGE_SMS_TEXT | 104 | Text of the SMS message.  
PARAM_ACTION_MESSAGE_SMS_FIRST | 101 | Start of enumeration of action parameters related to [SMS sending (#message)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#message).  
PARAM_ACTION_MESSAGE_SMS_LAST | 150 | End of enumeration of action parameters related to SMS sending.  
PARAM_ACTION_MESSAGE_EMAIL_TO_LOGINS | 151 | List of accounts for sending messages by email.  
PARAM_ACTION_MESSAGE_EMAIL_TO_GROUPS | 152 | List of groups for sending messages by email.  
PARAM_ACTION_MESSAGE_EMAIL_TO_EMAILS | 153 | List of addresses for sending messages by email.  
PARAM_ACTION_MESSAGE_EMAIL_SERVER | 154 | The name of the [mail server configuration](../../Mail-Servers/IMTConEmail.md), via which the message will be sent.   
PARAM_ACTION_MESSAGE_EMAIL_SUBJ | 155 | Subject of the email message.  
PARAM_ACTION_MESSAGE_EMAIL_TEXT | 156 | Text of the email message.  
PARAM_ACTION_MESSAGE_EMAIL_FIRST | 151 | Start of enumeration of action parameters related to [email sending (#message)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#message).  
PARAM_ACTION_MESSAGE_EMAIL_LAST | 200 | End of enumeration of action parameters related to email sending.  
PARAM_ACTION_ACCOUNT_CHANGE_GROUP | 201 | The group to which the specified accounts should be moved.  
PARAM_ACTION_ACCOUNT_CHANGE_GROUP_LOGINS | 202 | List of accounts to be moved to another group.  
PARAM_ACTION_ACCOUNT_CHANGE_GROUP_GROUPS | 203 | List of groups, accounts from which are to be moved to another group.  
PARAM_ACTION_ACCOUNT_CHANGE_GROUP_FIRST | 201 | Start of enumeration of action parameters related to [changing of an account group (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_CHANGE_GROUP_LAST | 205 | End of enumeration of action parameters related to account group changes.  
PARAM_ACTION_ACCOUNT_CHANGE_COLOR | 251 | The color to be set for the account.  
PARAM_ACTION_ACCOUNT_CHANGE_COLOR_LOGINS | 252 | List of accounts to change color.  
PARAM_ACTION_ACCOUNT_CHANGE_COLOR_GROUPS | 253 | List of groups, for accounts from which the color will be changed.  
PARAM_ACTION_ACCOUNT_CHANGE_COLOR_FIRST | 251 | Start of enumeration of action parameters related to [account color changes (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_CHANGE_COLOR_LAST | 300 | End of enumeration of action parameters related to account color changes.  
PARAM_ACTION_ACCOUNT_COMMENT | 301 | A comment to be added to the specified accounts.  
PARAM_ACTION_ACCOUNT_COMMENT_LOGINS | 302 | List of accounts for which a comment will be added.  
PARAM_ACTION_ACCOUNT_COMMENT_GROUPS | 303 | List of groups for accounts from which comments will be added.  
PARAM_ACTION_ACCOUNT_COMMENT_FIRST | 301 | Start of enumeration of action parameters related to [the addition of comments to accounts (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_COMMENT_LAST | 350 | End of enumeration of action parameters related to the addition of comments to accounts.  
PARAM_ACTION_ACCOUNT_CLIENT_COMMENT | 351 | A comment to be added to the specified clients.  
PARAM_ACTION_ACCOUNT_CLIENT_COMMENT_LOGINS | 352 | List of accounts for [client records](../../../Database-Interfaces/Clients/IMTClient.md)of which comments will be added.  
PARAM_ACTION_ACCOUNT_CLIENT_COMMENT_GROUPS | 353 | List of groups, for clients from which comments will be added (determined by [IMTClient::TradingGroup](../../../Database-Interfaces/Clients/IMTClient/TradingGroup.md)).  
PARAM_ACTION_CLIENT_COMMENT_FIRST | 351 | Start of enumeration of action parameters related to [the addition of comments to clients (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_CLIENT_COMMENT_LAST | 400 | End of enumeration of action parameters related to the addition of comments to clients.  
PARAM_ACTION_FINANCE_DEPOSIT_AMOUNT | 401 | The amount of the balance operation to be performed on the account. Indicate a positive amount to add funds and a negative value to deduct the appropriate amount.  
PARAM_ACTION_FINANCE_DEPOSIT_COMMENT | 402 | A comment to the deposit operation.  
PARAM_ACTION_FINANCE_DEPOSIT_LOGINS | 403 | List of accounts to add deposit.  
PARAM_ACTION_FINANCE_DEPOSIT_GROUPS | 404 | List of groups, for accounts from which the deposit operation will be performed.  
PARAM_ACTION_FINANCE_DEPOSIT_ACTION | 405 | The type of the balance operation to be performed on the account.  
PARAM_ACTION_FINANCE_DEPOSIT_FIRST | 401 | Start of enumeration of action parameters related to [account balance deposit (#finance)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finance).  
PARAM_ACTION_FINANCE_DEPOSIT_LAST | 450 | End of enumeration of action parameters related to account balance deposit.  
PARAM_ACTION_FINANCE_BONUS_AMOUNT | 451 | The amount of bonus adding/deducting operation. Indicate a positive amount to add a bonus and a negative value to deduct the appropriate amount.  
PARAM_ACTION_FINANCE_BONUS_COMMENT | 452 | Comment on the operation.  
PARAM_ACTION_FINANCE_BONUS_LOGINS | 453 | List of accounts for the operation.  
PARAM_ACTION_FINANCE_BONUS_GROUPS | 454 | List of groups, for accounts from which the operation will be performed.  
PARAM_ACTION_FINANCE_BONUS_FIRST | 451 | Start of enumeration of action parameters related to [bonus adding/deducting operation (#finance)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finance).  
PARAM_ACTION_FINANCE_BONUS_LAST | 500 | End of enumeration of action parameters related to bonus adding/deducting operation.  
PARAM_ACTION_FINANCE_CREDIT_AMOUNT | 501 | The amount of credit adding/deducting operation. Indicate a positive amount to add a credit and a negative value to deduct the appropriate amount.  
PARAM_ACTION_FINANCE_CREDIT_COMMENT | 502 | Comment on the operation.  
PARAM_ACTION_FINANCE_CREDIT_LOGINS | 503 | List of accounts for the operation.  
PARAM_ACTION_FINANCE_CREDIT_GROUPS | 504 | List of groups, for accounts from which the operation will be performed.  
PARAM_ACTION_FINANCE_CREDIT_FIRST | 501 | Start of enumeration of action parameters related to [credit adding/deducting operation (#finance)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finance).  
PARAM_ACTION_FINANCE_CREDIT_LAST | 550 | End of enumeration of action parameters related to credit adding/deducting operation.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_TYPES | 551 | Type of positions to be closed.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_SYMBOLS | 552 | Financial instrument for which positions will be closed.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_PRICE | 553 | Price at which positions will be closed.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_COMMENT | 554 | Comment to deals by which the positions will be closed.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_LOGINS | 555 | List of accounts on which positions will be closed.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_GROUPS | 556 | List of accounts on which positions will be closed.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_REASON | 557 | Operation execution reason to be specified in position closing deals. This parameter enables more accurate details in the database of deals. For example, if your automation task closes positions on Stop Out, then you can specify the relevant reason in the deals. Only [IMTDeal::EnDealReason (#endealreason)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealreason) values are allowed:

  * DEAL_REASON_DEALER (default) 
  * DEAL_REASON_SO 
  * DEAL_REASON_ROLLOVER 
  * DEAL_REASON_SETTLEMENT
  * DEAL_REASON_TRANSFER

  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_TRIGGER_LOGIN | 558 | The action is applied to the account on which the trigger was activated.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_TRIGGER_POSITION | 559 | Position from trigger. This option is available for the [IMTConAutomation::TRIGGER_SCHEDULE_POSITIONS (#entriggers)](../IMTConAutomation/Enumerations.md#entriggers) trigger. In this case, the action is applied to all positions which match the conditions specified for the automation task. For example, the trigger is combined with the condition "Position\Days since creation > 365". By selecting condition IMTConAutoAction::ACTION_TRADE_CLOSE_POSITIONS along with this parameter, you can close all positions that were opened more than a year ago.  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_FIRST | 551 | Start of enumeration of action parameters related to [position closing (#trading)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#trading).  
PARAM_ACTION_TRADE_CLOSE_POSITIONS_LAST | 600 | End of enumeration of action parameters related to position closing.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_TYPES | 601 | Type of orders to be canceled.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_SYMBOLS | 602 | Financial instrument for which orders will be canceled.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_COMMENT | 603 | A comment that is added to the orders being canceled.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_LOGINS | 604 | List of accounts on which orders will be canceled.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_GROUPS | 605 | List of groups on accounts from which orders will be canceled.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_FIRST | 601 | Start of enumeration of action parameters related to [order canceling (#trading)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#trading).  
PARAM_ACTION_TRADE_CLOSE_ORDERS_TRIGGER_LOGIN | 606 | The action is applied to the account on which the trigger was activated.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_TRIGGER_ORDER | 607 | Order from trigger. This option is available for the [IMTConAutomation::TRIGGER_SCHEDULE_ORDERS (#entriggers)](../IMTConAutomation/Enumerations.md#entriggers) trigger. In this case, the action is applied to all orders which match the conditions specified for the automation task. For example, the trigger is combined with the condition "Order\Days since Setup > 365". By selecting condition IMTConAutoAction::ACTION_TRADE_CLOSE_ORDERS along with this parameter, you can cancel all orders that were opened more than a year ago.  
PARAM_ACTION_TRADE_CLOSE_ORDERS_LAST | 650 | End of enumeration of action parameters related to order canceling.  
PARAM_ACTION_CONFIG_SYMBOL_MOVE_PATH | 651 | [Path](../../Symbols/IMTConSymbol/Path.md) for moving a symbol.  
PARAM_ACTION_CONFIG_SYMBOL_MOVE_FIRST | 651 | Start of enumeration of action parameters related to [symbol moving (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration).  
PARAM_ACTION_CONFIG_SYMBOL_MOVE_LAST | 700 | End of enumeration of action parameters related to symbol moving.  
PARAM_ACTION_PLATFORM_RESTART_SERVER_LOGIN | 701 | [ID of the server](../../Network/IMTConServer/Id.md) to restart.  
PARAM_ACTION_PLATFORM_RESTART_SERVER_FIRST | 701 | Start of enumeration of action parameters related to [server restart (#platform)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#platform).  
PARAM_ACTION_PLATFORM_RESTART_SERVER_LAST | 750 | End of enumeration of action parameters related to server restart.  
PARAM_ACTION_PLATFORM_RESTART_FEED_NAME | 751 | The [name](../../Data-Feeds/IMTConFeeder/Name.md) of the datafeed to restart.  
PARAM_ACTION_PLATFORM_RESTART_FEED_FIRST | 751 | Start of enumeration of action parameters related to [datafeed restart (#platform)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#platform).  
PARAM_ACTION_PLATFORM_RESTART_FEED_LAST | 800 | End of enumeration of action parameters related to datafeed restart.  
PARAM_ACTION_PLATFORM_RESTART_GATEWAY_NAME | 801 | The [name](../../Gateways/IMTConGateway/Name.md) of the gateway to restart.  
PARAM_ACTION_PLATFORM_RESTART_GATEWAY_FIRST | 820 | Start of enumeration of action parameters related to [gateway restart (#platform)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#platform).  
PARAM_ACTION_PLATFORM_RESTART_GATEWAY_LAST | 850 | End of enumeration of action parameters related to gateway restart.  
PARAM_ACTION_CONFIG_GROUP_UPDATE_JSON | 851 | Updated group description in JSON format.  
PARAM_ACTION_CONFIG_GROUP_UPDATE_FIRST | 851 | Start of enumeration of action parameters related to [group change (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration).  
PARAM_ACTION_CONFIG_GROUP_UPDATE_LAST | 900 | End of enumeration of action parameters related to group change.  
PARAM_ACTION_CONFIG_SYMBOL_UPDATE_JSON | 901 | Updated symbol description in JSON format.  
PARAM_ACTION_CONFIG_SYMBOL_UPDATE_FIRST | 901 | Start of enumeration of action parameters related to [symbol change (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration).  
PARAM_ACTION_CONFIG_SYMBOL_UPDATE_LAST | 950 | End of enumeration of action parameters related to symbol change.  
PARAM_ACTION_CONFIG_ROUTING_UPDATE_JSON | 951 | Updated description of a routing rule in JSON format.  
PARAM_ACTION_CONFIG_ROUTING_UPDATE_FIRST | 951 | Start of enumeration of action parameters related to [routing rule changes (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration).  
PARAM_ACTION_CONFIG_ROUTING_UPDATE_LAST | 1000 | End of enumeration of action parameters related to routing rule changes.  
PARAM_ACTION_ACCOUNT_DISABLE_LOGINS | 1001 | List of accounts to be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_GROUPS | 1002 | List of groups, accounts in which will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_FIRST | 1001 | Start of enumeration of action parameters related to [account enabling/disabling (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_DISABLE_LAST | 1050 | End of enumeration of action parameters related to account enabling/disabling.  
PARAM_ACTION_ACCOUNT_ENABLE_LOGINS | 1051 | List of accounts to be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_GROUPS | 1052 | List of groups, accounts in which will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_FIRST | 1051 | Start of enumeration of action parameters related to [account enabling/disabling (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_ENABLE_LAST | 1110 | End of enumeration of action parameters related to account enabling/disabling.  
PARAM_ACTION_ACCOUNT_DISABLE_TRADE_LOGINS | 1101 | List of accounts for which trading will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_TRADE_GROUPS | 1102 | List of groups for accounts from which trading will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_TRADE_FIRST | 1101 | Start of enumeration of action parameters related to [trading enabling/disabling on accounts (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_DISABLE_TRADE_LAST | 1150 | End of enumeration of action parameters related to trading enabling/disabling on accounts.  
PARAM_ACTION_ACCOUNT_ENABLE_TRADE_LOGINS | 1151 | List of accounts for which trading will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_TRADE_GROUPS | 1152 | List of groups for accounts from which trading will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_TRADE_FIRST | 1151 | Start of enumeration of action parameters related to [trading enabling/disabling on accounts (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_ENABLE_TRADE_LAST | 1200 | End of enumeration of action parameters related to trading enabling/disabling on accounts.  
PARAM_ACTION_ACCOUNT_DISABLE_EXPERT_LOGINS | 1201 | List of accounts for which trading using Expert Advisors will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_EXPERT_GROUPS | 1202 | List of groups for accounts from which trading using Expert Advisors will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_EXPERT_FIRST | 1201 | Start of enumeration of action parameters related to [enabling/disabling of trading using Expert Advisors on accounts (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_DISABLE_EXPERT_LAST | 1250 | End of enumeration of action parameters related to enabling/disabling of trading using Expert Advisors on accounts.  
PARAM_ACTION_ACCOUNT_ENABLE_EXPERT_LOGINS | 1251 | List of accounts for which trading using Expert Advisors will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_EXPERT_GROUPS | 1252 | List of groups for accounts from which trading using Expert Advisors will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_EXPERT_FIRST | 1251 | Start of enumeration of action parameters related to [enabling/disabling of trading using Expert Advisors on accounts (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_ENABLE_EXPERT_LAST | 1300 | End of enumeration of action parameters related to enabling/disabling of trading using Expert Advisors on accounts.  
PARAM_ACTION_ACCOUNT_DISABLE_TRAILING_LOGINS | 1301 | List of accounts for which the use of trailing stop in client terminals will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_TRAILING_GROUPS | 1302 | List of groups for accounts from which the use of trailing stop in client terminals will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_TRAILING_FIRST | 1301 | Start of enumeration of action parameters related to [enabling/disabling the use of trailing stop in client terminals (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_DISABLE_TRAILING_LAST | 1350 | End of enumeration of action parameters related to enabling/disabling the use of trailing stop in client terminals.  
PARAM_ACTION_ACCOUNT_ENABLE_TRAILING_LOGINS | 1351 | List of accounts for which the use of trailing stop in client terminals will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_TRAILING_GROUPS | 1352 | List of groups for accounts from which the use of trailing stop in client terminals will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_TRAILING_FIRST | 1351 | Start of enumeration of action parameters related to [enabling/disabling the use of trailing stop in client terminals (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_ENABLE_TRAILING_LAST | 1400 | End of enumeration of action parameters related to enabling/disabling the use of trailing stop in client terminals.  
PARAM_ACTION_ACCOUNT_FORCE_CHANGE_PASS_LOGINS | 1401 | List of accounts for which forced password change will be enabled during the next connection.  
PARAM_ACTION_ACCOUNT_FORCE_CHANGE_PASS_GROUPS | 1402 | List of groups for accounts from which forced password change will be enabled during the next connection.  
PARAM_ACTION_ACCOUNT_FORCE_CHANGE_PASS_FIRST | 1401 | Start of enumeration of action parameters related to [forced password change (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_FORCE_CHANGE_PASS_LAST | 1450 | End of enumeration of action parameters related to forced password change.  
PARAM_ACTION_ACCOUNT_ARCHIVE_LOGINS | 1451 | List of accounts to be moved to archive.  
PARAM_ACTION_ACCOUNT_ARCHIVE_GROUPS | 1452 | List of groups accounts from which will be moved to archive.  
PARAM_ACTION_ACCOUNT_ARCHIVE_FIRST | 1451 | Start of enumeration of action parameters related to [account moving to archive (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_ARCHIVE_LAST | 1500 | End of enumeration of action parameters related to account moving to archive.  
PARAM_ACTION_ACCOUNT_LEVERAGE | 1501 | Leverage to be set for the specified accounts.  
PARAM_ACTION_ACCOUNT_LEVERAGE_LOGINS | 1502 | List of accounts for which leverage will be changed.  
PARAM_ACTION_ACCOUNT_LEVERAGE_GROUPS | 1503 | List of groups, for accounts from which leverage will be changed.  
PARAM_ACTION_ACCOUNT_LEVERAGE_FIRST | 1501 | Start of enumeration of action parameters related to [leverage change (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_LEVERAGE_LAST | 1550 | End of enumeration of action parameters related to leverage change.  
PARAM_ACTION_FINANCE_DEPOSIT_PAYOFF_LOGINS | 1551 | List of accounts for which the entire balance will be written off.  
PARAM_ACTION_FINANCE_DEPOSIT_PAYOFF_GROUPS | 1552 | List of groups for accounts from which the entire balance will be written off.  
PARAM_ACTION_FINANCE_DEPOSIT_PAYOFF_COMMENT | 1553 | Comment to a deal by which the balance will be written off.  
PARAM_ACTION_FINANCE_DEPOSIT_PAYOFF_ACTION | 1554 | Type of the deal by which the balance will be written off.  
PARAM_ACTION_FINANCE_DEPOSIT_PAYOFF_FIRST | 1551 | Start of enumeration of action parameters related to [balance write-off (#finance)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finance).  
PARAM_ACTION_FINANCE_DEPOSIT_PAYOFF_LAST | 1600 | End of enumeration of action parameters related to balance write-off.  
PARAM_ACTION_FINANCE_CREDIT_PAYOFF_LOGINS | 1601 | List of accounts for which the entire credit amount will be written off.  
PARAM_ACTION_FINANCE_CREDIT_PAYOFF_GROUPS | 1602 | List of groups for accounts from which the entire credit amount will be written off.  
PARAM_ACTION_FINANCE_CREDIT_PAYOFF_COMMENT | 1603 | Comments for the deal by which the credit will be written off.  
PARAM_ACTION_FINANCE_CREDIT_PAYOFF_FIRST | 1601 | Start of enumeration of action parameters related to [credit write-off (#finance)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finance).  
PARAM_ACTION_FINANCE_CREDIT_PAYOFF_LAST | 1650 | End of enumeration of action parameters related to credit write-off.  
PARAM_ACTION_EXTERNAL_HTTP_REQUEST_METHOD | 1651 | Type of web request.  
PARAM_ACTION_EXTERNAL_HTTP_REQUEST_URL | 1652 | URL to which the web request will be sent.  
PARAM_ACTION_EXTERNAL_HTTP_REQUEST_HEADERS | 1653 | Web request headers.  
PARAM_ACTION_EXTERNAL_HTTP_REQUEST_DATA | 1654 | The body of the POST request.  
PARAM_ACTION_EXTERNAL_HTTP_REQUEST_FIRST | 1651 | Beginning of enumeration of action parameters related to [web request sending (#webrequest)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#webrequest).  
PARAM_ACTION_EXTERNAL_HTTP_REQUEST_LAST | 1700 | End of enumeration of action parameters related to web request sending.  
PARAM_ACTION_EXTERNAL_FINTEZA_EVENT_NAME | 1701 | The name of the event to be sent to Finteza.  
PARAM_ACTION_EXTERNAL_FINTEZA_EVENT_VALUE | 1702 | The value of the event to be sent to Finteza.  
PARAM_ACTION_EXTERNAL_FINTEZA_EVENT_UNIT | 1703 | Units of measurement for the value sent to Finteza.  
PARAM_ACTION_EXTERNAL_FINTEZA_EVENT_FIRST | 1701 | Beginning of enumeration of action parameters related to [event sending to the Finteza analytics system (#finteza)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finteza).  
PARAM_ACTION_EXTERNAL_FINTEZA_EVENT_LAST | 1750 | End of enumeration of action parameters related to event sending to the Finteza analytics system.  
PARAM_ACTION_EXTERNAL_APPLICATION_PATH | 1751 | Path to the file to run.  
PARAM_ACTION_EXTERNAL_APPLICATION_CMD | 1752 | Command line arguments to run the file with.  
PARAM_ACTION_EXTERNAL_APPLICATION_FIRST | 1751 | Beginning of enumeration of action parameters related to [external file run (#external)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#external).  
PARAM_ACTION_EXTERNAL_APPLICATION_LAST | 1800 | End of enumeration of action parameters related to external file run.  
PARAM_ACTION_CONFIG_SERVER_UPDATE_JSON | 1801 | Updated server description in JSON format.  
PARAM_ACTION_CONFIG_SERVER_UPDATE_ORIGINAL | 1802 | A JSON description of only those server parameters that will be changed.  
PARAM_ACTION_CONFIG_SERVER_UPDATE_FIRST | 1801 | Beginning of enumeration of action parameters related to [server configuration changes (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration).  
PARAM_ACTION_CONFIG_SERVER_UPDATE_LAST | 1900 | End of enumeration of action parameters related to server configuration changes.  
PARAM_ACTION_CONFIG_GATEWAY_UPDATE_JSON | 1901 | Updated gateway description in JSON format.  
PARAM_ACTION_CONFIG_GATEWAY_UPDATE_FIRST | 1901 | Beginning of enumeration of action parameters related to [gateway configuration changes (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration).  
PARAM_ACTION_CONFIG_GATEWAY_UPDATE_LAST | 2000 | End of enumeration of action parameters related to gateway configuration changes.  
PARAM_ACTION_CONFIG_DATAFEED_UPDATE_JSON | 2001 | Updated Data feed description in JSON format.  
PARAM_ACTION_CONFIG_DATAFEED_UPDATE_FIRST | 2001 | Beginning of enumeration of action parameters related to [data feed configuration changes (#configuration)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#configuration).  
PARAM_ACTION_CONFIG_DATAFEED_UPDATE_LAST | 2100 | End of enumeration of action parameters related to data feed configuration changes.  
PARAM_ACTION_FINANCE_BONUS_PERCENT_AMOUNT | 2101 | Accrued bonus as a percentage.  
PARAM_ACTION_FINANCE_BONUS_PERCENT_COMMENT | 2102 | Comment for the deal by which the bonus will be accrued.  
PARAM_ACTION_FINANCE_BONUS_PERCENT_LOGINS | 2103 | List of logins to which the bonus will be accrued.  
PARAM_ACTION_FINANCE_BONUS_PERCENT_GROUPS | 2104 | List of groups to which the bonus will be accrued.  
PARAM_ACTION_FINANCE_BONUS_PERCENT_FIRST | 2101 | Beginning of enumeration of action parameters related to [percentage bonus accrual (#finance)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#finance).  
PARAM_ACTION_FINANCE_BONUS_PERCENT_LAST | 2200 | End of enumeration of action parameters related to percentage bonus accrual.  
PARAM_ACTION_TRADE_CLEAR_SL_LOGINS | 2201 | List of logins, for which clearing of Stop Loss levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_SL_GROUPS | 2202 | List of groups, for which clearing of Stop Loss levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_SL_SYMBOLS | 2203 | List of symbols, for which clearing of Stop Loss levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_SL_TRIGGER_LOGIN | 2204 | List of logins, for which clearing of Stop Loss levels in trading operations will be enabled, is determined by the trigger.  
PARAM_ACTION_TRADE_CLEAR_SL_TRIGGER_ENTITY | 2205 | List of positions or orders, for which Stop Loss levels will be cleared, is determined by the trigger. This option is available if IMTConAutomation::TRIGGER_SCHEDULE_POSITIONS or IMTConAutomation::TRIGGER_SCHEDULE_ORDERS is used as the trigger.  
PARAM_ACTION_TRADE_CLEAR_TP_FIRST | 2201 | Beginning of enumeration of action parameters related to the [clearing of Stop Loss levels (#trading)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#trading).  
PARAM_ACTION_TRADE_CLEAR_TP_LAST | 2300 | End of enumeration of action parameters related to the clearing of Stop Loss levels.  
PARAM_ACTION_TRADE_CLEAR_TP_LOGINS | 2301 | List of logins, for which clearing of Take Profit levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_TP_GROUPS | 2302 | List of groups, for which clearing of Take Profit levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_TP_SYMBOLS | 2303 | List of symbols, for which clearing of Take Profit levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_TP_TRIGGER_LOGIN | 2304 | List of logins, for which clearing of Take Profit levels in trading operations will be enabled, is determined by the trigger.  
PARAM_ACTION_TRADE_CLEAR_TP_TRIGGER_ENTITY | 2305 | List of positions or orders, for which Take Profit levels will be cleared, is determined by the trigger. This option is available if IMTConAutomation::TRIGGER_SCHEDULE_POSITIONS or IMTConAutomation::TRIGGER_SCHEDULE_ORDERS is used as the trigger.  
PARAM_ACTION_TRADE_CLEAR_TP_FIRST | 2301 | Beginning of enumeration of action parameters related to the [clearing of Take Profit levels (#trading)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#trading).  
PARAM_ACTION_TRADE_CLEAR_TP_LAST | 2400 | End of enumeration of action parameters related to the clearing of Take Profit levels.  
PARAM_ACTION_TRADE_CLEAR_SL_TP_LOGINS | 2401 | List of logins, for which clearing of Stop Loss and Take Profit levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_SL_TP_GROUPS | 2402 | List of groups, for which clearing of Stop Loss and Take Profit levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_SL_TP_SYMBOLS | 2403 | List of symbols, for which clearing of Stop Loss and Take Profit levels in trading operations will be enabled.  
PARAM_ACTION_TRADE_CLEAR_SL_TP_TRIGGER_LOGIN | 2404 | List of logins, for which clearing of Stop Loss and Take Profit levels in trading operations will be enabled, is determined by the trigger.  
PARAM_ACTION_TRADE_CLEAR_SL_TP_TRIGGER_ENTITY | 2405 | List of positions or orders, for which Take Profit and Stop Loss levels will be cleared, is determined by the trigger. This option is available if IMTConAutomation::TRIGGER_SCHEDULE_POSITIONS or IMTConAutomation::TRIGGER_SCHEDULE_ORDERS is used as the trigger.  
PARAM_ACTION_TRADE_CLEAR_SL_TP_FIRST | 2401 | Beginning of enumeration of action parameters related to the [clearing of Take Profit and Stop Loss levels (#trading)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#trading).  
PARAM_ACTION_TRADE_CLEAR_SL_TP_LAST | 2500 | End of enumeration of action parameters related to the clearing of Take Profit and Stop Loss levels.  
PARAM_ACTION_ACCOUNT_ENABLE_REPORTS_LOGINS | 2501 | List of accounts for which the ability to receive daily reports will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_REPORTS_GROUPS | 2502 | List of groups, for accounts in which the ability to receive daily reports will be enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_REPORTS_FIRST | 2501 | Beginning of enumeration of action parameters related to [enabling the ability to receive daily reports (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_ENABLE_REPORTS_LAST | 2600 | End of enumeration of action parameters related to enabling the ability to receive daily reports.  
PARAM_ACTION_ACCOUNT_DISABLE_REPORTS_LOGINS | 2601 | List of accounts for which the ability to receive daily reports will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_REPORTS_GROUPS | 2602 | List of groups, for accounts in which the ability to receive daily reports will be disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_REPORTS_FIRST | 2601 | Beginning of enumeration of action parameters related to [disabling the ability to receive daily reports (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_DISABLE_REPORTS_LAST | 2700 | End of enumeration of action parameters related to disabling the ability to receive daily reports.  
PARAM_ACTION_MESSAGE_CHANNEL_CHANNEL | 2701 | The name of the channel in which the message will be posted.  
PARAM_ACTION_MESSAGE_CHANNEL_TEXT | 2702 | The message text to post to the channel.  
PARAM_ACTION_MESSAGE_CHANNEL_FIRST | 2701 | Beginning of enumeration of action parameters related to the [sending of messages to a channel (#message)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#message) via the messenger.  
PARAM_ACTION_MESSAGE_CHANNEL_LAST | 2800 | End of enumeration of action parameters related to the sending of messages to a channel via the messenger.  
PARAM_ACTION_ACCOUNT_ENABLE_VPS_LOGINS | 2801 | List of logins for which the sponsored VPS is enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_VPS_GROUPS | 2802 | List of groups for which the sponsored VPS is enabled.  
PARAM_ACTION_ACCOUNT_ENABLE_VPS_FIRST | 2801 | Beginning of enumeration of action parameters related to the [enabling of the sponsored VPS option (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_ENABLE_VPS_LAST | 2900 | End of enumeration of action parameters related to the enabling of the sponsored VPS option.  
PARAM_ACTION_ACCOUNT_DISABLE_VPS_LOGINS | 2901 | List of logins for which the sponsored VPS is disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_VPS_GROUPS | 2902 | List of groups for which the sponsored VPS is disabled.  
PARAM_ACTION_ACCOUNT_DISABLE_VPS_FIRST | 2901 | Beginning of enumeration of action parameters related to the [disabling of the sponsored VPS option (#account)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action#account).  
PARAM_ACTION_ACCOUNT_DISABLE_VPS_LAST | 3000 | End of enumeration of action parameters related to the disabling of the sponsored VPS option.  
PARAM_ACTION_FINANCE_BONUS_PAYOFF_LOGINS | 3001 | List of accounts for which bonus funds will be completely removed.  
PARAM_ACTION_FINANCE_BONUS_PAYOFF_GROUPS | 3002 | List of groups for accounts from which bonus funds will be completely removed.  
PARAM_ACTION_FINANCE_BONUS_PAYOFF_COMMENT | 3003 | Comment for the deal by which the bonus funds will be written off.  
PARAM_ACTION_FINANCE_BONUS_PAYOFF_FIRST | 3001 | Start of enumeration of action parameters related to [bonus removal (#finance)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/automation/automation_action#finance).  
PARAM_ACTION_FINANCE_BONUS_PAYOFF_LAST | 3100 | End of enumeration of action parameters related to bonus removal.  
PARAM_ACTION_MESSAGE_JOURNAL_TEXT | 3101 | Text to be written to the trading server log.  
PARAM_ACTION_MESSAGE_JOURNAL_FIRST | 3101 | Beginning of enumeration of action parameters related to [sending messages to the journal (#message)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/automation/automation_action#message).  
PARAM_ACTION_MESSAGE_JOURNAL_LAST | 3200 | End of enumeration of action parameters related to sending messages to the journal.  
PARAM_FIRST |  | Beginning of enumeration. Corresponds to PARAM_ACTION_MESSAGE_PUSH_TO_LOGINS.  
PARAM_LAST |  | End of enumeration. Corresponds to PARAM_ACTION_MESSAGE_JOURNAL_LAST.  
  
The enumeration is used in the [IMTConAutoParam::Param](Param.md) method.

<a id="enparamtype"></a>
## IMTConAutoParam::EnParamType (#enparamtype)

Parameter types are enumerated in IMTConAutoParam::EnParamType.

ID | Value | Description  
TYPE_NONE | 0 | Parameter is not specified.  
TYPE_STRING | 1 | The parameter is of the string type.  
TYPE_INT | 2 | The parameter is of the int type.  
TYPE_UINT | 3 | The parameter is of the uint type.  
TYPE_FLOAT | 4 | The parameter is of the float type.  
TYPE_COLOR | 5 | The parameter is of the color type.  
TYPE_MONEY | 6 | The parameter sets the amount of money.  
TYPE_VOLUME | 7 | The parameter sets the volume.  
TYPE_DATETIME | 8 | The parameter sets date and time (in seconds elapsed since 01.01.1970).  
TYPE_LEVERAGE | 9 | The parameter sets the leverage.  
TYPE_BOOL | 10 | The parameter sets the bool type.  
TYPE_TIME | 11 | The parameter sets time (in minutes since 00:00).  
TYPE_DATE | 12 | The parameter sets the day.  
TYPE_PERCENT | 13 | The parameter sets the percentage.  
TYPE_LANGUAGE | 14 | The parameter sets the language.  
TYPE_SERVER | 15 | The parameter sets a [server property](../../Network/IMTConServer.md).  
TYPE_HTML | 16 | The parameter sets the HTML content.  
TYPE_FIRST |  | Beginning of enumeration. Corresponds to TYPE_NONE.  
TYPE_LAST |  | End of enumeration. Corresponds to TYPE_HTML.  
  
The enumeration is used in the [IMTConAutoParam::ValueType](ValueType.md) method.
