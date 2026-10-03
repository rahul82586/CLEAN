[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_groups

[Previous](mt5-symbols-sessions.md) | [Next](mt5-groups/Enumerations.md)

# mt5_groups

[Groups'](../../../Platform-Setup/Groups.md) configurations are exported to the table. The table contains the following fields:

Name | Type | Description  
Group_ID | Integer | Primary key. Unique group ID for more efficient request of the group data from the database. Assigned automatically during the export.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
Group | String | The name of a group, including a path to it in accordance with the hierarchy.  
Server | Integer | The ID of the trade server, to which the group is linked.  
PermissionFlags | Integer | Flags of group permissions. Passed as a value of the [EnPermissionsFlags (#enpermissionsflags)](mt5-groups/Enumerations.md#enpermissionsflags) enumeration (sum of values of appropriate flags).  
AuthMode | Integer | Authorization mode for accounts in the group. Passed in a value of the [EnAuthMode (#enauthmode)](mt5-groups/Enumerations.md#enauthmode) enumeration.  
AuthPasswordMin | Integer | The minimum password length for accounts in the group.  
Company | String | Name of the company that services the group.  
CompanyPage | String | The website address of the company that services the group.  
CompanyEmail | String | The email address of the company that services the group.  
CompanySupportPage | String | The technical support website address of the company that services the group.  
CompanySupportEmail | String | The technical support email address of the company that services the group.  
CompanyCatalog | String | The name of the subdirectory that stores the templates of reports, emails, etc. for the company that services this group.  
Currency | String | The group deposit currency.  
CurrencyDigits | Integer | The number of digits after the decimal point in the group deposit currency.  
ReportsMode | Integer | Report generation modes. Passed in a value of the [EnReportsMode (#enreportsmode)](mt5-groups/Enumerations.md#enreportsmode) enumeration.  
ReportsFlags | Integer | Report sending options. Passed as a value of the [EnReportFlags (#enreportsflags)](mt5-groups/Enumerations.md#enreportsflags) enumeration (sum of values of appropriate flags).  
ReportsEmail | String | [The mail server](../../../Platform-Setup/Integrations/Mail-Servers.md) used for sending reports to clients from the group.  
ReportsSMTP | String | Address of SMTP server for sending reports. The field is obsolete and is not updated.  
ReportsSMTPLogin | String | A login for the authorization on the SMTP server that is used for sending reports. The field is obsolete and is not updated.  
NewsMode | Integer | The mode of news sending to the clients from the group. Passed in a value of the [EnNewsMode (#ennewsmode)](mt5-groups/Enumerations.md#ennewsmode) enumeration.  
NewsCategory | String | The categories of news received by the group. Use the backslash character "\" to specify subcategories.  
NewsLangs | Array of integer numbers | The array of languages, in which the group receives news. The language is specified in the LANGID format used in the [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (value from Prim.lang.identifier).  
MailMode | Integer | The mode of operation of the internal mail system for the group. Passed in a value of the [EnMailMode (#enmailmode)](mt5-groups/Enumerations.md#enmailmode) enumeration.  
TradeFlags | Integer | Trade options of the group. Passed as a value of the [EnTradeFlags (#entradeflags)](mt5-groups/Enumerations.md#entradeflags) enumeration (sum of values of appropriate flags).  
TradeInterestrate | Float | The annual interest rate on deposits of the group accounts.  
TradeVirtualCredit | Float | The amount of additional funds that a brokerage company can provide to a client for opening a position with a volume larger than allowed by the client's current funds.  
MarginFreeMode | Integer | The mode of using of floating profit/loss in the free margin. Passed in a value of the [EnFreeMarginMode (#enfreemarginmode)](mt5-groups/Enumerations.md#enfreemarginmode) enumeration.  
MarginSOMode | Integer | The mode of checking the levels of Stop Out and Margin Call. Passed in a value of the [EnStopOutMode (#enstopoutmode)](mt5-groups/Enumerations.md#enstopoutmode) enumeration.  
MarginCall | Float | The level of Margin Call. Units are determined by the MarginSOMode parameter.  
MarginStopOut | Float | The level of Stop Out. Units are determined by the MarginSOMode parameter.  
MarginFreeProfitMode | Integer | The mode of using the profit/loss fixed during a trade day in the free margin.  
MarginMode | Integer | The risk management model of the group.  
MarginFlags | Integer | Margin calculation flags.  
DemoLeverage | Integer | The default credit leverage for demo accounts opened in the group.  
DemoDeposit | Float | The default amount of deposit for demo accounts opened in the group.  
LimitHistory | Integer | The maximum number of days, for which the group can request data on conducted trade operation. Passed in a value of the [EnHistoryLimit (#enhistorylimit)](mt5-groups/Enumerations.md#enhistorylimit) enumeration.  
LimitOrders | Integer | The maximum number of orders that can be simultaneously placed by an account from this group.  
LimitSymbols | Integer | The maximum number of symbols, for which an account can simultaneously receive quotes.  
LimitPositions | Integer | The maximum number of open positions which the client can have on the account at the same time.  
LimitPositionsVolume | Float | Currently the field is not used.  
TradeTransferMode | Integer | The mode of transferring funds between accounts.
