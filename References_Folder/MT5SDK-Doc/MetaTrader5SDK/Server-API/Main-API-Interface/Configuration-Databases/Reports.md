[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Reports

[Previous](Routing/RouteGet.md) | [Next](Reports/ReportCreate.md)

# Report Configuration

The MetaTrader 5 platform includes functions for generating various reports on the trading activity on servers. A number of reports is included in the standard package of the platform, but this list can be extended by developing custom reports using the MetaTrader 5 Report API.

Such reports are separate modules implemented as DLL files. A report module is placed in a trade server, in the special /reports folder. Further the report can be configured from the MetaTrader 5 Administrator.

> Please note that the report modules are configured separately for each trade server and generate reports specifically for that server.

Functions described in this section allow managing configurations of reports, as well subscribe and unsubscribe from events associated with their change.

Function | Purpose  
---|---  
[ReportCreate](Reports/ReportCreate.md) | Create an object of the configuration of reports.  
[ReportModuleCreate](Reports/ReportModuleCreate.md) | Create an object of configuration of a report module.  
[ReportParamCreate](Reports/ReportParamCreate.md) | Create an object of a report parameter.  
[ReportSubscribe](Reports/ReportSubscribe.md) | Subscribe to events and hooks associated with the configuration of reports.  
[ReportUnsubscribe](Reports/ReportUnsubscribe.md) | Unsubscribe from events and hooks associated with the configuration of reports.  
[ReportAdd](Reports/ReportAdd.md) | Add or update a report configuration.  
[ReportDelete](Reports/ReportDelete.md) | Delete a report configuration by the name or index  
[ReportShift](Reports/ReportShift.md) | Change the position of a report configuration in the list.  
[ReportTotal](Reports/ReportTotal.md) | The total number of report configurations available in the platform.  
[ReportNext](Reports/ReportNext.md) | Get a report configuration by the index.  
[ReportGet](Reports/ReportGet.md) | Get a report configuration by the name.  
[ReportModuleTotal](Reports/ReportModuleTotal.md) | The total number of configurations of report modules available in the platform.  
[ReportModuleNext](Reports/ReportModuleNext.md) | Get a report module by the index.  
[ReportModuleGet](Reports/ReportModuleGet.md) | Get a report module configuration by the name.
