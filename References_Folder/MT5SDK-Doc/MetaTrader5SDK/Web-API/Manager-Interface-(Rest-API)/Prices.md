[🏠 Document Start](../../README.md) / [Web API](../README.md) / [Manager Interface (Rest API)](../Manager-Interface-(Rest-API).md) / Prices

[Previous](News/Get-With-Body.md) | [Next](Prices/Data-Structure.md)

# Prices

Using the MetaTrader 5 Web API, you can receive price data from a trade server. The following requests are available in the Web API:

Request | Description  
---|---  
[/api/tick/last](Prices/Get-Quotes.md) | Get the current prices of a symbol.  
[/api/tick/last_group](Prices/Get-Quotes-by-Group.md) | Get the current prices of a symbol taking into account conversion for this group.  
[/api/tick/stat](Prices/Get-Statistics.md) | Get the current statistics of a symbol.  
[/api/tick/history](Prices/Get-Tick-History.md) | Get the history of ticks.  
[/api/chart/get](Prices/Get-M1-History.md) | Get the history of bars (1-minute data).  
[/api/book/get](Prices/Get-Market-Depth.md) | Get the Market Depth of a symbol.  
  
The format, in which the data about prices are passed, are described in the ["Data Structure"](Prices/Data-Structure.md) section.
