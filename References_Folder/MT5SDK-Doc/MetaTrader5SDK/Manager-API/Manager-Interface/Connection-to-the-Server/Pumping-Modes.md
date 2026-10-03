[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Connection to the Server](../Connection-to-the-Server.md) / Pumping Modes

[Previous](../Connection-to-the-Server.md) | [Next](Connect.md)

# Pumping Mode

Enabled pumping mode means that the application will synchronize the appropriate server database with a locally created database. Thus, to obtain information the application can access a local database using the Get and Next methods (for example, [IMTManagerAPI::SymbolGet](../Configuration-Databases/Symbols/SymbolGet.md), [IMTManagerAPI::GroupNext](../Configuration-Databases/Groups/GroupNext.md), etc.). Since databases can be quite large, pumping should only be enabled for information that requires frequent and rapid access. Local databases are loaded into RAM, therefore enabling pumping directly affects RAM usage. When pumping is disabled, required information can be requested directly from the server using Request methods (for example, [IMTManagerAPI::SymbolRequest](../Configuration-Databases/Symbols/SymbolRequest.md), [IMTManagerAPI::GroupRequest](../Configuration-Databases/Groups/GroupRequest.md)).

Possible pumping modes are enumerated in IMTManagerAPI::EnPumpModes. The pumping mode in which we want to connect is specified in the pump_mode parameter of the [IMTManagerAPI::Connect](Connect.md) method.

ID | Value | Description  
PUMP_MODE_USERS | 0x00000001 | Pumping of users.  
PUMP_MODE_ACTIVITY | 0x00000002 | Pumping of the online activity of users.  
PUMP_MODE_MAIL | 0x00000004 | Mail pumping.  
PUMP_MODE_ORDERS | 0x00000008 | Pumping of orders.  
PUMP_MODE_NEWS | 0x00000020 | News pumping.  
PUMP_MODE_POSITIONS | 0x00000080 | Pumping of positions.  
PUMP_MODE_GROUPS | 0x00000100 | Pumping of configurations of user groups.  
PUMP_MODE_SYMBOLS | 0x00000200 | Pumping of symbol configurations.  
PUMP_MODE_HOLIDAYS | 0x00000800 | Pumping of holiday configurations.  
PUMP_MODE_TIME | 0x00001000 | Pumping of time configurations.  
PUMP_MODE_GATEWAYS | 0x00002000 | Pumping of gateway configurations. It is used for displaying available gateways in the box of [accounts in external systems](../../../Database-Interfaces/Users/IMTUser/ExternalAccountAdd.md) on the "Account" tab of a client in the administrator or manager terminal.  
PUMP_MODE_REQUESTS | 0x00004000 | Pumping of the request queue and results of processing requests by other dealers. It is required for connecting a manager in the ["Supervisor" (#dealer-supervisor)](../Trade-Activity.md#dealer-supervisor) mode.  
PUMP_MODE_PLUGINS | 0x00008000 | Pumping of the plugin configurations on the server. It is required for the possibility of setting up plugins through the Manager API application. Additionally the plugin must have the [IMTConPlugin::PLUGIN_FLAG_MAN_CONFIG (#enpluginflags)](../../../Configuration-Interfaces/Plugins/IMTConPlugin/Enumerations.md#enpluginflags) flag enabled, and the manager account must have the [IMTConManager::RIGHT_CFG_PLUGINS (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission granted.  
PUMP_MODE_CLIENTS | 0x00010000 | Pumping of clients.  
PUMP_MODE_SUBSCRIPTIONS | 0x00020000 | Pumping of [subscription configurations](../Configuration-Databases/Subscriptions.md).  
PUMP_MODE_SUBSCRIPTIONS | 0x00020000 | Pumping of all the information listed above.  
  
  * When enabling the pumping of orders and positions, the pumping of accounts, groups and symbols is enabled automatically.


  * The pumping mode does not affect the operation of those methods, which request data directly from the server (such as [IMTManagerAPI::UserRequest](../Users/UserRequest.md), [IMTManagerAPI::OrderRequest](../Trade-Databases/Orders/OrderRequest.md) etc.). Such methods can be used in any pumping mode.


  * To use pumping, the manager account, which is used for connecting applications, needs the relevant permissions. For example, the [IMTConManager::RIGHT_TRADES_READ (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission is required to pump orders and positions.

  
---
