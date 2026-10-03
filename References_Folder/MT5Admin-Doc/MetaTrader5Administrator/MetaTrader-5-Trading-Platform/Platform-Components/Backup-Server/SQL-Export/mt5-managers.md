[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_managers

[Previous](mt5-commissions-tiers.md) | [Next](mt5-clients.md)

# mt5_managers

Data about [manager accounts](../../../Platform-Setup/Managers.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Initial key. The user login, based on which the manager account is created.  
Timestamp | Integer | A unique values within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has changed.  
Name | String | The name of the manager.  
Mailbox | String | The name of the manager's mailbox in the internal mailing system.  
Server | Integer | The ID of the trade server to which the manager belongs.  
RequestLimitLogs | Integer | The time period of system logs that are available to a manager:

  * 0 — unlimited
  * 1 — 1 month
  * 2 — 3 months
  * 3 — 6 months
  * 4 — 1 year
  * 5 — 2 years
  * 6 — 3 years

  
RequestLimitReports | Integer | The time period of reports that are available to a manager:

  * 0 — unlimited
  * 1 — 1 month
  * 2 — 3 months
  * 3 — 6 months
  * 4 — 1 year
  * 5 — 2 years
  * 6 — 3 years

  
Groups | String | The list of groups processed by the manager. The groups are separated by commas, for example: "demo\forex-netting,demo\forex-netting".  
Access | String | The list of IP addresses, from which a manager is allowed to connect to the platform. Example: 192.168.0.1-192.168.0.10,192.168.0.12-192.168.0.20.  
Further fields in the table describe [manager permissions (#permissions)](../../../Platform-Setup/Managers.md#permissions). A value of 1 means that the right is granted to the manager, 0 means no permission.  
Right_Admin | Integer | Connection using the administrator terminal.  
Right_Manager | Integer | Connection using the manager terminal.  
Right_Cfg_Servers | Integer | Network configuration  
Right_Cfg_Access | Integer | Configuration of the list of IP access.  
Right_Cfg_Time | Integer | Configuration of the server working time.  
Right_Cfg_Holidays | Integer | Configuration of holidays.  
Right_Cfg_Groups | Integer | Configuration of groups.  
Right_Cfg_Managers | Integer | Configuration of manager rights.  
Right_Cfg_Requests | Integer | Configuration of the routing table.  
Right_Cfg_Gateways | Integer | Configuration of gateways.  
Right_Cfg_Plugins | Integer | Configuration of plugins.  
Right_Cfg_Datafeeds | Integer | Configuration of data feeds.  
Right_Cfg_Reports | Integer | Configuration of reports.  
Right_Cfg_Symbols | Integer | Configuring the symbols.  
Right_Cfg_Hst_Sync | Integer | Configuration of synchronization.  
Right_Cfg_ECN | Integer | ECN configuration.  
Right_Cfg_VPS | Integer | Configuring Sponsored VPS for traders.  
Right_Cfg_Web_Services | Integer | Configuring integration with web services: SSL certificates and addresses for callback requests.  
Right_Cfg_Funds | Integer | Configuring investment funds in the Administrator terminal  
Right_Cfg_Messengers | Integer | Configuring integration with SMS providers and messengers in the Administrator terminal  
Right_Cfg_KYC | Integer | Configuring integration with KYC services in the Administrator terminal  
Right_Cfg_Automations | Integer | Configuring automatic actions for specified scenarios in the Administrator terminal.  
Right_Cfg_Allocations | Integer | Accessing the Allocations section of the Administrator terminal. The section allows configuring groups, in which traders are able to open demo and preliminary real accounts directly from client terminals.  
Right_Cfg_Corporates | Integer | Access to [corporate link](../../../Platform-Setup/Accounts/Corporate-Links.md) settings.  
Right_Cfg_Payments | Integer | Configuring integration with payment systems.  
Right_Cfg_Mails | Integer | Configuring integration with email services in the Administrator terminal.  
Right_Srv_Journals | Integer | Access to server journals.  
Right_Srv_Reports | Integer | Receiving automatic server reports.  
Right_Charts | Integer | Editing history data on the server.  
Right_Email | Integer | Sending internal emails.  
Right_News | Integer | Permission to send newsletters. An administrator or manager can only send newsletters if his or her account belongs to a group created on the main trade server.  
Right_Export | Integer | Permission to export data.  
Right_Techsupport | Integer | Access to the technical support tab in the administrator and manager terminals. The permission is obsolete and is no longer used.  
Right_Market | Integer | Permission to access the Market of applications in the MetaTrader 5 Administrator. The permission is obsolete and is no longer used.  
Right_Accountant | Integer | Permission to work with funds on accounts.  
Right_Acc_Read | Integer | Access to accounts.  
Right_Acc_Details_Name | Integer | Access to name details in [accounts (#personal)](../../../Platform-Setup/Accounts/Editing-Account.md#personal).  
Right_Acc_Details_Location | Integer | Access to location data in accounts: country, city, region, zip code.  
Right_Acc_Details_Address | Integer | Access to address details in [accounts (#personal)](../../../Platform-Setup/Accounts/Editing-Account.md#personal).  
Right_Acc_Details_ID | Integer | Access to data on document numbers in accounts.  
Right_Acc_Details_EMail | Integer | Access to email details in accounts.  
Right_Acc_Details_Phone | Integer | Access to phone details in accounts.  
Right_Acc_Details_General | Integer | Access to other data in accounts (language, status, comment, MetaQuotes ID, etc.).  
Right_Acc_Technical | Integer | When combined with the "[Show to regular managers (#limits)](../../../Platform-Setup/Accounts/Editing-Account.md#limits)" permission, provides greater convenience when working with various testing and technical accounts. Disable the "Enable visibility for regular managers" permission for all technical accounts, and then disable access to technical accounts for the managers who do not configure the platform. Otherwise, such technical accounts can be confusing for managers working with clients.  
Right_Acc_Tech_Modify | Integer | Allows enabling and disabling the "[Show to regular managers (#limits)](../../../Platform-Setup/Accounts/Editing-Account.md#limits)" and "[Include in server reports (#limits)](../../../Platform-Setup/Accounts/Editing-Account.md#limits)" options for a trading account. Without this permission, the manager can only see the states of the relevant options, without the ability to change them (read-only).  
Right_Acc_Manager | Integer | Account editing.  
Right_Acc_Delete | Integer | Deleting client accounts via the administrator and manager terminals, and via the Manager API. The Right_Acc_Manager permission is required in order to enable this permission.  
Right_Acc_Online | Integer | Getting the current client connections.  
Right_Confirm_Actions | Integer | By default the manager terminal displays a confirmation dialog when performing balance operations on client accounts and closing multiple orders. A manager needs to enter a randomly generated sequence of characters in order to confirm the appropriate action. If this permission is disabled, the above actions will be performed immediately without any confirmation.  
Right_Notifications | Integer | Permission to send push notifications to clients' mobile devices from the manager terminal. Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 5 Mobile for [iPhone](https://download.mql5.com/cdn/mobile/mt5/ios?hl=ru&utm_campaign=download&utm_source=metatrader5.help "iPhone") and [Android](https://download.mql5.com/cdn/mobile/mt5/android?hl=ru&utm_campaign=download&utm_source=metatrader5.help "Android"). For more information please read the MetaTrader 5 Manager user guide.  
Right_Trades_Read | Integer | Viewing trading orders, deals and positions. This right affects the possibility to enable Right_Trades_Manager and Right_Trades_Dealer permissions.  
Right_Trades_Manager | Integer | Changing any fields of orders, deals and positions in the administrator terminal, and changing position open prices in the manager terminal.  
Right_Trades_Delete | Integer | Deleting any orders, deals and positions via the administrator and manager terminals, and via the Manager API. The Right_Trades_Manager permission is required in order to enable this permission.  
Right_Trades_Dealer | Integer | The possibility to perform trading and dealing operations in the manager terminal.  
Right_Trades_Supervisor | Integer | This right allows the manager to view the entire queue of requests received from groups of clients available to the manager, as well as to track processing of requests by other dealers in the manager terminal. Manager works in the "Supervisor" mode without connecting as a dealer in the manager terminal. After connecting as a dealer, the manager will only see the requests that are forwarded to him or her for processing in accordance with the routing rules.  
Right_Quotes_Raw | Integer | If this permission is enabled, the "Show raw quotes" command will appear in the context menu of the Market Watch window in the manager terminal. With this permission, the manager can view quotes without considering spread difference settings set for the manager group.  
Right_Quotes | Integer | Permission to throw in quotes  
Right_Symbol_Details | Integer | Permission to change spread and execution mode.  
Right_Risk_Manager | Integer | Permission to receive information about client's aggregate positions and company's coverage positions.  
Right_Group_Margin | Integer | Permission to configure margin for groups in MetaTrader 5 Manager.  
Right_Group_Commission | Integer | Permission to configure commissions for groups in MetaTrader 5 Manager.  
Right_Reports | Integer | Permission to request and receive various reports on client operations.  
Right_Finteza_Access | Integer | Access to the [Finteza Analytics](../../../Platform-Setup/Integrations.md) section.  
Right_Finteza_Websites | Integer | View Finteza data relating to websites in the Analytics section of the Manager terminal.  
Right_Finteza_Campaigns | Integer | View Finteza data relating to marketing campaigns in the Analytics section of the Manager terminal.  
Right_Finteza_Reports | Integer | The permission is currently not used.  
Right_Clients_Access | Integer | Access to the Clients section in the Administrator and Manager terminals.  
Right_Clients_Create | Integer | Permission to create new client records manually.  
Right_Clients_Edit | Integer | Permission to edit client data, except for documents.  
Right_Clients_Delete | Integer | PermiRight_Clients_KYCssion to delete client records.  
Right_Clients_KYC | Integer | Permission to launch automated validation of client data via [integrated KYC services](../../../Platform-Setup/Integrations/KYC.md). The permission affects the launching of verification from Manager and Administrator terminals, as well as from API.  
Right_Documents_Access | Integer | Permission to view client documents.  
Right_Documents_Create | Integer | Permission to add general information about documents in client records.  
Right_Documents_Edit | Integer | Permission to edit general information about documents in client records.  
Right_Documents_Delete | Integer | Permission to delete general information about documents from client records.  
Right_Documents_Files_Add | Integer | Permission to add document files in client records.  
Right_Documents_Files_Delete | Integer | Permission to delete document files from client records.  
Right_Comments_Access | Integer | Permission to read comments to clients and their documents.  
Right_Comments_Create | Integer | Permission to write comments to clients and their documents.  
Right_Comments_Delete | Integer | Permission to delete comments to clients and their documents.  
Right_Admin_Computer | Integer | Access to the server machine administration menu in the Network section of the Administrator terminal  
Right_Subscriptions_View | Integer | Permission to view existing settings in the Subscriptions section in the Administrator terminal, as well as access to subscription statistics.  
Right_Subscriptions_Edit | Integer | Permission to create, edit and remove settings in the Subscriptions section of the Administrator terminal.  
Right_Payments_Access | Integer | Permission to view current and processed [payments](../../../Platform-Setup/Payments.md) and payment accounts.  
Right_Payments_Process | Integer | [Permission to confirm and reject payments](../../../Platform-Setup/Payments/Processing.md) processed manually via the Manager terminal.  
Right_Payments_Edit | Integer | Permission to edit current and processed payments and payment accounts.  
Right_Payments_Delete | Integer | Permission to delete current and processed payments and payment accounts.
