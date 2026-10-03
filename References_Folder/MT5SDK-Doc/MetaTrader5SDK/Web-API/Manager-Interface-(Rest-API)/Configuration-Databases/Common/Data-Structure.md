[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Data Structure

[Previous](../Common.md) | [Next](Get.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

The common configuration is passed in JSON format in response to [/api/common/get](../Common.md) and [/api/common/set](Set.md) requests. The common configuration includes the following parameters:

Option Field | Type | Description  
Name | String | Server name.  
NameFull | String | The full name of the server.  
Owner | String | The name of the platform owner.  
OwnerID | String | The short name of the platform owner.  
OwnerHost | String | The host address of the platform owner.  
OwnerEmail | String | The email address of the owner of the platform.  
Product | String | The full name of the product.  
ExpirationLicense | Integer | The license expiry date.  
ExpirationSupport | Integer | The date of technical support expiration is specified in the license.  
LimitTradeServers | Integer | The maximum number of trade servers.  
LimitWebServers | Integer | The maximum number of web servers.  
LimitAccounts | Integer | The maximum number of accounts that can be opened in the trading platform.  
LimitDeals | Integer | The maximum number of deals that can be committed in the trading platform.  
LimitGroups | Integer | The maximum number of groups that can be created in the trading platform.  
LiveUpdateMode | Integer | The mode of updating the trading platform components. To pass the mode, the [EnUpdateMode](../../../../Configuration-Interfaces/Common/IMTConCommon/IMTCon-Enumerations.md) enumeration is used.  
TotalUsers | Integer | The total number of client records in the entire trading platform.  
TotalUsersReal | Integer | The total number of real clients in the entire trading platform.  
TotalDeals | Integer | The total number of deals executed in the entire trading platform.  
TotalOrders | Integer | The total number of active orders placed in the entire trading platform.  
TotalOrdersHistory | Integer | The total number of historic orders in the entire trading platform.  
TotalPositions | Integer | The total number of positions in the entire trading platform.  
AccountURL | String | The address a client is redirected to when opening a demo account from the client terminal.  
AccountDepositURL | String | Deposit page URL for all accounts in the platform.  
AccountWithdrawalURL | String | Withdrawal page URL for all accounts in the platform.  
AccountAuto | Integer | A sign of automatic allocation of demo accounts at client terminal launch: 0 — disabled, 1 — enabled.  
AccountGroup | Array of objects | Array of objects describing [demo account allocation group](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups) settings.  
  
Groups for allocating demo account

Parameter | Type | Description  
Group | String | The name of the group in which accounts are allocated.  
Description | String | Description for the "Account type" fields in terminals.  
Company | String | The name of the company, in which terminals the group will be available.  
Currency | String | Deposit currency.  
CurrencyDigits | Integer | Deposit currency accuracy.  
AccountType | Integer | Type of accounts in the group: 0 — preliminary, 1 — real, 2 — demo.  
DefaultLeverage | Float | List of available leverages.  
Countries | String | List of countries, in which the group will be available to clients.  
ConfirmationEmail | String | [Mail configuration](../../../../Configuration-Interfaces/Mail-Servers.md) name, via which confirmation emails will be sent.  
Agreements | Array of strings | Array with the description of [agreements (#agreements)](Data-Structure.md#agreements).  
  
<a id="agreements"></a>
## Agreements (#agreements)

Parameter | Type | Description  
CaptionType | Integer | Agreement type:

  * 1 — client agreement
  * 2 — risk disclaimer
  * 3 — client agreement and risk disclaimer
  * 4 — complaint handling procedure
  * 5 — order execution policy
  * 6 — client categorization procedure
  * 7 — conflict of interest clause
  * 8 — other (custom option)

  
CaptionCustom | String | Agreement name for CaptionType = 8.  
URL | String | Link to agreement.
