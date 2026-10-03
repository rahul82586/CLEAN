[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / Enumerations

[Previous](../IMTConAutoCondition.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConAutoCondition](../IMTConAutoCondition.md) class contains the following enumerations:

  * [IMTConAutoCondition::EnConditions (#enconditions)](Enumerations.md#enconditions)
  * [IMTConAutoCondition::EnConditionRule (#enconditionrule)](Enumerations.md#enconditionrule)
  * [IMTConAutoCondition::EnConditionType (#enconditiontype)](Enumerations.md#enconditiontype)



<a id="enconditions"></a>
## IMTConAutoCondition::EnConditions (#enconditions)

The IMTConAutoCondition::EnConditions enumeration contains [conditions](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition) for triggering automation tasks.

ID number | Value | Description  
CONDITION_DATETIME_DATETIME | 0 | Date and time.  
CONDITION_DATETIME_DATE | 1 | Date.  
CONDITION_DATETIME_TIME | 2 | Time  
CONDITION_DATETIME_FIRST | 0 | Beginning of enumeration of conditions by date and time.  
CONDITION_DATETIME_LAST | 1000 | End of enumeration of conditions by date and time.  
CONDITION_ACCOUNT_LOGIN | 1001 | Account number.  
CONDITION_ACCOUNT_GROUP | 1002 | Group name.  
CONDITION_ACCOUNT_COUNTRY | 1003 | Account owner country.  
CONDITION_ACCOUNT_CITY | 1004 | Account owner city.  
CONDITION_ACCOUNT_LANGUAGE | 1005 | Account owner language.  
CONDITION_ACCOUNT_PHONE | 1006 | Account owner phone number.  
CONDITION_ACCOUNT_EMAIL | 1007 | Account owner email address.  
CONDITION_ACCOUNT_COLOR | 1008 | Account color.  
CONDITION_ACCOUNT_COMMENT | 1009 | Comment to the account.  
CONDITION_ACCOUNT_REGISTRATION | 1010 | The date of account creation in the platform.  
CONDITION_ACCOUNT_LASTTIME | 1011 | The date of the last account connection to the server.  
CONDITION_ACCOUNT_LEVERAGE | 1012 | Account leverage  
CONDITION_ACCOUNT_BALANCE | 1013 | Account balance.  
CONDITION_ACCOUNT_CREDIT | 1014 | Credit funds on the account.  
CONDITION_ACCOUNT_POSITIONS | 1015 | The amount of open positions on the account.  
CONDITION_ACCOUNT_ORDERS | 1016 | The number of active pending orders on the account.  
CONDITION_ACCOUNT_PROFIT | 1017 | Floating profit on the account.  
CONDITION_ACCOUNT_EQUITY | 1018 | Account equity.  
CONDITION_ACCOUNT_MARGIN | 1019 | Reserved margin on the account.  
CONDITION_ACCOUNT_MARGIN_FREE | 1020 | Free margin on the account.  
CONDITION_ACCOUNT_MARGIN_LEVEL | 1021 | Account margin level.  
CONDITION_ACCOUNT_CURRENCY | 1022 | Account deposit currency.  
CONDITION_ACCOUNT_REGISTRATION_ELAPSED | 1023 | The number of days that have elapsed since account creation.  
CONDITION_ACCOUNT_LASTTIME_ELAPSED | 1024 | The number of days that have elapsed since the last connection to the account.  
CONDITION_ACCOUNT_LEAD_SOURCE | 1025 | Lead source specified in the account.  
CONDITION_ACCOUNT_LEAD_CAMPAIGN | 1026 | Lead campaign specified in the account.  
CONDITION_ACCOUNT_ONLINE | 1027 | Status of account connection to the trade server: "true" — connected, "false" — not connected.  
CONDITION_ACCOUNT_ACTIVITY_TRADE_ELAPSED | 1028 | The number of days since the last trading operation on the account. Any operations are checked: trading, balance, commission accrual, etc. In addition, the system checks if the account has any open positions or active pending orders.  
CONDITION_ACCOUNT_ENABLED | 1029 | Account status: enabled or disabled ([IMTUser::USER_RIGHT_ENABLED (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).  
CONDITION_ACCOUNT_TRADING_ENABLED | 1030 | Permission for an account to trade ([IMTUser::USER_RIGHT_TRADE_DISABLED (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).  
CONDITION_ACCOUNT_EXPERT_ENABLED | 1031 | Permission to trade using EAs ([IMTUser::USER_RIGHT_EXPERT (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).  
CONDITION_ACCOUNT_OWN_FUNDS_PERCENT | 1032 | The share of the client's own funds, i.e. of the money the client has deposited to the trading account. The calculation equation: (1 - (Credit / Equity)) * 100.  
CONDITION_ACCOUNT_OWN_FUNDS_VOLUME | 1033 | Client's own funds, i.e. the money the client has deposited to the trading account. The calculation equation: Equity - Credit.  
CONDITION_ACCOUNT_AGENT | 1034 | Agent account specified for the trading account.  
CONDITION_ACCOUNT_GROUP_PREVIOUS | 1035 | The group from which the trading account was moved. The condition is only used with the [IMTConAutomation::TRIGGER_ACCOUNT_CHANGE_GROUP (#entriggers)](../IMTConAutomation/Enumerations.md#entriggers) trigger.  
CONDITION_ACCOUNT_STATUS | 1036 | Status of account owner, RE (resident) or NR (non-resident).  
CONDITION_ACCOUNT_COMPANY | 1037 | Name of company of account owner.  
CONDITION_ACCOUNT_CLIENT_ID | 1038 | The unique client ID with which the trading account is associated ([IMTClient::RecordID](../../../Database-Interfaces/Clients/IMTClient/RecordID.md)).  
CONDITION_ACCOUNT_ACTIVITY_BALANCE_ELAPSED | 1039 | The number of days that have elapsed since the last [balance deal (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) on the account. Such deals include deposits/withdrawals, credit transactions, bonuses, adjustments, dividends, taxes, commissions, annual interest accrual and compensation. You can use this condition in addition to checking trading activity on the account, for example when automatically archiving accounts. If you archive accounts with zero balances, you can additionally check if the funds were withdrawn recently.  
CONDITION_ACCOUNT_ACTIVITY_CREDIT_ELAPSED | 1040 | The number of days that have elapsed since the last [credit transaction (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) on the account. Such transactions include credit transactions themselves, credit reset operations, as well as the accrual and withdrawal of bonuses.  
CONDITION_ACCOUNT_LAST | 2000 | End of enumeration of conditions by trading account parameters.  
CONDITION_MONITOR_CPU | 2001 | Total CPU usage.  
CONDITION_MONITOR_CPU_PROCESS | 2002 | Process CPU usage.  
CONDITION_MONITOR_CPU_PROCESS_THREADS | 2003 | Process threads.  
CONDITION_MONITOR_MEMORY_FREE | 2004 | Total free memory, MB.  
CONDITION_MONITOR_MEMORY_PROCESS | 2005 | Process memory, MB.  
CONDITION_MONITOR_DISK_FREE | 2006 | Disk free space, MB.  
CONDITION_MONITOR_DISK_SPEED_READ | 2007 | Disk read speed, MBps.  
CONDITION_MONITOR_DISK_SPEED_WRITE | 2008 | Disk write speed, MBps.  
CONDITION_MONITOR_DISK_QUEUE_LENGTH | 2009 | Disk queue.  
CONDITION_MONITOR_NETWORK_CONNECTIONS | 2010 | Connections.  
CONDITION_MONITOR_NETWORK_BLOCKED | 2011 | Blocked connections.  
CONDITION_MONITOR_NETWORK_SOCKETS | 2012 | Total sockets.  
CONDITION_MONITOR_NETWORK_TRAFFIC_IN | 2013 | Traffic in, Mbps.  
CONDITION_MONITOR_NETWORK_TRAFFIC_OUT | 2014 | Traffic out, Mbps.  
CONDITION_MONITOR_NETWORK_RETRANSMIT | 2015 | Retransmits, %.  
CONDITION_MONITOR_HANDLES_PROCESS | 2016 | Process handles.  
CONDITION_MONITOR_CPU_DPC | 2017 | CPU load when handling deferred procedure calls.  
CONDITION_MONITOR_CPU_INTERRUPTS | 2018 | CPU Interrupts.  
CONDITION_MONITOR_FIRST | 2001 | Beginning of enumeration of conditions by [cluster performance parameters](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_monitoring).  
CONDITION_MONITOR_LAST | 3000 | End of enumeration of conditions by cluster performance parameters.  
CONDITION_SERVER_ID | 3001 | [Server ID](../../Network/IMTConServer/Id.md).  
CONDITION_SERVER_TYPE | 3002 | [Server Type](../../Network/IMTConServer/Type.md).  
CONDITION_SERVER_CONNECTED | 3003 | Server connection state to the main trade server.  
CONDITION_SERVER_CURRENT_ID | 3004 | The identifier of the trade server on which the automation task was triggered.  
CONDITION_SERVER_CURRENT_TYPE | 3005 | The type of trading server on which the automation task was triggered: main or additional.  
CONDITION_SERVER_CURRENT_STATE | 3006 | The state of the trade server on which the automation task was triggered. Available values: 0 — the server does not reboot; 1 — a regular reboot has been started, 2 — the server service is stopped, 3 — the server service is stopped due to a platform update.  
CONDITION_SERVER_CURRENT_CONNECTED | 3007 | The state showing the connection between the trade server on which the automation task was triggered and the main server of the platform.  
CONDITION_SERVER_FIRST | 3001 | Beginning of enumeration of conditions by [server parameters](../../Network/IMTConServer.md).  
CONDITION_SERVER_LAST | 4000 | End of enumeration of conditions by server parameters.  
CONDITION_FINANCE_AMOUNT | 4001 | The amount of transactions.  
CONDITION_FINANCE_CURRENCY | 4002 | Operation currency.  
CONDITION_FINANCE_COMMENT | 4003 | A text comment to the operation.  
CONDITION_FINANCE_ACTION | 4004 | Deal type ([IMTDeal::EnDealAction (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction)): Buy, Sell, balance or credit operation, etc.  
CONDITION_FINANCE_MANAGER | 4005 | The login of the manager who performed the financial transaction.  
CONDITION_FINANCE_FIRST | 4001 | Beginning of enumeration of conditions by financial operation parameters.  
CONDITION_FINANCE_LAST | 5000 | End of enumeration of conditions by financial operation parameters.  
CONDITION_PRICES_SYMBOL | 5001 | The financial instrument for which a quote has been received.  
CONDITION_PRICES_LASTTIME | 5002 | Time of the last quote received for the financial instrument.  
CONDITION_PRICES_FIRST | 5001 | Beginning of enumeration of conditions by quote parameters.  
CONDITION_PRICES_LAST | 6000 | End of enumeration of conditions by quote parameters.  
CONDITION_POSITION_LOGIN | 6001 | The number of the account on which the position was opened.  
CONDITION_POSITION_TICKET | 6002 | Position ticket.  
CONDITION_POSITION_SYMBOL | 6003 | Financial instrument of a position.  
CONDITION_POSITION_VOLUME | 6004 | Position volume.  
CONDITION_POSITION_TYPE | 6005 | Position type.  
CONDITION_POSITION_PRICE_OPEN | 6006 | Position opening price.  
CONDITION_POSITION_PRICE_CURRENT | 6007 | Current price of the symbol, for which a position is open.  
CONDITION_POSITION_PROFIT | 6008 | Current profit of the position.  
CONDITION_POSITION_REASON | 6009 | Reason for opening the position.  
CONDITION_POSITION_TIME_CREATE | 6010 | Position opening time.  
CONDITION_POSITION_TIME_UPDATE | 6011 | Last position volume modification time.  
CONDITION_POSITION_EXPERT | 6012 | ID of the Expert Advisor that has opened the position.  
CONDITION_POSITION_TIME_CREATE_ELAPSED | 6013 | The amount of time that have elapsed since position opening.  
CONDITION_POSITION_TIME_UPDATE_ELAPSED | 6014 | The amount of time that have elapsed since the last change in position volume.  
CONDITION_POSITION_COMMENT | 6015 | A text comment to the position.  
CONDITION_POSITION_DEALER | 6016 | The login of the dealer who confirmed or placed the order (deal) which caused the position to open.  
CONDITION_POSITION_FIRST | 6001 | Beginning of enumeration of conditions by [position parameters](../../../Database-Interfaces/Trade/Positions/IMTPosition.md).  
CONDITION_POSITION_LAST | 7000 | End of enumeration of conditions by position parameters.  
CONDITION_DEAL_LOGIN | 7001 | Account number on which the deal was performed.  
CONDITION_DEAL_TICKET | 7002 | The ticket of a deal.  
CONDITION_DEAL_SYMBOL | 7003 | Financial instrument of a deal.  
CONDITION_DEAL_VOLUME | 7004 | Volume of a deal.  
CONDITION_DEAL_TYPE | 7005 | Deal type.  
CONDITION_DEAL_ENTRY | 7006 | Deal direction.  
CONDITION_DEAL_PRICE | 7007 | Transaction price  
CONDITION_DEAL_PROFIT | 7008 | Profit from a deal.  
CONDITION_DEAL_REASON | 7009 | Reason for deal execution.  
CONDITION_DEAL_TIME | 7010 | Deal execution time.  
CONDITION_DEAL_EXPERT | 7011 | ID of the Expert Advisor that has executed a deal.  
CONDITION_DEAL_COMMENT | 7012 | A text comment to the deal.  
CONDITION_DEAL_DEALER | 7013 | The login of the dealer who confirmed or placed the order, which caused the deal to execute.  
CONDITION_DEAL_FIRST | 7001 | Beginning of enumeration of conditions by [deal parameters](../../../Database-Interfaces/Trade/Deals/IMTDeal.md).  
CONDITION_DEAL_LAST | 8000 | End of enumeration of conditions by deal parameters.  
CONDITION_MESSAGE_FROM | 8001 | The login of the email sender.  
CONDITION_MESSAGE_FROM_NAME | 8002 | The name of the email sender.  
CONDITION_MESSAGE_TO | 8003 | The login of the email recipient.  
CONDITION_MESSAGE_TO_NAME | 8004 | The name of the email recipient.  
CONDITION_MESSAGE_SUBJECT | 8005 | Email subject.  
CONDITION_MESSAGE_BODY | 8006 | Contents of the email or message sent via the SMS provider or instant messenger.  
CONDITION_MESSAGE_ADDRESS | 8007 | Recipient's email address or phone number.  
CONDITION_MESSAGE_PROVIDER_NAME | 8008 | The configuration name of the SMS provider, instant messenger or mail server through which the message was sent.  
CONDITION_MESSAGE_PROVIDER_BALANCE | 8009 | Remaining balance with the SMS provider.  
CONDITION_MESSAGE_FIRST | 8001 | Beginning of enumeration of conditions based on the parameters of messages sent via the [internal mail](../../../Database-Interfaces/Mail-Database/IMTMail.md), [SMS providers](../../Messengers/IMTConMessenger.md), [instant messengers](../../Messengers/IMTConMessenger.md) and [email](../../Mail-Servers/IMTConEmail.md).  
CONDITION_MESSAGE_LAST | 9000 | End of enumeration of conditions by messaging parameters.  
CONDITION_ORDER_TICKET | 9001 | Order ticket.  
CONDITION_ORDER_ORDER_ID | 9002 | Order identifier in the external system.  
CONDITION_ORDER_LOGIN | 9003 | Account number from which the order was placed.  
CONDITION_ORDER_SYMBOL | 9004 | The financial instrument of the order.  
CONDITION_ORDER_TIME_SETUP | 9005 | Order placing time.  
CONDITION_ORDER_TIME_SETUP_ELAPSED | 9006 | The number of days that have elapsed since order placing.  
CONDITION_ORDER_TIME_EXPIRATION | 9007 | Order expiration time.  
CONDITION_ORDER_TYPE | 9008 | Order type.  
CONDITION_ORDER_PRICE_ORDER | 9009 | The order execution price specified by the trader.  
CONDITION_ORDER_PRICE_TRIGGER | 9010 | Trigger price for Buy Stop Limit and Sell Stop Limit orders.  
CONDITION_ORDER_PRICE_CURRENT | 9011 | The current price of the symbol, for which the order has been placed.  
CONDITION_ORDER_PRICE_SL | 9012 | Stop Loss specified in the order.  
CONDITION_ORDER_PRICE_TP | 9013 | Take Profit specified in the order.  
CONDITION_ORDER_VOLUME_INITIAL | 9014 | The volume requested by the client in the order.  
CONDITION_ORDER_VOLUME_CURRENT | 9015 | If the order is not filled in the volume requested by trader this field will display the remainder volume.  
CONDITION_ORDER_STATE | 9016 | Current state of the order (filled, rejected, partially filled, expired, etc.).  
CONDITION_ORDER_EXPERT | 9017 | Identifier (magic number) of an Expert Advisor which placed the order in the client terminal.  
CONDITION_ORDER_POSITION_ID | 9018 | Ticket of the position opened, modified or closed due to this order.  
CONDITION_ORDER_COMMENT | 9019 | A text comment to the order.  
CONDITION_ORDER_CONTRACT_SIZE | 9020 | The contract size of the symbol, for which an order was placed.  
CONDITION_ORDER_CURRENCY | 9021 | The deposit currency of the client who has placed the order.  
CONDITION_ORDER_DEALER | 9022 | The login of the dealer who confirmed or placed the order.  
CONDITION_ORDER_FIRST | 9001 | Beginning of enumeration of conditions by [order parameters](../../../Database-Interfaces/Trade/Orders/IMTOrder.md).  
CONDITION_ORDER_LAST | 10000 | End of enumeration of conditions by order parameters.  
CONDITION_GATEWAY_NAME | 10001 | The name of the gateway configuration.  
CONDITION_GATEWAY_ID | 10002 | The identifier specified in the gateway configuration.  
CONDITION_GATEWAY_CONNECTED | 10003 | The state of the gateway connection to the platform at the trigger activation time. Connected — true; not connected — false.  
CONDITION_GATEWAY_FIRST | 10001 | Beginning of enumeration of conditions by [gateway parameters](../../Gateways/IMTConGateway.md).  
CONDITION_GATEWAY_LAST | 11000 | End of enumeration of conditions by gateway parameters.  
CONDITION_DATAFEED_NAME | 11001 | The name of the datafeed configuration.  
CONDITION_DATAFEED_CONNECTED | 11002 | The state of the datafeed connection to the platform at the trigger activation time. Connected — true; not connected — false.  
CONDITION_DATAFEED_FIRST | 11001 | Beginning of enumeration of conditions by [datafeed parameters](../../Data-Feeds/IMTConFeeder.md).  
CONDITION_DATAFEED_LAST | 12000 | End of enumeration of conditions by datafeed parameters.  
CONDITION_KYC_STATE_CODE | 12001 | KYC check [status code (#kyc-code)](Enumerations.md#kyc-code).  
CONDITION_KYC_STATE_DESC | 12002 | KYC check [status description (#kyc-code)](Enumerations.md#kyc-code).  
CONDITION_KYC_REJECT_REASON | 12003 | [Reason for client rejection (#kyc-code)](Enumerations.md#kyc-code) by the KYC system.  
CONDITION_KYC_FIRST | 12001 | Start of enumeration of conditions by [KYC checks](../../KYC/IMTCon.md).  
CONDITION_KYC_LAST | 13000 | End of enumeration of conditions by KYC checks.  
CONDITION_MANAGER_LOGIN | 13001 | The manager login.  
CONDITION_MANAGER_FIRST | 13001 | Beginning of enumeration of conditions by [manager account parameters](../../Managers/IMTConManager.md).  
CONDITION_MANAGER_LAST | 14000 | End of enumeration of conditions by manager account parameters.  
CONDITION_EXTERNAL_WEBCALLBACK_URL | 14001 | The URL of the callback request that runs the automation task.  
CONDITION_EXTERNAL_FIRST | 14001 | Beginning of the enumeration of conditions associated with the running of automation tasks from [external systems (#external)](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_trigger#external).  
CONDITION_EXTERNAL_LAST | 15000 | End of the enumeration of conditions associated with the running of automation tasks from external systems.  
CONDITION_CONNECTION_IP | 15001 | Client's IP address.  
CONDITION_CONNECTION_COUNTRY | 15002 | The country where the IP address is located.  
CONDITION_CONNECTION_CITY | 15003 | The city where the IP address is located.  
CONDITION_CONNECTION_FLAG_DATACENTER | 15004 | The address belongs to a data center.  
CONDITION_CONNECTION_FLAG_TOR | 15005 | The address belongs to the TOR network.  
CONDITION_CONNECTION_FLAG_PROXY | 15006 | The address is a proxy server.  
CONDITION_CONNECTION_FLAG_VPN | 15007 | The address is a VPN server.  
CONDITION_CONNECTION_FLAG_ATTACKER | 15008 | The address has been seen in various attacks, such as as spam, password brute-forcing, DDoS, etc.  
CONDITION_CONNECTION_FLAG_BOTNET | 15009 | The address belongs to a botnet.  
CONDITION_CONNECTION_ASN | 15010 | The Autonomous System Number (ASN) to which an IP address belongs.  
CONDITION_CONNECTION_ISP | 15011 | The name of the internet service provider that owns an IP address.  
CONDITION_CONNECTION_FIRST | 15001 | The beginning of the enumeration of conditions associated with the client's IP address.  
CONDITION_CONNECTION_LAST | 16000 | The end of the enumeration of conditions associated with the client's IP address.  
CONDITION_PAYMENT_ACTION | 16001 | Payment transaction type in the [integrated payment system](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments): deposit or withdrawal.  
CONDITION_PAYMENT_AMOUNT | 16002 | The transaction amount requested by the client. Specified in the deposit currency.  
CONDITION_PAYMENT_CURRENCY | 16003 | Transaction currency.  
CONDITION_PAYMENT_COMMISSION | 16004 | The commission charged by the broker in accordance with the [settings (#commissions)](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments/payments_wallets#commissions).  
CONDITION_PAYMENT_WALLET_AMOUNT | 16005 | The amount of the transaction on the side of the payment provider. It is specified in the currency selected by the user on the client terminal side when making the operation.  
CONDITION_PAYMENT_WALLET_CURRENCY | 16006 | The currency of the transaction on the payment provider's side.  
CONDITION_PAYMENT_WALLET_COMMISSION | 16007 | The payment provider's commission for the operation.  
CONDITION_PAYMENT_DESCRIPTION | 16008 | Additional information about the transaction. Can be filled in by payment systems or manually by managers.  
CONDITION_PAYMENT_MANAGER | 16009 | The login and name of the manager who [processed the transaction](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments/payments_processing). It is filled only for manually processed transactions.  
CONDITION_PAYMENT_TYPE | 16010 | The payment method type: card, bank transfer, etc.  
CONDITION_PAYMENT_PROVIDER_TYPE | 16011 | The type of the payment provider (gateway).  
CONDITION_PAYMENT_PROVIDER_NAME | 16012 | The name of the payment provider configuration under which the payment was made.  
CONDITION_PAYMENT_CLIENT_IP | 16013 | The IP address from which the payment was requested.  
CONDITION_PAYMENT_CLIENT_TYPE | 16014 | The type of client terminal from which the payment was requested: desktop, mobile, or web.  
CONDITION_PAYMENT_CLIENT_DEAL | 16015 | Ticket of the balance operation via which funds are credited to or debited from the trading account.  
CONDITION_PAYMENT_EXTERNAL_ID | 16016 | The transaction identifier on the payment provider's side.  
CONDITION_PAYMENT_EXTERNAL_ERROR_CODE | 16017 | The error code that occurred on the provider's side.  
CONDITION_PAYMENT_EXTERNAL_ERROR_DESC | 16018 | A description of the error that occurred on the provider's side.  
CONDITION_PAYMENT_REJECT_CODE | 16019 | The error code that occurred on the platform side.  
CONDITION_PAYMENT_REJECT_DESC | 16020 | A description of the error that occurred on the platform side.  
CONDITION_PAYMENT_FIRST | 16001 | Beginning of enumeration of conditions related to transactions in the [integrated payment system](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments).  
CONDITION_PAYMENT_LAST | 17000 | End of enumeration of conditions related to transactions in the integrated payment system.  
CONDITION_FIRST |  | Beginning of enumeration. Corresponds to CONDITION_DATETIME_FIRST.  
CONDITION_LAST |  | End of enumeration. Corresponds to CONDITION_CONNECTION_LAST.  
  
This enumeration is used in the [IMTConAutoCondition::Condition](Condition.md) method.

<a id="enconditionrule"></a>
## IMTConAutoCondition::EnConditionRule (#enconditionrule)

The IMTConAutoCondition::EnConditionRule enumeration contains parameter and value comparison types.

ID number | Value | Description  
RULE_EQ | 0 | Condition of equality.  
RULE_NOT_EQ | 1 | Condition of inequality.  
RULE_GREATER | 2 | Condition of "greater than".  
RULE_NOT_LESS | 3 | Condition of "not less than".  
RULE_LESS | 4 | Condition of "less than".  
RULE_NOT_GREATER | 5 | Condition of "not greater than".  
RULE_MATCH_MASK | 6 | Mask matching condition. Here you can specify strings with the "*" mask. For example: Condition IMTConAutoCondition::CONDITION_PRICES_SYMBOL, value "Forex\USD*" — all symbols from the Forex group, having USD as an underlying currency.  
RULE_FIRST |  | Beginning of enumeration. Corresponds to RULE_EQ.  
RULE_LAST |  | End of enumeration. Corresponds to RULE_MATCH_MASK.  
  
The enumeration is used in the [IMTConAutoCondition::Rule](Rule.md) method.

<a id="enconditiontype"></a>
## IMTConAutoCondition::EnConditionType (#enconditiontype)

The IMTConAutoCondition::EnConditionType enumeration contains parameter types.

ID number | Value | Description  
TYPE_NONE | 0 | Parameter is not specified.  
TYPE_STRING | 1 | The parameter is of the string type.  
TYPE_INT | 2 | The parameter is of the int type.  
TYPE_UINT | 3 | The parameter is of the uint type.  
TYPE_DOUBLE | 4 | The parameter is of the double type.  
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
TYPE_POSITION | 16 | The parameter sets a [position property](../../../Database-Interfaces/Trade/Positions/IMTPosition.md).  
TYPE_REASON | 17 | The parameters sets the trade operation execution [reason](../../../Database-Interfaces/Trade/Deals/IMTDeal/Reason.md).  
TYPE_DEAL | 18 | The parameter sets a [deal property](../../../Database-Interfaces/Trade/Deals/IMTDeal.md).  
TYPE_DEAL_ENTRY | 19 | The parameter sets a [deal direction](../../../Database-Interfaces/Trade/Deals/IMTDeal/Entry.md).  
TYPE_ORDER | 20 | The parameter sets the [order type](../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md).  
TYPE_ORDER_STATE | 21 | The parameter sets the [order state](../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md).  
TYPE_KYC_STATE | 22 | The parameter sets the state of the [KYC check (#kyc-code)](Enumerations.md#kyc-code).  
TYPE_LOGIN | 23 | The parameter sets the account number.  
TYPE_DURATION | 24 | The parameters sets the number of days, hours, minutes and seconds.  
TYPE_FIRST |  | Beginning of enumeration. Corresponds to TYPE_NONE.  
TYPE_LAST |  | End of enumeration. Corresponds to TYPE_DURATION.  
  
<a id="kyc-code"></a>
## KYC check status code and description (#kyc-code)

Code | Description  
---|---  
STATUS_INIT | Initiated  
STATUS_QUEUED | Queued  
STATUS_APPROVED | Approved  
STATUS_DECLINED | Declined  
STATUS_EXPIRED | Expired  
ERROR_GENERAL | General error  
ERROR_CONNECTION | Connection error  
ERROR_AUTH | Auth error  
ERROR_INTERNAL | Internal error  
ERROR_DOC_DUPLICATE | Duplicate document (image, video) was uploaded. Exact equality is taken into account  
ERROR_DOC_TOO_MANY | Applicant contains too many documents. Adding new ones is not allowed  
ERROR_DOC_TOO_BIG | Uploaded file is too big (more than 64MB)  
ERROR_DOC_EMPTY | Uploaded file is empty (0 bytes)  
ERROR_DOC_CORRUPTED | File is corrupted or incorrect format (e.g. PDF file is uploaded as JPEG)  
ERROR_DOC_FORMAT | Unsupported file format (e.g. a TIFF image)  
  
The values are used in [IMTConAutoCondition::CONDITION_KYC_* (#enconditions)](Enumerations.md#enconditions) parameters.

The enumeration is used in the [IMTConAutoCondition::ValueType](ValueType.md) method.
