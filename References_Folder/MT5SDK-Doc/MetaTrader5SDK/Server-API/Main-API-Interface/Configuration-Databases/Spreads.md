[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Spreads

[Previous](Symbols/SymbolGroupExist.md) | [Next](Spreads/SpreadCreate.md)

# Configuration of Spreads

MetaTrader 5 Server API allows users to configure the charging of the margin in case client's trading positions are in a spread to one another. The spread is defined as the presence of the oppositely directed positions at related symbols. Reduced margin requirements provide more trading opportunities for traders.

Functions described in this section allow managing spreads, as well subscribe and unsubscribe from events associated with their change.

Function | Purpose  
---|---  
[SpreadCreate](Spreads/SpreadCreate.md) | Create an object of the configuration of a spread.  
[SpreadLegCreate](Spreads/SpreadLegCreate.md) | Create an object of the configuration of a spread leg.  
[SpreadSubscribe](Spreads/SpreadSubscribe.md) | Subscribe to events and hooks associated with the configuration of spreads.  
[SpreadUnsubscribe](Spreads/SpreadUnsubscribe.md) | Unsubscribe from events and hooks associated with spread configuration.  
[SpreadAdd](Spreads/SpreadAdd.md) | Add or update a spread configuration.  
[SpreadDelete](Spreads/SpreadDelete.md) | Deleting a spread configuration by the index.  
[SpreadShift](Spreads/SpreadShift.md) | Change the position of a spread configuration in the list.  
[SpreadTotal](Spreads/SpreadTotal.md) | The total number of spread configurations available in the platform.  
[SpreadNext](Spreads/SpreadNext.md) | Receiving a spread configuration by the index.  
[SpreadGet](Spreads/SpreadGet.md) | Receiving a spread configuration by the identifier.
