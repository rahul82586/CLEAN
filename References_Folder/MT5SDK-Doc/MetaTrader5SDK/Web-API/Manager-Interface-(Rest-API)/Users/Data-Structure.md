[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Data Structure

[Previous](../Users.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Data on users is passed in JSON format as a response to the [/api/user/add](Add.md), [/api/user/update](Add.md) and [/api/user/get](Get-by-Login.md) requests.

<a id="user"></a>
## User Parameters (#user)

Information about a user includes the following parameters:

Option Field | Type | Description  
Login | Integer | The login of a user.  
Group | String | User group.  
CertSerialNumber | Integer | The number of a last used certificate for user authorization.  
Rights | Integer | Flags of the users permissions. Passed using a value of the [EnUserRights (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) enumeration (sum of values of appropriate flags).  
Registration | Integer | The user record creation date.  
LastAccess | Integer | The date of the last connection using the account.  
LastIP | String | The IP address from which the user last connected to the server.  
LastPassChange | Integer | The date of the last password change.  
Name | String | The name of the client. Obsolete field.  
FirstName | String | The first name of the client.  
LastName | String | The last name of the client.  
MiddleName | String | The middle name of the client.  
Company | String | The name of user's company.  
Account | String | The number of a user's account in an external bank.  
Country | String | The client's country of residence.  
Language | Integer | User's language in the format LANGID used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (value from Prim.lang.identifier).  
City | String | The client's city of residence.  
State | String | The user's state (region) of residence.  
ZIPCode | String | The client's zip code.  
Address | String | The address of the user.  
Phone | String | The user's phone number.  
Email | String | The email address of the user.  
ID | String | The number of a user's identity document.  
Status | String | Client's status.  
Comment | String | A comment to the user.  
Color | Integer | The color of the user. The color of the user. This is the color of the user's requests shown when handling the requests via the manager terminal.  
PhonePassword | String | The user's phone password.  
Leverage | Integer | The size of a user's leverage.  
Agent | Integer | Agent account number of the user.  
Balance | Float | The current balance of a client. The balance cannot be updated via this field when creating or modifying an account. To top up an account, use the [/webapi_trade_balance](../Trading/Trade-Requests/DepositWithdrawal.md) request.  
Credit | Float | The current amount of funds credited to the client.  
InterestRate | Float | The amount accrued for the current month calculated based on the annual interest rate.  
CommissionDaily | Float | The amount of commissions charged from a client for a day.  
CommissionMonthly | Float | The total amount of commissions charged from a client for the current month.  
CommissionAgentDaily | Float | The size of agent commissions charged for a client's trade operations for a day, from a daily report.  
CommissionAgentMonthly | Float | The amount of agent commissions charged for a client's trade operations for the current month.  
BalancePrevDay | Float | Client's balance as of the end of the previous day.  
BalancePrevMonth | Float | Client's balance as of the end of the previous trading month.  
EquityPrevDay | Float | A client's equity as of the end of the previous day.  
EquityPrevMonth | Float | The value of a client's equity as of the end of the previous trading month.  
MQID | String | MetaQuotes ID of the user.  
TradeAccounts | String | User account numbers in external trading systems as [gateway ID]=[account number in the system to which the gateway is connected]. The total length of the accounts and IDs stored for an account is limited to 128 characters (including the end-of-line character). The maximum length of each account is limited to 32 characters (including the end-of-line character). If the total length is exceeded when you add or change the account state, the error code [MT_RET_ERR_DATA](../../../Return-Codes/Common-errors.md) will be returned.  
ApiData | Array | [Array of user data (#apidata)](Data-Structure.md#apidata).  
LeadSource | String | A lead source — a website a client has come from.  
LeadCampaign | String | A lead campaign — name of a marketing campaign a client was attracted by.  
LimitOrders | Integer | The maximum number of active (placed) pending orders allowed on the account.  
LimitPositions | Integer | Maximum value of open positions allowed on the account.  
  
<a id="account"></a>
## Trade Account Parameters (#account)

Information about a trade account includes the following parameters:

Option Field | Type | Description  
Login | Integer | The login of the client, to whom the trading account belongs.  
CurrencyDigits | Integer | The number of digits after the decimal point in the account deposit currency.  
Balance | Float | The balance of a trade account.  
Credit | Float | The current amount of credit given to an account.  
Margin | Float | The current amount of credit given to an account.  
MarginFree | Float | The free margin of an account.  
MarginLevel | Float | The margin level as a percentage. It is calculated as a percentage of the current account equity (Equity) to the margin volume (Margin).  
MarginLeverage | Integer | Margin leverage.  
MarginInitial | Float | The current size of the initial margin of positions on a trading account.  
MarginMaintenance | Float | The current size of the maintenance margin of positions on a trading account.  
Profit | Float | The size of the current profit for all open positions.  
Storage | Float | The current size of swaps charged for open positions on the account.  
Floating | Float | The size of floating profit/loss of open positions on the account. The floating profit/loss is calculated as the sum of Profit, Storage and Commission of open positions on the account.  
Equity | Float | The account equity calculated as a sum of Balance, Credit and Floating.  
SOActivation | Integer | The account status as per the minimum amount of funds on the account required to maintain trading positions. Passed using a value of the [EnSoActivation (#ensoactivation)](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Enumerations.md#ensoactivation) enumeration.  
SOTime | Integer | The time when the Margin Call or Stop Out level was reached , in seconds that had elapsed since 01.01.1970.  
SOLevel | Float | The margin level of an account at the time it reaches the Stop Out level.  
SOEquity | Float | The equity of an account at the time it reaches the Stop Out level.  
SOMargin | Float | The volume of margin on the account at the time it reaches the Stop Out level.  
BlockedCommission | Float | The amount of the standard commission locked on the account, which has been accumulated during the day/month.  
BlockedProfit | Float | The amount of intraday profit locked on the account.  
Assets | Float | The current total amount of assets on a trading account.  
Liabilities | Float | The current total amount of liabilities on a trading account.  
  
<a id="apidata"></a>
## User data (#apidata)

Parameter | Type | Description  
AppID | Integer | The identifier of the application that recorded the data.  
ID | Integer | Data identifier.  
ValueInt | Integer | The user parameter value of the int type.  
ValueUint | Integer | The user parameter value of the uint type.  
ValueDouble | Float | The user parameter value of the double type.
