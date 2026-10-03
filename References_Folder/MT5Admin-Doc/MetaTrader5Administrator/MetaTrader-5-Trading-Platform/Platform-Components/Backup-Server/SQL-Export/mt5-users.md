[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_users

[Previous](mt5-documents.md) | [Next](mt5-users/Enumerations.md)

# mt5_users

Data on [account](../../../Platform-Setup/Accounts.md) database is exported to the table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Primary key. The login of a user.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
TimestampTrade | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
Group | String | User group.  
CertSerialNumber | Integer | The number of a last used certificate for user authorization.  
Rights | Integer | Flags of the users permissions. Passed using a value of the [EnUserRights (#enusersrights)](mt5-users/Enumerations.md#enusersrights) enumeration (sum of values of appropriate flags).  
Registration | DateTime | Time of a client record generation in the YYYY-MM-DD HH:MM:SS format.  
LastAccess | DateTime | The date of the last connection using an account in the YYYY-MM-DD HH:MM:SS format. This field is not updated in real time, in order to save traffic and reduce the load on the platform. The value is only updated when the user connects to the platform, if more than 24 hours have passed since the previous connection.  
LastPassChange | DateTime | The date of the last password change.  
LastIP | String | The IP address from which the user last connected to the server.  
Name | String | The name of the user. Obsolete field.  
FirstName | String | The first name of the client.  
LastName | String | The last name of the client.  
MiddleName | String | The middle name of the client.  
Company | String | The name of user's company.  
Account | String | The number of a user's account in an external bank.  
Country | String | The user's country of residence.  
Language | Integer | User's language in the format LANGID used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (value from Prim.lang.identifier).  
ClientID | Integer | The identifier of the [client](../../../Platform-Setup/Clients.md), to whom the trading account corresponds.  
City | String | The user's city of residence.  
State | String | The user's state (region) of residence.  
ZIPCode | String | The user's zip code.  
Address | String | The address of the user.  
Phone | String | The user's phone number.  
EMail | String | The email address of the user.  
ID | String | The number of a user's identity document.  
Status | String | Client's status.  
Comment | String | A comment to the user.  
Color | COLORREF | The color of the user. This is the color of the user's requests shown when handling the requests via the manager terminal.  
PhonePassword | String | The user's phone password.  
Leverage | Integer | The size of a user's leverage.  
Agent | Integer | Agent account number of the user.  
Balance | Float | The current balance of a user.  
Credit | Float | The current amount of funds credited to the user.  
InterestRate | Float | The amount accrued for the current month calculated based on the annual interest rate.  
CommissionDaily | Float | The amount of commissions charged from the user for a day.  
CommissionMonthly | Float | The total amount of commissions charged from the user for the current month.  
BalancePrevDay | Float | The value of the user's balance as of the end of the previous day.  
BalancePrevMonth | Float | The value of a user's balance as of the end of the previous trading month.  
EquityPrevDay | Float | The user's equity as of the end of the previous day.  
EquityPrevMonth | Float | The value of the user's equity as of the end of the previous trading month.  
TradeAccounts | String | Account numbers in external trading systems and gateway identifiers used for working with that systems. The string format is: gateway_ID=account_number|gateway_ID=account_number...  
MQID | String | MetaQuotes ID of the user.  
LeadCampaign | String | Name of the [marketing campaign (#leadsource)](../../../Platform-Setup/Accounts/Editing-Account.md#leadsource) a client was attracted by.  
LeadSource | String | [Lead source (#leadsource)](../../../Platform-Setup/Accounts/Editing-Account.md#leadsource) (address of the website a client has come from).  
ApiData | String | User data which can be added via MetaTrader 5 API. Sample user data entry: [{pos:0,app_id:1,valInt:500,valUInt:500,valDbl:0.00000000}]. It specifies the user data index, the ID of the application that added it, as well as the data of three types: Int, UInt and double. The string may contain up to 16 such entries.  
LimitOrders | Integer | The maximum number of active (placed) pending orders allowed on the account.  
LimitPositions | Integer | Maximum value of open positions allowed on the account.
