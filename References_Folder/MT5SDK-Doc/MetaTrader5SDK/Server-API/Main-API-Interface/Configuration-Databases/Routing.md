[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Routing

[Previous](Gateways/GatewayRestart.md) | [Next](Routing/RouteCreate.md)

# Routing Configuration

The MetaTrader 5 platform allows creating a custom set of rules of routing clients' requests received by trade servers. In each routing rule, you can set up the parameters of trade requests, as well as actions that shall apply to them.

Functions described in this section allow managing routing configurations, as well subscribe and unsubscribe from events associated with their change.

Function | Purpose  
---|---  
[RouteCreate](Routing/RouteCreate.md) | Create an object of a routing rule.  
[RouteConditionCreate](Routing/RouteConditionCreate.md) | Create an object of an additional condition to apply a rule.  
[RouteDealerCreate](Routing/RouteDealerCreate.md) | Create an object of a dealer configuration to whom requests under this rule will be sent.  
[RouteSubscribe](Routing/RouteSubscribe.md) | Subscribe to events and hooks associated with the configuration of request routing.  
[RouteUnsubscribe](Routing/RouteUnsubscribe.md) | Unsubscribe from events and hooks associated with the configuration of request routing.  
[RouteAdd](Routing/RouteAdd.md) | Add or update a routing rule.  
[RouteDelete](Routing/RouteDelete.md) | Delete a routing rule by its name or index  
[RouteShift](Routing/RouteShift.md) | Move a routing rule in the list.  
[RouteTotal](Routing/RouteTotal.md) | The total number of routing rules available in the platform.  
[RouteNext](Routing/RouteNext.md) | Get a routing rule by the index.  
[RouteGet](Routing/RouteGet.md) | Get a routing rule by the name.
