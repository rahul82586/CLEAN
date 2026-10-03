[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Gateways

[Previous](History-Synchronization/HistorySyncNext.md) | [Next](Gateways/GatewayCreate.md)

# Gateway Configuration

Gateways are used for integrating the MetaTrader 5 platform with external trading systems. Gateways allow to transmit trade operations to external systems, as well as transmit quotes and news from them.

Functions described in this section allow managing the gateway configurations, as well subscribe and unsubscribe from events associated with their change.

Function | Purpose  
---|---  
[GatewayCreate](Gateways/GatewayCreate.md) | Create an object of the gateway configuration.  
[GatewayModuleCreate](Gateways/GatewayModuleCreate.md) | Create an object of configuration of the gateway module.  
[GatewayParamCreate](Gateways/GatewayParamCreate.md) | Create an object of the gateway parameter.  
[GatewayTranslateCreate](Gateways/GatewayTranslateCreate.md) | Create an object of the parameter for converting the information received by the gateway.  
[GatewaySubscribe](Gateways/GatewaySubscribe.md) | Subscribe to events and hooks associated with the gateway configuration.  
[GatewayUnsubscribe](Gateways/GatewayUnsubscribe.md) | Unsubscribe from events and hooks associated with the gateway configuration.  
[GatewayAdd](Gateways/GatewayAdd.md) | Add or update a gateway configuration.  
[GatewayDelete](Gateways/GatewayDelete.md) | Delete a gateway configuration by the name or index  
[GatewayShift](Gateways/GatewayShift.md) | Change the position of a gateway configuration in the list.  
[GatewayTotal](Gateways/GatewayTotal.md) | The total number of gateway configurations available in the platform.  
[GatewayNext](Gateways/GatewayNext.md) | Get the gateway configuration by the index.  
[GatewayGet](Gateways/GatewayGet.md) | Get the gateway configuration by the name.  
[GatewayModuleTotal](Gateways/GatewayModuleTotal.md) | The total number of gateway modules available in the platform.  
[GatewayModuleNext](Gateways/GatewayModuleNext.md) | Get the gateway module by the index.  
[GatewayModuleGet](Gateways/GatewayModuleGet.md) | Get the gateway module by the name.  
[GatewayRestart](Gateways/GatewayRestart.md) | Restart gateways.
