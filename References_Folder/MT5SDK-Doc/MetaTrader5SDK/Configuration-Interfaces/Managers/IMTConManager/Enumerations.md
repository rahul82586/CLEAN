[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / Enumerations

[Previous](../IMTConManager.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConManager](../IMTConManager.md) class contains the following enumerations:

  * [IMTConManager::EnManagerRights (#enmanagerrights)](Enumerations.md#enmanagerrights)
  * [IMTConManager::EnManagerRightFlags (#enmanagerrightflags)](Enumerations.md#enmanagerrightflags)
  * [IMTConManager::EnManagerLimit (#enmanagerlimit)](Enumerations.md#enmanagerlimit)



<a id="enmanagerrights"></a>
## IMTConManager::EnManagerRights (#enmanagerrights)

Rights that can be specified for a manager are listed in IMTConManager::EnManagerRights.

ID number | Value | Description  
RIGHT_ADMIN | 0 | Connection using the administrator terminal.  
RIGHT_MANAGER | 1 | Connection using the manager terminal.  
RIGHT_CFG_SERVERS | 10 | Network configuration  
RIGHT_CFG_ACCESS | 11 | Configuration of the list of IP access.  
RIGHT_CFG_TIME | 12 | Configuration of the server working time.  
RIGHT_CFG_HOLIDAYS | 13 | Configuration of holidays.  
RIGHT_CFG_HST_SYNC | 14 | Configuration of synchronization.  
RIGHT_CFG_SYMBOLS | 15 | Configuration of symbols.  
RIGHT_CFG_GROUPS | 16 | Configuration of groups.  
RIGHT_CFG_MANAGERS | 17 | Configuration of manager rights.  
RIGHT_CFG_DATAFEEDS | 18 | Configuration of data feeds.  
RIGHT_CFG_REQUESTS | 19 | Configuration of the routing table.  
RIGHT_SRV_JOURNALS | 20 | Access to server journals.  
RIGHT_SRV_REPORTS | 21 | Receive automatic server reports.  
RIGHT_CHARTS | 22 | Editing history data on the server. The RIGHT_CFG_SYMBOLS permission is additionally required to access the data.  
RIGHT_EMAIL | 23 | Sending internal emails.  
RIGHT_ACCOUNTANT | 24 | The permission to work with funds on accounts.  
RIGHT_ACC_READ | 25 | Access to accounts.  
RIGHT_ACC_DETAILS_NAME | 26 | Access to name details in [accounts](../../../Database-Interfaces/Users/IMTUser.md).  
RIGHT_ACC_MANAGER | 27 | Editing accounts.  
RIGHT_ACC_ONLINE | 28 | Getting the current client connections.  
RIGHT_TRADES_READ | 29 | Viewing trading orders, deals and positions. This permission affects the possibility of including rights and RIGHT_TRADES_MANAGER RIGHT_TRADES_DEALER.  
RIGHT_TRADES_MANAGER | 30 | Permission to edit any fields of orders, deals and positions in the administrator terminal and position open price in the the manager terminal.  
RIGHT_QUOTES | 31 | A permission to add quotes to the stream.  
RIGHT_RISK_MANAGER | 32 | A permission to receive information about client's aggregate positions and company's coverage positions.  
RIGHT_REPORTS | 33 | A permission to request and receive various reports on client operations.  
RIGHT_NEWS | 34 | Sending news. A manager/administrator is able to send news only if their account belongs to a group created at the main trade server.  
RIGHT_CFG_GATEWAYS | 35 | Configuring gateways.  
RIGHT_CFG_PLUGINS | 36 | Configuring plugins.  
RIGHT_TRADES_DEALER | 37 | Trading and dealing activities in the manager terminal. See ["Trading Activities" (#dealer-supervisor)](../../../Manager-API/Manager-Interface/Trade-Activity.md#dealer-supervisor) for more information.  
RIGHT_CFG_REPORTS | 38 | Configuration of reports.  
RIGHT_EXPORT | 39 | Permission to export data (orders, accounts, etc.) to external files from administrator and manager terminals. The permission does not affect the ability to export server configurations from the administrator terminal.  
RIGHT_SYMBOL_DETAILS | 40 | Permission to change spread and execution mode.  
RIGHT_TECHSUPPORT | 41 | Access to the Technical Support tab in the administrator and managerial terminals. The permission is no longer used due to being obsolete.  
RIGHT_TRADES_SUPERVISOR | 42 | This right allows a manager to view the entire queue of requests forwarded to him or her from available client groups, and track the process of request processing by other dealers in the manager terminal. The manager works in the Supervisor mode without connecting as a dealer in the manager terminal. After connecting as a dealer, the manager will only see the requests that are forwarded to the dealer for processing in accordance with the routing rules. See [ "Trading Activities" (#dealer-supervisor)](../../../Manager-API/Manager-Interface/Trade-Activity.md#dealer-supervisor) for more details about this mode.  
RIGHT_QUOTES_RAW | 43 | When this permission is enabled, the context menu command "Show raw quotes" will appear in the Market Watch window of the manager terminal. This command allows viewing quotes without [spread markup](../../Groups/IMTConGroupSymbol/SpreadDiff.md) set for the manager group.  
RIGHT_MARKET | 44 | Permission to access the Market of applications in MetaTrader 5 Administrator. The permission is no longer used due to being obsolete.  
RIGHT_GRP_DETAILS_MARGIN | 45 | Permission to change margin settings of groups ([IMTConGroupSymbol::Margin*](../../Groups/IMTConGroupSymbol/MarginFlags.md)) via MetaTrader 5 Manager.  
RIGHT_NOTIFICATIONS | 46 | A right to send push notifications to clients' mobile devices using the manager terminal. Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 5 Mobile for [iPhone](https://download.mql5.com/cdn/mobile/mt5/ios?hl=ru&utm_campaign=download&utm_source=metatrader5.help "iPhone") and [Android](https://download.mql5.com/cdn/mobile/mt5/android?hl=ru&utm_campaign=download&utm_source=metatrader5.help "Android"). More details are provided in the manager terminal user guide.  
RIGHT_ACC_DELETE | 47 | Deleting client accounts via the administrator and manager terminals, as well as via the Manager API. The RIGHT_ACC_MANAGER permission is also required in order to be able to delete accounts.  
RIGHT_TRADES_DELETE | 48 | Deleting any orders, accounts and positions via the administrator and manager terminals, as well as via the Manager API. The RIGHT_TRADES_MANAGER permission is also required in order to be able to delete accounts.  
RIGHT_CONFIRM_ACTIONS | 49 | By default the manager terminal displays a confirmation dialog when performing balance operations on client accounts and closing multiple orders. A manager needs to enter a randomly generated sequence of characters in order to confirm the appropriate action. If this permission is disabled, the above actions will be performed immediately without any confirmation.  
RIGHT_CFG_ECN | 50 | ECN settings.  
RIGHT_GRP_DETAILS_COMMISSION | 51 | Permission to change commission settings of groups ([IMTConCommission](../../Groups/IMTConCommission.md)) via MetaTrader 5 Manager.  
RIGHT_SUBSCRIPTIONS_VIEW | 52 | Viewing existing settings in the Subscriptions section in the Administrator terminal, as well as statistics on using subscriptions.  
RIGHT_SUBSCRIPTIONS_EDIT | 53 | Creating, changing and removing settings in the Subscriptions section of the Administrator terminal.  
RIGHT_CFG_FUNDS | 54 | Configuring investment funds in the Administrator terminal  
RIGHT_CFG_MAILS | 55 | Configuring integration with email services in the Administrator terminal  
RIGHT_CFG_MESSENGERS | 56 | Configuring integration with SMS providers and messengers in the Administrator terminal  
RIGHT_CFG_KYC | 57 | Configuring integration with KYC services in the Administrator terminal  
RIGHT_CFG_AUTOMATIONS | 58 | Configuring automatic actions for specified scenarios in the Administrator terminal.  
RIGHT_CFG_ALLOCATIONS | 59 | Accessing the Allocations section of the Administrator terminal. The section allows configuring groups, in which traders are able to open demo and preliminary real accounts directly from client terminals.  
RIGHT_CFG_VPS | 60 | Configuring Sponsored VPS for traders.  
RIGHT_CFG_PAYMENTS | 61 | Configuring integration with payment systems (in development).  
RIGHT_ADMIN_COMPUTER | 62 | Access to the server machine administration menu in the "Network" section of the Administrator terminal  
RIGHT_CFG_WEB_SERVICES | 63 | Configuring integration with web services: [SSL certificates](../../../Server-API/Main-API-Interface/Configuration-Databases/Network/TLSCertificateUpdate.md) and addresses for callback requests.  
RIGHT_FINTEZA_ACCESS | 64 | Access the the "Finteza Analytics" section in MetaTrader 5 Administrator.  
RIGHT_FINTEZA_WEBSITES | 65 | Viewing Finteza data relating to websites in the "Analytics" section of the Manager terminal.  
RIGHT_FINTEZA_CAMPAIGNS | 66 | Viewing Finteza data relating to marketing campaigns in the "Analytics" section of the Manager terminal.  
RIGHT_FINTEZA_REPORTS | 67 | The permission is currently not used.  
RIGHT_ACC_TECHNICAL | 70 | When combined with the [IMTUsers::USER_RIGHT_TECHNICAL (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) permission, provides greater convenience in working with various testing and technical accounts. Disable the IMTUsers::USER_RIGHT_TECHNICAL permission for all technical accounts, and then disable access to technical accounts for the managers who do not configure the platform. Otherwise, such technical accounts can be confusing for managers working with clients.  
RIGHT_ACC_TECHNICAL_MODIFY | 71 | Allows enabling and disabling the [IMTUsers::USER_RIGHT_TECHNICAL (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) and [IMTUser::USER_RIGHT_EXCLUDE_REPORTS (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) options for a trading account. Without this permission, the manager can only see the states of the relevant options, without the ability to change them (read-only).  
RIGHT_PAYMENTS_PROCESS | 72 | [Permission to confirm and reject payments](https://support.metaquotes.net/en/docs/mt5/manager/payments_processing) processed manually via the Manager terminal.  
RIGHT_CFG_CORPORATES | 73 | Access to [corporate link](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/corporate_links) settings.  
RIGHT_CFG_LEVERAGES  | 74 | Configuration of [floating leverage](../../Floating-Margin/IMTConLeverage.md).  
RIGHT_CFG_STREAMING | 75 | Configuring integrations with streaming data processing services.  
RIGHT_ACC_DETAILS_LOCATION | 76 | Access to location data in accounts: country, city, region, zip code.  
RIGHT_ACC_DETAILS_ADDRESS | 77 | Access to address details in [accounts](../../../Database-Interfaces/Users/IMTUser.md).  
RIGHT_ACC_DETAILS_ID | 78 | Access to data on document numbers in accounts.  
RIGHT_ACC_DETAILS_EMAIL | 79 | Access to email details in accounts.  
RIGHT_ACC_DETAILS_PHONE | 80 | Access to phone details in accounts.  
RIGHT_ACC_DETAILS_GENERAL | 81 | Access to other data in accounts (language, status, comment, MetaQuotes ID, etc.).  
RIGHT_CLIENTS_DETAILS_NAME | 82 | Access to name details in [clients](../../../Database-Interfaces/Clients/IMTClient.md).  
RIGHT_CLIENTS_DETAILS_LOCATION | 83 | Access to location data in clients: country, city, region, zip code.  
RIGHT_CLIENTS_DETAILS_ADDRESS | 84 | Access to address details in clients.  
RIGHT_CLIENTS_DETAILS_ID | 85 | Access to data on document numbers in clients.  
RIGHT_CLIENTS_DETAILS_EMAIL | 86 | Access to email details in clients.  
RIGHT_CLIENTS_DETAILS_PHONE | 87 | Access to phone details in clients.  
RIGHT_CLIENTS_DETAILS_GENERAL | 88 | Access to other data in clients (language, status, Lead Source, Lead Campaign, etc.).  
RIGHT_CLIENTS_ACCESS | 96 | Access to the "Clients" section in the Administrator and Manager terminals.  
RIGHT_CLIENTS_CREATE | 97 | Permission to create new client entries manually.  
RIGHT_CLIENTS_EDIT | 98 | Permission to edit client data, except for documents.  
RIGHT_CLIENTS_DELETE | 99 | Permission to delete client entries.  
RIGHT_DOCUMENTS_ACCESS | 100 | Permission to view client documents.  
RIGHT_DOCUMENTS_CREATE | 101 | Permission to add general information about documents in client entries.  
RIGHT_DOCUMENTS_EDIT | 102 | Permission to edit general information about documents in client entries.  
RIGHT_DOCUMENTS_DELETE | 103 | Permission to delete general information about documents from client entries.  
RIGHT_DOCUMENTS_FILES_ADD | 104 | Permission to add document files in client entries.  
RIGHT_DOCUMENTS_FILES_DELETE | 105 | Permission to delete document files from client entries.  
RIGHT_COMMENTS_ACCESS | 106 | Permission to read comments to clients and their documents.  
RIGHT_COMMENTS_CREATE | 107 | Permission to write comments to clients and their documents.  
RIGHT_COMMENTS_DELETE | 108 | Permission to delete comments to clients and their documents.  
RIGHT_CLIENTS_KYC | 109 | Permission to launch automated validation of client data via [integrated KYC services](../../KYC/IMTCon.md). The permission affects the launching of verification from Manager and Administrator terminals, as well as the [IMTAdminAPI::KYCStart](../../../Manager-API/Administrator-Interface/Configuration-Databases/KYC/Start.md) and [IMTServerAPI::KYCStart](../../../Server-API/Main-API-Interface/Configuration-Databases/KYC/Start.md) methods.  
RIGHT_PAYMENTS_ACCESS | 110 | Permission to view current and processed [payments](https://support.metaquotes.net/en/docs/mt5/platform/administration/payments) and payment accounts.  
RIGHT_PAYMENTS_EDIT | 111 | Permission to edit current and processed payments and payment accounts.  
RIGHT_PAYMENTS_DELETE | 112 | Permission to delete current and processed payments and payment accounts.  
RIGHT_FIRST |  | Beginning of enumeration. Corresponds to RIGHT_ADMIN.  
RIGHT_LAST | 128 | End of enumeration.  
  
This enumeration is used in the [IMTConManager::Right](Right.md) method.

<a id="enmanagerrightflags"></a>
## IMTConManager::EnManagerRightFlags (#enmanagerrightflags)

The states of manager rights are listed in IMTConManager::EnManagerRightFlags.

ID number | Value | Description  
RIGHT_FLAGS_DENIED | 0 | The right is not granted.  
RIGHT_FLAGS_GRANTED | 1 | The right is granted.  
RIGHT_FLAGS_NONE | 0 | Beginning of enumeration. Corresponds to the absence of rights.  
RIGHT_FLAGS_ALL |  | End of enumeration. Corresponds to RIGHT_FLAGS_GRANTED.  
  
This enumeration is used in the [IMTConManager::Right](Right.md) method.

<a id="enmanagerlimit"></a>
## IMTConManager::EnManagerLimit (#enmanagerlimit)

IMTConManager::EnManagerLimit contains the periods, for which a manager can view reports and system logs.

ID number | Value | Description  
MANAGER_LIMIT_ALL | 0 | Unlimited.  
MANAGER_LIMIT_MONTHS_1 | 1 | One month.  
MANAGER_LIMIT_MONTHS_3 | 2 | Three months.  
MANAGER_LIMIT_MONTHS_6 | 3 | Six months.  
MANAGER_LIMIT_YEAR_1 | 4  | One year.  
MANAGER_LIMIT_YEAR_2 | 5 | Two years.  
MANAGER_LIMIT_YEAR_3 | 6 | Three years.  
MANAGER_LIMIT_FIRST |  | Beginning of enumeration. Corresponds to MANAGER_LIMIT_ALL.  
MANAGER_LIMIT_LAST |  | End of enumeration. Corresponds to MANAGER_LIMIT_YEAR_3.  
  
This enumeration is used in the following methods:

  * [IMTConManager::LimitLogs](LimitLogs.md)
  * [IMTConManager::LimitReports](LimitReports.md)


