[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / Enumerations

[Previous](../IMTConGroup.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConGroup](../IMTConGroup.md) class contains the following enumerations:

  * [IMTConGroup::EnPermissionsFlags (#enpermissionsflags)](Enumerations.md#enpermissionsflags)
  * [IMTConGroup::EnAuthMode (#enauthmode)](Enumerations.md#enauthmode)
  * [IMTConGroup::EnReportsMode (#enreportsmode)](Enumerations.md#enreportsmode)
  * [IMTConGroup::EnReportsFlags (#enreportsflags)](Enumerations.md#enreportsflags)
  * [IMTConGroup::EnNewsMode (#ennewsmode)](Enumerations.md#ennewsmode)
  * [IMTConGroup::EnMailMode (#enmailmode)](Enumerations.md#enmailmode)
  * [IMTConGroup::EnHistoryLimit (#enhistorylimit)](Enumerations.md#enhistorylimit)
  * [IMTConGroup::EnFreeMarginMode (#enfreemarginmode)](Enumerations.md#enfreemarginmode)
  * [IMTConGroup::EnStopOutMode (#enstopoutmode)](Enumerations.md#enstopoutmode)
  * [IMTConGroup::EnTradeFlags (#entradeflags)](Enumerations.md#entradeflags)
  * [IMTConGroup::EnMarginFreeProfitFlags (#enmarginfreeprofitflags)](Enumerations.md#enmarginfreeprofitflags)
  * [IMTConGroup::EnAuthOTPMode (#enauthotpmode)](Enumerations.md#enauthotpmode)
  * [IMTConGroup::EnTransferMode (#entransfermode)](Enumerations.md#entransfermode)
  * [IMTConGroup::EnMarginMode (#enmarginmode)](Enumerations.md#enmarginmode)
  * [IMTConGroup::EnMarginFlags (#enmarginflags)](Enumerations.md#enmarginflags)



<a id="enpermissionsflags"></a>
## IMTConGroup::EnPermissionsFlags (#enpermissionsflags)

Flags of group permissions are listed in IMTConGroup::EnPermissionsFlags.

ID | Value | Description  
PERMISSION_NONE | 0x00000000 | No permissions. Default value.  
PERMISSION_CERT_CONFIRM | 0x00000001 | Enable confirmation of certificates.  
PERMISSION_ENABLE_CONNECTION | 0x00000002 | Allow client connections.  
PERMISSION_RESET_PASSWORD | 0x00000004 | Forces users to change the master password during the first connection. Users will not be able to perform any actions before they change the password.  
PERMISSION_FORCED_OTP_USAGE | 0x00000008 | In some countries, regulating institutions require the use of additional account security measures, such as the use of OTP. When this flag is enabled, all clients from the group will need to use one-time passwords for connection. Otherwise, clients can bind their accounts to the generator or use the default authentication method. Before you enable it, please inform your clients about the new OTP option. Be extremely careful enabling this option for the only one manager group on the trade server. The mobile terminal MetaTrader 5 for iPhone is used for generating passwords.  
PERMISSION_RISK_WARNING | 0x00000010 | If the flag is enabled, when a client connects from the trading terminal, a warning about the risks associated with operations on the financial markets is displayed. Trade operations on a client's account are not allowed until the client confirms that he or she has read the warning and is aware of the risks. To confirm, the client should check "I am aware of the risks and I wish to trade in financial markets". This warning is displayed once per session of the terminal. The next time it appears after the restart of the terminal. The risk warning is not displayed for demo accounts.  
PERMISSION_REGULATION_PROTECT | 0x00000020 | Enforce country-specific regulatory restrictions for retail clients. Every country has regulators — state bodies that supervise the activities of financial institutions (including brokers). Each regulator has its own set of requirements applied to trading currencies, securities and other instruments. In most cases, clients of brokerage firms are individuals from different countries. The platform provides the means of meeting the requirements of certain regulators without interfering with the work of traders not covered with these requirements. Restrictions applied to trader accounts depend on the client's country and other conditions set by that country's regulator. For example, the National Securities Market Commission (Comisión Nacional del Mercado de Valores) of Spain compels brokers to warn clients using the leverage of 1:10 or higher about potential risks in a special way. Therefore, if a client's country is Spain and they use a leverage of 1:10 or higher, an additional warning is displayed in the trading dialog Currently, only one regional limitation is used in the platform. The list is to be expanded later.  
PERMISSION_NOTIFY_DEALS | 0x00000040 | Allow accounts to subscribe to [server push notifications  (#push)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/groups_settings#push) about deals.  
PERMISSION_NOTIFY_ORDERS | 0x00000080 | Allow accounts to subscribe to server push notifications about orders.  
PERMISSION_NOTIFY_BALANCES | 0x00000100 | Allow accounts to subscribe to server push notifications about balance operations.  
PERMISSION_ALL |  | End of enumeration. Corresponds to enabling of all permissions.  
  
This enumeration is used in the [IMTConGroup::PermissionFlags](PermissionsFlags.md) method.

<a id="enauthmode"></a>
## IMTConGroup::EnAuthMode (#enauthmode)

Types of authentication of clients from the group are listed in IMTConGroup::EnAuthMode.

ID | Value | Description  
AUTH_STANDARD | 0 | Standard authorization.  
AUTH_RSA1024 | 1 | Extended authentication with 1024-bit encryption.  
AUTH_RSA2048 | 2 | Extended authorization with 2048-bit encryption.  
AUTH_RSA_CUSTOM | 4  | Extended authentication using the third-party certificates.  
AUTH_FIRST |  | Beginning of enumeration. It corresponds to AUTH_STANDARD.  
AUTH_LAST |  | End of enumeration. Corresponds to AUTH_RSA_CUSTOM.  
  
This enumeration is used in the [IMTConGroup::AuthMode](AuthMode.md) method.

<a id="enreportsmode"></a>
## IMTConGroup::EnReportsMode (#enreportsmode)

Report generation modes are listed in IMTConGroup::EnReportsMode.

ID | Value | Description  
REPORTS_DISABLED | 0 | Reports are disabled.  
REPORTS_FULL | 1 | The platform can save the end-of-day and/or end-of-month states of accounts to a special database. The information includes balance, equity, margin, and other details. The database is located on the trade server, in the bases\daily\daily_*.dat file. Data from the file is used in end-of-day and end-of-month trading reports sent to clients, as well as in some manager reports. If the mode is enabled, the platform will save information on accounts from the selected group to the database. This flag enables the generation of both end-of-day and end-of-month data.  
REPORTS_DAY_ONLY | 2 | Enable data generation for reports only at the end of the day.  
REPORTS_MONTH_ONLY | 3 | Enable data generation for reports only at the end of the month.  
REPORTS_FIRST |  | Beginning of enumeration. It corresponds to REPORTS_DISABLED.  
REPORTS_LAST |  | End of enumeration. Corresponds to REPORTS_MONTH_ONLY.  
  
This enumeration is used in the [IMTConGroup::ReportsMode](ReportsMode.md) method.

<a id="enreportsflags"></a>
## IMTConGroup::EnReportsFlags (#enreportsflags)

Report generation options are listed in IMTConGroup::EnReportsFlags.

ID | Value | Description  
REPORTSFLAGS_NONE | 0 | No additional options enabled.  
REPORTSFLAGS_EMAIL | 1 | Enables sending of generated HTML report files to clients by email. Addresses from trading accounts ([IMTUser::Email](../../../Database-Interfaces/Users/IMTUser/EMail.md)) are used for sending.  
REPORTSFLAGS_SUPPORT | 2 | Enables sending of report copies to a technical support email address ([IMTConGroup::CompanySupportEmail](CompanySupportEmail.md)).  
REPORTSFLAGS_STATEMENTS | 4 | Enables account state report generation. The HTML report files are created using templates from the \templates\confirmation\ and \templates\statement\ folders on the trade server. The generate reports, the [IMTConGroup::REPORTS_STANDARD (#enreportsmode)](Enumerations.md#enreportsmode) mode must be enabled.  
REPORTSFLAGS_ALL |  | End of enumeration. All flags are enabled.  
  
This enumeration is used in the [IMTConGroup::ReportsFlags](ReportsMode.md) method.

<a id="ennewsmode"></a>
## IMTConGroup::EnNewsMode (#ennewsmode)

Modes of news sending are listed in IMTConGroup::EnNewsMode.

ID | Value | Description  
NEWS_MODE_DISABLED | 0 | News sending is disabled.  
NEWS_MODE_HEADERS | 1 | Only news headers.  
NEWS_MODE_FULL | 2 | Fill package.  
NEWS_MODE_FIRST |  | Beginning of enumeration. It corresponds to NEWS_MODE_DISABLED.  
NEWS_MODE_LAST |  | End of enumeration. It corresponds to NEWS_MODE_FULL.  
  
This enumeration is used in the [IMTConGroup::NewsMode](NewsMode.md) method.

<a id="enmailmode"></a>
## IMTConGroup::EnMailMode (#enmailmode)

Modes of using the internal mail system are listed in IMTConGroup::EnMailMode.

ID | Value | Description  
MAIL_MODE_DISABLED | 0 | Disable the internal mail system.  
MAIL_MODE_FULL | 1 | Enable the internal mail system.  
MAIL_MODE_FIRST |  | Beginning of enumeration. It corresponds to MAIL_MODE_DISABLED.  
MAIL_MODE_LAST |  | End of enumeration. It corresponds to MAIL_MODE_FULL.  
  
This enumeration is used in the [IMTConGroup::MailMode](MailMode.md) method.

<a id="enhistorylimit"></a>
## IMTConGroup::EnHistoryLimit (#enhistorylimit)

The intervals of trading history available to clients from the group are listed in IMTConGroup::EnHistoryLimit.

ID | Value | Description  
TRADE_HISTORY_ALL | 0 | The entire history.  
TRADE_HISTORY_MONTHS_1 | 1 | One month.  
TRADE_HISTORY_MONTHS_3 | 2 | Three months.  
TRADE_HISTORY_MONTHS_6 | 3 | Six months.  
TRADE_HISTORY_YEAR_1 | 4  | One year.  
TRADE_HISTORY_YEAR_2 | 5 | Two years.  
TRADE_HISTORY_YEAR_3 | 6 | Three years.  
TRADE_HISTORY_FIRST |  | Beginning of enumeration. It corresponds to TRADE_HISTORY_ALL.  
TRADE_HISTORY_LAST |  | End of enumeration. It corresponds to TRADE_HISTORY_YEAR_3.  
  
This enumeration is used in the [IMTConGroup::LimitHistory](LimitHistory.md) method.

<a id="enfreemarginmode"></a>
## IMTConGroup::EnFreeMarginMode (#enfreemarginmode)

Modes of including floating profit/loss into free margin calculation are listed in IMTConGroup::EnFreeMarginMode.

ID | Value | Description  
FREE_MARGIN_NOT_USE_PL | 0 | Do not use unrealized profit/loss.  
FREE_MARGIN_USE_PL | 1 | Use unrealized profit/loss.  
FREE_MARGIN_PROFIT | 2 | Use unrealized profit.  
FREE_MARGIN_LOSS | 3 | Use unrealized loss.  
FREE_MARGIN_FIRST |  | Beginning of enumeration. It corresponds to FREE_MARGIN_NOT_USE_PL.  
FREE_MARGIN_LAST |  | End of enumeration. It corresponds to FREE_MARGIN_LOSS.  
  
This enumeration is used in the [IMTConGroup::MarginFreeMode](MarginFreeMode.md) method.

<a id="enstopoutmode"></a>
## IMTConGroup::EnStopOutMode (#enstopoutmode)

Modes for checking Margin Call and Stop Out are listed in IMTConGroup::EnStopOutMode.

ID | Value | Description  
STOPOUT_PERCENT | 0 | The levels of Margin Call and Stop Out in percentage terms.  
STOPOUT_MONEY | 1 | The levels of Margin Call and Stop Out in money terms.  
STOPOUT_FIRST |  | Beginning of enumeration. It corresponds to STOPOUT_PERCENT.  
STOPOUT_LAST |  | End of enumeration. It corresponds to STOPOUT_MONEY.  
  
This enumeration is used in the [IMTConGroup::MarginSOMode](MarginSOMode.md) method.

<a id="entradeflags"></a>
## IMTConGroup::EnTradeFlags (#entradeflags)

Group trade options are enumerated in IMTConGroup::EnTradeFlags.

ID | Value | Description  
TRADEFLAGS_NONE | 0x00000000 | Options are disabled.  
TRADEFLAGS_SWAPS | 0x00000001 | Allow charging of swaps.  
TRADEFLAGS_TRAILING | 0x00000002 | Enable trailing stop.  
TRADEFLAGS_EXPERTS | 0x00000004 | Enable trading using Expert Advisors.  
TRADEFLAGS_EXPIRATION | 0x00000008 | Enable order expiration.  
TRADEFLAGS_SIGNALS_ALL | 0x00000010 | Allows using the [Signals](https://www.mql5.com/ru/signals "Signals in MetaTrader") service in trading terminals.  
TRADEFLAGS_SIGNALS_OWN | 0x00000020 | Allow only using [signals](https://www.mql5.com/ru/signals "Signals in MetaTrader") from the company's servers. If this flag is enabled, clients from this group will only be able to subscribe to signals based on the accounts opened with the same broker. Signals from other accounts will not be displayed in trading terminals.  
TRADEFLAGS_SO_COMPENSATION | 0x00000040 | Automatically execute on a client's account the special [DEAL_SO_COMPENSATION (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) operation, which increases the balance and sets it to zero, if the balance has become negative after a position was closed by Stop Out. For more details please read the [MetaTrader 5 Administrator Help files (#compensate)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/groups_settings#compensate).  
TRADEFLAGS_SO_FULLY_HEDGED | 0x00000080 | If the flag is enabled, then Stop out will be performed on accounts having open positions, the zero margin (positions are covered) and negative equity. If the option is disabled, orders and positions will not be forcibly closed in above cases. The flag can be only used on hedging accounts. ([IMTConGroup::MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](Enumerations.md#enmarginmode)).  
TRADEFLAGS_FIFO_CLOSE | 0x00000100 | The position closing mode by FIFO rule. If the flag is enabled, then positions for each instrument can only be closed only in the order in which they were opened: the oldest one should be closed first, then the next one, etc. The option is only valid for hedging accounts, in which traders can have multiple positions for the same financial instrument. There are three main methods to close a position; the flag behavior will be different for each of the methods:

  * Closing from the client terminal: the trader closes the position manually, using a trading robot, based on the Signals service subscription, etc. In case of an attempt to close a position, which does not meet the FIFO rule, the trader will receive an appropriate error.
  * Closing upon Stop Loss or Take Profit activation: these orders are processed on the server side, so the position closure is not requested on the trader (terminal) side, but is initiated by the server. If Stop Loss or Take Profit triggers for a position, and this position does not comply with the FIFO rule (there is an older position fro the same symbol), the position will not be closed. An appropriate message will be printed to the log: "position close prohibited by FIFO rule, position #100448219 buy 3.00 EURUSD 1.11544 sl: 1.11537 tp: 1.11549 take profit activation skipped".
  * Closing upon Stop Out triggering: such operations are also processed on the server side. In a normal mode, in which FIFO-based closing is disabled, in case of [Stop Out (#stopout-processing)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/groups_settings#stopout-processing) positions are closed starting with the one having the largest loss. If this option option is enabled, the open time will be additionally checked for losing positions. The server determines losing positions for each symbol, finds the oldest position for each symbol, and then closes the one which has the greatest loss among the found positions.

  
TRADEFLAGS_HEDGE_PROHIBIT | 0x00000200 | Prohibit opening of opposite positions and placing of opposite orders. If this option is enabled, accounts are not allowed to have oppositely directed positions and orders for the same financial instrument. For example, if the account has a Buy position, then the user cannot open a Sell position or place a pending sell order for the same symbol. If such an attempt is made, the user will receive the [MT_RET_REQUEST_HEDGE_PROHIBITED](../../../Return-Codes/Trade-Requests.md) error. The option is only valid for groups with the hedging position accounting mode ([IMTConGroup::MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](Enumerations.md#enmarginmode)).  
TRADEFLAGS_DEAL_COST | 0x00000400 | Calculate deal execution costs and display them in client terminals. All NFA regulated brokers should enable this option. For more details, please see [MetaTrader 5 Administrator documentation (#deal-cost)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_groups/groups_settings#deal-cost).  
TRADEFLAGS_SO_COMPENSATION_CREDIT | 0x00000800 | Works as an addition to the TRADEFLAGS_SO_COMPENSATION flag. If enabled, the credit funds on the account will be set to zero after a negative balance compensation operation. Credit funds are withdrawn in a separate balance operation with the [DEAL_SO_CREDIT_COMPENSATION (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) type.  
TRADEFLAGS_ALL |  | End of enumeration. All flags are enabled.  
  
This enumeration is used in the [IMTConGroup::TradeFlags](TradeFlags.md) method.

<a id="enmarginfreeprofitflags"></a>
## IMTConGroup::EnMarginFreeProfitFlags (#enmarginfreeprofitflags)

Modes of using profit/loss recorded during a trading day in free margin calculation are listed in IMTConGroup::EnMarginFreeProfitFlags.

ID | Value | Description  
FREE_MARGIN_PROFIT_PL | 0 | Taking into account the profit and loss recorded during the trading day when calculating the free margin.  
FREE_MARGIN_PROFIT_LOSS | 1 | Taking into account the loss recorded during the trading day when calculating the free margin. The profits of the client during a trading day are accumulated in the [IMTAccount::BlockedProfit](../../../Database-Interfaces/Trade/Accounts/IMTAccount/BlockedProfit.md) field and are not included in the free margin. At the end of the trading day, the accumulated profits are credited to the balance and the value of IMTAccount::BlockedProfit is reset. This option only works with the [netting position accounting (#enfreemarginmode)](Enumerations.md#enfreemarginmode).  
FREE_MARGIN_PROFIT_FIRST |  | Beginning of enumeration. Corresponds to FREE_MARGIN_PROFIT_PL.  
FREE_MARGIN_PROFIT_LAST |  | End of enumeration. Corresponds to FREE_MARGIN_PROFIT_LOSS.  
  
This enumeration is used in the [IMTConGroup::MarginFreeProfitMode](MarginFreeProfitMode.md) method.

<a id="enauthotpmode"></a>
## IMTConGroup::EnAuthOTPMode (#enauthotpmode)

Authentication modes using one-time passwords are enumerated in IMTConGroup::EnAuthOTPMode.

ID | Value | Description  
AUTH_OTP_DISABLED | 0 | Authentication via one-time passwords is disabled.  
AUTH_OTP_TOTP_SHA256 | 1 | Authentication is performed using the standard generator of one-time passwords TOTP SHA-256. One-time passwords are used for all types of connection.  
AUTH_OTP_TOTP_SHA256_WEB | 2 | Authentication is performed using the standard generator of one-time passwords TOTP SHA-256. One-time passwords are used only for connections via web terminal.  
AUTH_OTP_FIRST |  | Beginning of enumeration. It corresponds to AUTH_OTP_DISABLED.  
AUTH_OTP_LAST |  | End of enumeration. It corresponds to AUTH_OTP_TOTP_SHA256_WEB.  
  
This enumeration is used in the [IMTConGroup::AuthOTPMode](AuthOTPMode.md) method.

<a id="entransfermode"></a>
## IMTConGroup::EnTransferMode (#entransfermode)

The IMTConGroup::EnTransferMode enumeration contains modes of money transfer between accounts.

ID | Value | Description  
TRANSFER_MODE_DISABLED | 0 | Transfer of funds is disabled.  
TRANSFER_MODE_NAME | 1 | Transfer of funds is only allowed between accounts with a matching name and email.  
TRANSFER_MODE_GROUP | 2 | Transfer of funds is only allowed between accounts from the same group or subgroup (for example, accounts from the group demo\forex and demo\CFD).  
TRANSFER_MODE_NAME_GROUP | 3 | The transfer of funds is allowed when the following two conditions are met: matching names and email addresses, accounts from the same group or subgroup.  
TRANSFER_MODE_FIRST |  | Beginning of enumeration. Corresponds to TRANSFER_MODE_DISABLED  
TRANSFER_MODE_LAST |  | End of enumeration. Corresponds to TRANSFER_MODE_NAME_GROUP.  
  
This enumeration is used in the [IMTConGroup::TradeTransferMode](TradeTransferMode.md) method.

<a id="enmarginmode"></a>
## IMTConGroup::EnMarginMode (#enmarginmode)

The IMTConGroup::EnMarginMode enumeration contains risk management models, which define the type of pre-trade control and the system of positions used.

ID | Value | Description  
MARGIN_MODE_RETAIL | 0 | Used for the OTC market. Margin calculation is based on the type of instrument, as well as group settings. The netting position accounting system is used.  
MARGIN_MODE_EXCHANGE_DISCOUNT | 1 | Used on the exchange markets. Margin calculation is based on the discounts specified in symbol settings. Discounts are set by the broker, however they cannot be lower than the exchange set values.  
MARGIN_MODE_RETAIL_HEDGED | 2 | Used for the OTC market. Margin calculation is based on the type of instrument, as well as group settings. The hedging position accounting system is used.  
MARGIN_MODE_FIRST |  | Beginning of enumeration. Corresponds to MARGIN_MODE_RETAIL.  
MARGIN_MODE_LAST |  | End of enumeration. Corresponds to MARGIN_MODE_RETAIL_HEDGED.  
  
This enumeration is used in the [IMTConGroup::MarginMode](MarginMode.md) method.

<a id="enmarginflags"></a>
## IMTConGroup::EnMarginFlags (#enmarginflags)

The IMTConGroup::EnMarginFlags enumeration contains margin calculation flags.

ID | Value | Description  
MARGIN_FLAGS_NONE | 0 | No flags.  
MARGIN_FLAGS_CLEAR_ACC | 1 | The flag is only available in the [FREE_MARGIN_PROFIT_LOSS (#enmarginfreeprofitflags)](Enumerations.md#enmarginfreeprofitflags) mode. When the flag is enabled, the client's profit accumulated during a day will be released and added to the balance at the end of the trading day (and will be taken into account when calculating the free margin). If the flag is not used, the accumulated profit can only be released using another application (e.g. from a gateway). The operation will not be performed by the server.  
MARGIN_FLAGS_ALL |  | End of enumeration. All flags are enabled.  
  
This enumeration is used in the [IMTConGroup::MarginFlags](MarginFlags.md) method.
