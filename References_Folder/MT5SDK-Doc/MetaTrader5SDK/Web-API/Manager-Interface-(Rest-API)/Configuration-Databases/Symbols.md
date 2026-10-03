[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../Configuration-Databases.md) / Symbols

[Previous](Groups/Get-by-Name.md) | [Next](Symbols/Data-Structure.md)

# Symbols

The Web API provides the following requests for receiving settings of symbols on the server:

Request | Description  
---|---  
[/api/symbol/add](Symbols/Add.md) | Create or change a symbol on the server.  
[/api/symbol/add_batch](Symbols/Add-Multiple.md) | Create or change multiple symbols on the server.  
[/api/symbol/delete](Symbols/Delete.md) | Delete a symbol from the server.  
[/api/symbol/delete_batch](Symbols/Delete-Multiple.md) | Delete multiple symbols from the server.  
[/api/symbol/shift](Symbols/Shift.md) | Change the position of a symbol configuration in the list.  
[/api/symbol/total](Symbols/Get-Total.md) | Get the number of symbols on a trade server.  
[/api/symbol/list](Symbols/Get-List.md) | Get the list of symbols available on the trade server.  
[/api/symbol/next](Symbols/Get-by-Index.md) | Get the configuration of one or more symbols by index in the list.  
[/api/symbol/get](Symbols/Get-by-Name-or-Mask.md) | Get the symbol configurations by the name or mask.  
[/api/symbol/get_group](Symbols/Get-by-Group.md) | Get an individual configuration of a symbol for a group by the name of the symbol.  
[/api/symbol_group/add](Symbols/Add-Subgroup.md) | Add a subgroup of symbols.  
[/api/symbol_group/delete](Symbols/Delete-Subgroup.md) | Delete a subgroup of symbols by name or index.  
[/api/symbol_group/shift](Symbols/Shift-Subgroup.md) | Change the position of a subgroup of symbols in a list.  
[/api/symbol_group/total](Symbols/Get-Subgroup-Total.md) | Get the total number of symbol subgroups existing in the platform.  
[/api/symbol_group/next](Symbols/Get-Subgroup-by-Index.md) | Get the name of a subgroup of symbols by index.  
[/api/symbol_group/list](Symbols/Get-Subgroup-List.md) | Get a list of symbol subgroups available on the trading server.  
  
The format, in which the data about symbol configuration are passed, are described in the ["Data Structure"](Symbols/Data-Structure.md) section.
