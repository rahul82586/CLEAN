[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../../Platform-Components.md) / [Backup Server](../../../Backup-Server.md) / [SQL Export](../../SQL-Export.md) / [mt5_groups](../mt5-groups.md) / Enumerations

[Previous](../mt5-groups.md) | [Next](../mt5-groups-symbols.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

To pass information about groups the following enumerations are used:

  * [EnPermissionsFlags (#enpermissionsflags)](Enumerations.md#enpermissionsflags)
  * [EnAuthMode (#enauthmode)](Enumerations.md#enauthmode)
  * [EnReportsMode (#enreportsmode)](Enumerations.md#enreportsmode)
  * [EnReportsFlags (#enreportsflags)](Enumerations.md#enreportsflags)
  * [EnNewsMode (#ennewsmode)](Enumerations.md#ennewsmode)
  * [EnMailMode (#enmailmode)](Enumerations.md#enmailmode)
  * [EnHistoryLimit (#enhistorylimit)](Enumerations.md#enhistorylimit)
  * [EnFreeMarginMode (#enfreemarginmode)](Enumerations.md#enfreemarginmode)
  * [EnStopOutMode (#enstopoutmode)](Enumerations.md#enstopoutmode)
  * [EnTradeFlags (#entradeflags)](Enumerations.md#entradeflags)
  * [EnMarginFreeProfitFlags (#enmarginfreeprofitflags)](Enumerations.md#enmarginfreeprofitflags)



<a id="enpermissionsflags"></a>
## EnPermissionsFlags (#enpermissionsflags)

Flags of permissions for groups are listed in EnPermissionsFlags.

ID | Value | Description  
PERMISSION_NONE | 0x00000000 | No permissions. Default value.  
PERMISSION_CERT_CONFIRM | 0x00000001 | Enable confirmation of certificates.  
PERMISSION_ENABLE_CONNECTION | 0x00000002 | Allow client connections.  
PERMISSION_RESET_PASSWORD | 0x00000004 | Force users to change their master password at first login. A user will not be able to take any actions before changing the password.  
PERMISSION_FORCED_OTP_USAGE | 0x00000008 | In some countries, regulators require use of additional account security measures, such as the use of OTP. When this flag is enabled, all clients in this group will need to use one-time passwords to connect. Otherwise, clients can bind their accounts to the generator or use the default authentication method. Before you enable it, please inform your clients about the new OTP option. Be extremely careful when enabling this option for the only one manager group on the trading server. For generating one-time passwords, the mobile terminal MetaTrader 5 for iPhone is used for generating one-time passwords.  
PERMISSION_RISK_WARNING | 0x00000010 | If this flag is enabled, when a client connects in the trading terminal, a warning about the risks associated with operations on the financial markets appears. Trade operations on a client's account are not allowed until the client confirms that he or she has read the warning and is aware of the risks. To confirm, the client should check "I am aware of the risks and I wish to trade high risk investment products". This warning is displayed once per session of the terminal. The next time it will appear after the restart of the terminal.  
PERMISSION_REGULATION_PROTECT | 0x00000020 | Enforce country-specific regulatory restrictions for retail clients. Every country has regulators — state bodies that supervise the activities of financial institutions (including brokers). Each regulator has its own set of requirements applied to trading currencies, securities and other instruments. In most cases, clients of brokerage firms are individuals from different countries. The platform provides the means of meeting the requirements of certain regulators without interfering with the work of traders not covered with these requirements. Restrictions applied to trader accounts depend on the client's country and other conditions set by that country's regulator. For example, the National Securities Market Commission (Comisión Nacional del Mercado de Valores) of Spain compels brokers to warn clients using the leverage of 1:10 or higher about potential risks in a special way. Therefore, if a client's country is Spain and they use a leverage of 1:10 or higher, an additional warning is displayed in the trading dialog Currently, only one regional limitation is used in the platform. The list is to be expanded later.  
PERMISSION_NOTIFY_DEALS | 0x00000040 | Allow accounts to subscribe to [server push notifications  (#push)](../../../../Platform-Setup/Groups/Group-Settings.md#push) about deals.  
PERMISSION_NOTIFY_ORDERS | 0x00000080 | Allow accounts to subscribe to server push notifications about orders.  
PERMISSION_NOTIFY_BALANCES | 0x00000100 | Allow accounts to subscribe to server push notifications about balance operations.  
  
<a id="enauthmode"></a>
## EnAuthMode (#enauthmode)

Types of authorization of clients in the group are listed in EnAuthMode.

ID | Value | Description  
AUTH_STANDARD | 0 | Standard authorization.  
AUTH_RSA1024 | 1 | Extended authorization with 1024-bit encryption.  
AUTH_RSA2048 | 2 | Extended authorization with 2048-bit encryption.  
  
<a id="enreportsmode"></a>
## EnReportsMode (#enreportsmode)

Report generation modes are listed in EnReportsMode.

ID | Value | Description  
REPORTS_DISABLED | 0 | Reports are disabled.  
REPORTS_FULL | 1 | The platform can save the end-of-day and/or end-of-month states of accounts to a special database. The information includes balance, equity, margin, and other details. The database is located on the trade server, in the bases\daily\daily_*.dat file. Data from the file is used in end-of-day and end-of-month trading reports sent to clients, as well as in some manager reports. If the mode is enabled, the platform will save information on accounts from the selected group to the database. This flag enables the generation of both end-of-day and end-of-month data.  
REPORTS_DAY_ONLY | 2 | Enable data generation for reports only at the end of the day.  
REPORTS_MONTH_ONLY | 3 | Enable data generation for reports only at the end of the month.  
  
<a id="enreportsflags"></a>
## EnReportsFlags (#enreportsflags)

Report generation options are listed in IMTConGroup::EnReportsFlags.

ID | Value | Description  
REPORTSFLAGS_NONE | 0 | No additional options enabled.  
REPORTSFLAGS_EMAIL | 1 | Enables sending of generated HTML report files to clients by email. Addresses from [trading accounts (#personal)](../../../../Platform-Setup/Accounts/Editing-Account.md#personal) are used for sending.  
REPORTSFLAGS_SUPPORT | 2 | Enables sending of report copies to a [technical support email address (#support-email)](../../../../Platform-Setup/Groups/Group-Settings.md#support-email).  
REPORTSFLAGS_STATEMENTS | 4 | Enables account state report generation. The HTML report files are created using templates from the \templates\confirmation\ and \templates\statement\ folders on the trade server. The generate reports, the [REPORTS_STANDARD (#enreportsmode)](Enumerations.md#enreportsmode) mode must be enabled.  
  
<a id="ennewsmode"></a>
## EnNewsMode (#ennewsmode)

Modes of news sending are listed in EnNewsMode.

ID | Value | Description  
NEWS_MODE_DISABLED | 0 | News sending is disabled.  
NEWS_MODE_HEADERS | 1 | Only news headers.  
NEWS_MODE_FULL | 2 | Fill package.  
  
<a id="enmailmode"></a>
## EnMailMode (#enmailmode)

Modes of using the internal mail system are listed in EnMailMode.

ID | Value | Description  
MAIL_MODE_DISABLED | 0 | Disable the internal mail system.  
MAIL_MODE_FULL | 1 | Enable the internal mail system.  
  
<a id="enhistorylimit"></a>
## EnHistoryLimit (#enhistorylimit)

The intervals of trading history available to clients in the group are listed in EnHistoryLimit.

ID | Value | Description  
TRADE_HISTORY_ALL | 0 | The entire history.  
TRADE_HISTORY_MONTHS_1 | 1 | One month.  
TRADE_HISTORY_MONTHS_3 | 2 | Three months.  
TRADE_HISTORY_MONTHS_6 | 3 | Six months.  
TRADE_HISTORY_YEAR_1 | 4 | One year.  
TRADE_HISTORY_YEAR_2 | 5 | Two years.  
TRADE_HISTORY_YEAR_3 | 6 | Three years.  
  
<a id="enfreemarginmode"></a>
## EnFreeMarginMode (#enfreemarginmode)

Modes of using the floating profit/loss in the free margin are listed in EnFreeMarginMode.

ID | Value | Description  
FREE_MARGIN_NOT_USE_PL | 0 | Do not use unrealized profit/loss.  
FREE_MARGIN_USE_PL | 1 | Use unrealized profit/loss.  
FREE_MARGIN_PROFIT | 2 | Use unrealized profit.  
FREE_MARGIN_LOSS | 3 | Use unrealized loss.  
  
<a id="enstopoutmode"></a>
## EnStopOutMode (#enstopoutmode)

Modes for checking Margin Call and Stop Out are listed in EnStopOutMode.

ID | Value | Description  
STOPOUT_PERCENT | 0 | The levels of Margin Call and Stop Out in percentage terms.  
STOPOUT_MONEY | 1 | The levels of Margin Call and Stop Out in money terms.  
  
<a id="entradeflags"></a>
## EnTradeFlags (#entradeflags)

Group trade options are enumerated in EnTradeFlags.

ID | Value | Description  
TRADEFLAGS_NONE | 0x00000000 | Options are disabled.  
TRADEFLAGS_SWAPS | 0x00000001 | Allow charging of swaps.  
TRADEFLAGS_TRAILING | 0x00000002 | Enable trailing stop.  
TRADEFLAGS_EXPERTS | 0x00000004 | Enable trading using Expert Advisors.  
TRADEFLAGS_EXPIRATION | 0x00000008 | Enable order expiration.  
TRADEFLAGS_SIGNALS_ALL | 0x00000010 | Allow using the ["Signals"](https://www.mql5.com/en/signals "Signals in MetaTrader") service in the client terminals.  
TRADEFLAGS_SIGNALS_OWN | 0x00000020 | Allow using the [signals](https://www.mql5.com/en/signals "Signals in MetaTrader") from own servers only. If this flag is set, clients in this groups will be able to subscribe only to the signals created on the basis of accounts opened in your brokerage company. Signals created on the basis of other accounts will not be displayed in the client terminals.   
TRADEFLAGS_SO_COMPENSATION | 0x00000040 | Automatically execute on a client's account the special "so compensation" operation, which increases the balance and sets it to zero, if the balance has become negative after a position was closed by Stop Out. For more details please read the [corresponding section (#compensate)](../../../../Platform-Setup/Groups/Group-Settings.md#compensate).  
TRADEFLAGS_SO_FULLY_HEDGED | 0x00000080 | If the flag is enabled, then Stop out will be performed on accounts having open positions, the zero margin (positions are covered) and negative equity. If the option is disabled, orders and positions will not be forcibly closed in above cases. The flag can be only used on [hedging accounts (#hedging)](../../../../Platform-Setup/Groups/Position-Accounting-Systems.md#hedging).  
TRADEFLAGS_FIFO_CLOSE | 0x00000100 | The position closing mode by FIFO rule. If the flag is enabled, then positions for each instrument can only be closed only in the order in which they were opened: the oldest one should be closed first, then the next one, etc. The option is only valid for hedging accounts, in which traders can have multiple positions for the same financial instrument. There are three main methods to close a position; the flag behavior will be different for each of the methods:

  * Closing from the client terminal: the trader closes the position manually, using a trading robot, based on the Signals service subscription, etc. In case of an attempt to close a position, which does not meet the FIFO rule, the trader will receive an appropriate error.
  * Closing upon Stop Loss or Take Profit activation: these orders are processed on the server side, so the position closure is not requested on the trader (terminal) side, but is initiated by the server. If Stop Loss or Take Profit triggers for a position, and this position does not comply with the FIFO rule (there is an older position fro the same symbol), the position will not be closed. An appropriate message will be printed to the log: "position close prohibited by FIFO rule, position #100448219 buy 3.00 EURUSD 1.11544 sl: 1.11537 tp: 1.11549 take profit activation skipped".
  * Closing upon Stop Out triggering: such operations are also processed on the server side. In a normal mode, in which FIFO-based closing is disabled, in case of [Stop Out (#stopout-processing)](../../../../Platform-Setup/Groups/Group-Settings.md#stopout-processing) positions are closed starting with the one having the largest loss. If this option option is enabled, the open time will be additionally checked for losing positions. The server determines losing positions for each symbol, finds the oldest position for each symbol, and then closes the one which has the greatest loss among the found positions.

  
TRADEFLAGS_HEDGE_PROHIBIT | 0x00000200 | Prohibit opening of opposite positions and placing of opposite orders. If this option is enabled, accounts are not allowed to have oppositely directed positions and orders for the same financial instrument. For example, if the account has a Buy position, then the user cannot open a Sell position or place a pending sell order for the same symbol. If such an attempt is made, the user will receive an error. The option is only valid for groups with the [hedging (#hedging)](../../../../Platform-Setup/Groups/Position-Accounting-Systems.md#hedging) position accounting mode.  
TRADEFLAGS_DEAL_COST | 0x00000400 | Calculate deal execution [costs (#deal-cost)](../../../../Platform-Setup/Groups/Group-Settings.md#deal-cost) and display them in client terminals. All NFA regulated brokers should enable this option.  
TRADEFLAGS_SO_COMPENSATION_CREDIT | 0x00000800 | Works as an addition to the TRADEFLAGS_SO_COMPENSATION flag. If enabled, the credit funds on the account will be set to zero after a negative balance compensation operation. [Credit funds (#so-credit)](../../../../Platform-Setup/Groups/Group-Settings.md#so-credit) are withdrawn in a separate balance operation with the "so credit compensation" type.  
  
<a id="enmarginfreeprofitflags"></a>
## EnMarginFreeProfitFlags (#enmarginfreeprofitflags)

Modes of using of the profit/loss fixed during a trade day in the free margin are enumerated in EnMarginFreeProfitFlags.

ID | Value | Description  
FREE_MARGIN_PROFIT_PL | 0 | Include both profit and loss fixed during a day in the free margin.  
FREE_MARGIN_PROFIT_LOSS | 1 | Include onlyInclude only loss fixed during a day in the free margin. The profits of the client during a trading day are accumulated in the [BlockedProfit](../mt5-accounts.md) field of the trade account and are not included in the free margin. At the end of the trading day, the accumulated profits are credited to the balance and the value of IMTAccount::BlockedProfit is reset. fixed during a day in the free margin.  
  
<a id="enmarginmode"></a>
## EnMarginMode (#enmarginmode)

The models of risk management are enumerated in EnMarginMode. The model defines the type of pre-trade control and the position accounting system used.

ID | Value | Description  
MARGIN_MODE_RETAIL | 0 | Used for the OTC market. Margin calculation is based on the type of instrument, as well as group settings. Netting position accounting system is used.  
MARGIN_MODE_EXCHANGE_DISCOUNT | 1 | Used for the exchange market. Margin calculation is based on the discounts specified in symbol settings. Discounts are set by the broker, however they cannot be lower than the exchange set values.  
MARGIN_MODE_RETAIL_HEDGED | 2 | Used for the OTC market. Margin calculation is based on the type of instrument, as well as group settings. Hedging position accounting system is used.  
  
<a id="enmarginflags"></a>
## EnMarginFlags (#enmarginflags)

EnMarginFlags contains the margin calculation flags.

ID | Value | Description  
MARGIN_FLAGS_NONE | 0 | No flags.  
MARGIN_FLAGS_CLEAR_ACC | 1 | The flag is available only in the [FREE_MARGIN_PROFIT_LOSS (#enmarginfreeprofitflags)](Enumerations.md#enmarginfreeprofitflags) mode. If enabled, the profit accumulated by a client will be released (and thus included in the free margin) at the end of trade day. If this flag is disabled, then it will be possible to release the accumulated profit only using an external application (for example, a gateway). The server will not perform this operation.
