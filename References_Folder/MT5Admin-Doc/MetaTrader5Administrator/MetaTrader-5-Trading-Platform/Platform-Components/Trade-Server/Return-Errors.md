[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Trade Server](../Trade-Server.md) / Return Errors

[Previous](SendMail-Utility.md) | [Next](../Access-Server.md)

# Return Errors

When an attempt is made to perform invalid operations, a trade server returns errors to terminals. They are displayed on the ["Journal"](../../MetaTrader-5-Administrator/User-Interface/Toolbox/Journal.md) tab of the "Toolbox" window, as well as in [journals of servers](../../Platform-Setup/Network-cluster/Journal.md).

## Common Errors

Error | Description  
---|---  
Common error | Error not included to any of categories listed below.  
Invalid parameters | Incorrect parameters are specified at the attempt to change any of configurations.  
Disk error | This error occurs when it is impossible to write information on a disk.  
Memory error | This error indicates that there is not enough memory.  
Network error | This error is shown when a failure occurs in the network interaction of the platform components.  
Not enough permissions | This error occurs when a manager/administrator attempts to perform an action, for which he or she doesn't have enough [permissions (#permissions)](../../Platform-Setup/Managers.md#permissions).  
Operation timeout | The error means that the operation fulfillment waiting period is over.  
No connection | Connection to the server couldn't be established.  
Service is not available | This error can appear when information is requested from one of the platform components that is currently unavailable.  
Too frequent requests | The error occurs if requests to the server are made to often.  
Not found | Requested information was not found.  
  
## Authorization Errors

Error | Description  
---|---  
Invalid terminal type | This error can occur at the attempt to connect using a [manager](../../Platform-Setup/Managers.md) group account via the client terminal or vice versa - connect from manager/administrator terminal using an account from a common [group](../../Platform-Setup/Groups.md).  
Invalid account | This error appears if invalid account number or incorrect password are specified during [authorization](../../MetaTrader-5-Administrator/Getting-Started/Connect-to-Server.md).  
Unknown account | This error appears if a user tries to authorize using an account that is created on a trade server, connection to which is [prohibited for the access server (#servers)](../../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md#servers). Due to it, the access server cannot identify the account and denies its connection.  
Account disabled | The error appears at the attempt to connect using a [disabled (#enable)](../../Platform-Setup/Accounts/Editing-Account.md#enable) account.  
Advanced authorization | This message indicates that the procedure of [extended authorization](../../MetaTrader-5-Administrator/Getting-Started/Connect-to-Server/Extended-Authorization.md) must be performed for connecting.  
Certificate required | This message is shown at the attempt to to connect using the account that requires a SSL certificate to be generated in order to connect.  
Invalid certificate | This message appears at the attempt to connect using a certificate that is invalid for this account. For example, if it was [reset (#authorization)](../../Platform-Setup/Accounts/Editing-Account.md#authorization) on the server.  
Certificate is not confirmed | The message is shown at the attempt to connect using an [unconfirmed (#authorization)](../../Platform-Setup/Accounts/Editing-Account.md#authorization) certificate.  
Attempt to connect to non-access server | This error means that an attempt is made to connect to one of the platform components directly, bypassing the [access server](../Access-Server.md).  
Invalid or fake server | The error indicates that the server, to which there was an attempt to connect, is invalid.  
Only updates available | This error is shown when an attempt is made to connect to the [history server](../History-Server.md) at the time when only connecting to it for obtaining updates is allowed. This situation can appear during the platform update, when the server has been updated and is operating, but its configurations are not yet synchronized with the [main trade server](../Trade-Server.md).  
Old version | It indicates that the version of the component is old.  
Account doesn't have manager config | The error occurs at the attempt to connect using the account for which no [manager](../../Platform-Setup/Managers.md) configurations have been created.  
IP address unallowed for manager | The error occurs at the attempt of a manager connection from an [unallowed IP address (#access-list)](../../Platform-Setup/Managers.md#access-list).  
Group is not initialized | The error occurs at the attempt to create an account in the [group](../../Platform-Setup/Groups.md) that hasn't been initialized yet. In order to initialize a group after it has been created, the trade server needs to be [restarted](../../Platform-Setup/Network-cluster/Restarting-and-Stopping-Servers.md).  
Certificate generation disabled | The error occurs if the terminal requests generation of a new SSL certificate, but the possibility of their automatic generation is disabled on the server.  
  
## Configuration Management Errors

Error | Description  
---|---  
Last admin config deleting | The error appears at the attempt to delete the last [manager configuration](../../Platform-Setup/Managers.md).  
Last admin group cannot be deleted | The error appears at the attempt to delete the last administrator [group](../../Platform-Setup/Groups.md).  
Accounts or trades in group | The error appears at the attempt to delete a [group](../../Platform-Setup/Groups.md) that contains [accounts](../../Platform-Setup/Accounts.md) or [trade operations](../../Platform-Setup/Positions.md).  
Invalid accounts or trades ranges | The error appears at the attempt to set the range of [accounts (#accounts)](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#accounts), [orders (#orders)](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#orders) or [deals (#deals)](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#deals) for a trade server that coincide with the same ranges on other servers.  
Account is not from manager group | The error occurs at the attempt to create a [manager configuration](../../Platform-Setup/Managers.md) based on the account that does not belong to the manager group.  
Built-in protected config | The error occurs at the attempt to delete a built-in configuration of collection of the server [performance parameters](../../Platform-Setup/Network-cluster/Monitor.md).   
Configuration duplicate | This error is shown when an attempt is made to add the second [main trade server](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md) or a [history server](../../Platform-Setup/Network-cluster/Configuring-Servers/History-Server.md) in the "Network" section.  
Configuration limit reached | This error appears at the attempt to create a new configuration, when the limit to their creation is reached. This can happen if the license was [not activated](../../Platform-Installation/Activation.md). In this case the number of [groups](../../Platform-Setup/Groups.md), for example, is limited to five.  
Invalid network configuration | This error appears at the attempt to save such [network settings](../../Platform-Setup/Network-cluster.md) that the administrator will not be able no connect to the main trade server.  
  
## Account Management Errors

Error | Description  
---|---  
Last admin account deleting | This error appears at the attempt to delete the last [manager](../../Platform-Setup/Managers.md) account.  
Logins range exhausted | The error appears at the attempt to create an account when the [range of allowed accounts (#accounts)](../../Platform-Setup/Network-cluster/Configuring-Servers/Trade-Server.md#accounts) was exhausted.  
Login reserved at another server | This error appears at the attempt to [create an account](../../Platform-Setup/Accounts/Creating-Account.md) via a manager or administrator terminal with the login that already exists on another server.  
Account already exists | The error appears at the attempt to [create an account](../../Platform-Setup/Accounts/Creating-Account.md) with already existing login.  
Attempt of self-deletion | The error appears if an administrator is trying to delete his or her own account via the administrator terminal.  
Invalid account password | The error appears if incorrect password was specified during [password verification (#password)](../../Platform-Setup/Accounts/Editing-Account.md#password).  
Users limit reached | The error appears at the attempt to create a new [account](../../Platform-Setup/Accounts.md) when their limit is over. The situation is possible when the license was [not activated](../../Platform-Installation/Activation.md).  
Account has open trades | The error appears at the attempt to delete an account with [open positions](../../Platform-Setup/Positions.md).  
Attempt to move account to different server | The error appears at the attempt to move an [account](../../Platform-Setup/Accounts.md) to the group that belongs to [another trade server (#trade-server)](../../Platform-Setup/Groups/Group-Settings.md#trade-server).  
Attempt to move account to different currency group | The error appears at the attempt to move an account to the group with a different [deposit currency (#currency)](../../Platform-Setup/Groups/Group-Settings.md#currency).  
  
## State of Trade Requests

Error | Description  
---|---  
Request on the way | The request has been sent to a server but it hasn't accepted it yet.  
Request accepted | The request has been accepted by the server and is waiting to be processed.  
Request processed | The server has started to process the request.  
Requote | Requoting as a reply to a client's request to execute a trade operation.  
Prices | Sending prices.  
Request rejected | The request is rejected by the server or dealer.  
Request canceled | the request was canceled by the server, dealer or client.  
Order placed | The order has been placed and is waiting till the specified processing conditions appear.  
Request executed | The requested operation has been executed.  
Request executed partly | The requested operation has been executed partially. E.g. a [deal](../../Platform-Setup/Deals.md) on the part of volume specified in the [order](../../Platform-Setup/Orders.md) is executed.  
Request error | Error of request execution.  
Request timeout | Time of request execution waiting is over.  
Invalid request | The request didn't pass the common validation procedure.  
Invalid volume | Incorrect volume is specified in the request.  
Invalid price | Incorrect price is specified in the request.  
Invalid stops | Incorrect Take Profit and Stop Loss levels are specified in the request.  
Trade disabled | Trading is [disabled (#trading)](../../Platform-Setup/Accounts/Editing-Account.md#trading) for this account.  
Market closed | The error appears at the attempt to execute trade operations beyond the allowed period (both [common trading hours (#daylight-saving)](../../Platform-Setup/Time.md#daylight-saving) and [trade sessions](../../Platform-Setup/Symbols/Symbol-Settings/Sessions.md) of separate symbols).  
No money | Attempt to execute a trade operations, when there is not enough money for its execution.  
Price changed | The error appears when the [maximal deviation (#max-deviation)](../../Platform-Setup/Symbols/Symbol-Settings/Execution.md#max-deviation) of the current price at the request price is exceeded.  
No prices | The error appears when there is no thread of quotes.  
Invalid expiration | The error occurs at the attempt to place an order with an incorrect [expiration (#expiration)](../../Platform-Setup/Orders.md#expiration) date.  
Order has been changed already | The error appears at the attempt to modify an order, which has been simultaneously modified.  
Too many trade requests | The error appears if trade requests are sent too often to the server.  
AutoTrading disabled by server | This error indicates that trading of [Expert Advisors (#ea-trading)](../../Platform-Setup/Accounts/Editing-Account.md#ea-trading) on this account is prohibited.  
AutoTrading disabled by client | This error indicates that trading of Expert Advisors is disabled in the client terminal.
