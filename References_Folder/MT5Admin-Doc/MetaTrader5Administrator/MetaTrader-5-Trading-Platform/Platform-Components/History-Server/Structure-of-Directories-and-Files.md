[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [History Server](../History-Server.md) / Structure of Directories and Files

[Previous](../History-Server.md) | [Next](Interaction-with-Quote-Providers.md)

# Structure of Directories and Files

The history server is installed to folder "history_server". It contains the following executable files:

  * mt5srvupdater64.exe — the executable file of the live update system of the history server. This component has a number of [console commands](Console-Commands.md);
  * mt5history64.exe — the executable file of the history server.



The main directory of the history server contains the following folders: bases, config, datafeed, gateway, history, liveupdate, logs, plugins.

The bases directory contains different data bases:

Files and folders | Description | Files and folders | Description  
---|---|---|---  
ecn\ | [ECN](../../Platform-Setup/ECN.md) data directory. | executions\ | Bases and indexes of ECN trade executions by trade servers.  
history\ | Bases and indexes related to the history of client order execution in ECN, by months.  
symbols\\{Symbol}\matching.dat | Symbol databases related to client orders placed in ECN for matching.  
symbols\\{Symbol}\filling_items.dat | Symbol databases of matching operations processed in ECN.  
symbols\\{Symbol}\books\yyyymmdd.book | ECN Market Depth journals by days.  
filling_orders.dat | Databases of internal ECN order which are executed on gateways.  
performance\ | Monthly history server performance databases and data indexes, which are displayed on the [Monitoring](../../Platform-Setup/Network-cluster/Monitor.md) tab.  
news.dat | News data base.  
news.idx | The index file of the news database.  
  
The config directory contains different configurations as *.ini files:

Files | Description  
---|---  
common.ini | Common History Server settings.  
ecn_symbols.ini | [ECN](../../Platform-Setup/ECN.md) symbol settings.  
mt5srvupdater.ini | [Update](../../Platform-Setup/Live-Update.md) settings.  
history_sync.ini | Settings of [history data synchronization](../../Platform-Setup/Synchronization.md).  
server.ini | Individual settings of the access server.  
servers.ini | Settings of the internal [network of servers](../../Platform-Setup/Network-cluster.md).  
symbol_groups.ini | Individual settings of [symbols for groups](../../Platform-Setup/Groups/Group-Symbol-Settings.md).  
symbols.ini | [Symbol](../../Platform-Setup/Symbols.md) settings.  
time.ini | [Time](../../Platform-Setup/Time.md) settings.  
  
The datafeed directory contains files for working with [data feeds](../../Platform-Setup/Data-Feeds.md):

Files | Description  
---|---  
[datafeed_name]\logs\yyyymmdd.log | Journal files in which records regarding data feed operation are stored. For each data feed which has been added through the [relevant section](../../Platform-Setup/Data-Feeds.md) of the Administrator terminal, a separate journal file is created. The file name is set in accordance with the data feed name.  
[datafeed_name]\*.dat | Data files with data feed settings.  
*.exe | Data feed executables. It is not allowed to have several datafeed executable files with the same name in the history server directory. If you place several identical files in different subdirectories, this may lead to conflicts in the operation and display of modules in the Administrator terminal.  
MT5APIGateway.dll, MT5APIGateway64.dll | Libraries for data feed operation.  
  
The gateway directory contains files for working with [gateways](../../Platform-Setup/Gateways.md):

Files and folders | Description  
---|---  
[gateway_name]\\[gateway configuration name]\logs\yyyymmdd.log | Journal files in which gateway operation logs are stored. For each data feed which has been added through the [relevant section](../../Platform-Setup/Gateways.md) of the Administrator terminal, a separate journal file is created. The file name is set in accordance with the data feed name.  
[gateway_name]\\[gateway configuration name]\*.dat | Data files with gateway settings.  
*.exe | Gateway executables. It is not allowed to have several datafeed executable files with the same name in the history server directory. If you place several identical files in different subdirectories, this may lead to conflicts in the operation and display of modules in the Administrator terminal.  
MT5APIGateway.dll, MT5APIGateway64.dll | Libraries for gateway operation.  
  
The history folder contains [history data](../../Platform-Setup/1-Minute-History-Charts.md) divided by symbols:

Folders | Files | Description  
[2 chars]\\[symbol]\ | yyyy.hsc | History data on a symbol, divided by years. '2 chars' are the first two characters in the instrument name; 'symbol' is the name of the instrument. Arranging symbol data in different directories reduces the load on the file system and provides faster data operations.  
[2 chars]\\[symbol]\ | yyyy.tkc | Tick data on a symbol, divided by years. '2 chars' are the first two characters in the instrument name; 'symbol' is the name of the instrument. Arranging symbol data in different directories reduces the load on the file system and provides faster data operations.  
  
The liveupdate folder contains the latest updates of all the platform components:

Files | Description  
---|---  
mt5adm.build | Live update of the administrator terminal. The build number is specified after the point.  
mt5as.build | Live update of the access server.  
mt5bs.build | Live update of the backup server.  
mt5clw.build | Live update of the client server.  
mt5clwide.build | Live Update of MetaEditor.  
mt5clwmql.build | Live Update of the MQL5 compiler.  
mt5hs.build | Live update of the history server.  
mt5hsu.build | Live update of the update system of the history server.  
mt5man.build | Live update of the manager server.  
mt5ts.build | Live update of the trade server.  
  
The logs folder contains log files of the history server operation, as well as crash logs:

Files and folders | Description  
---|---  
Crash\crash.log.* | The /crash directory contains server crash files. These files are automatically sent to the software developing company for detecting reasons of the crash and eliminating them.  
yyyymmdd.log | [Journal](../../Platform-Setup/Network-cluster/Journal.md) files that contain all the information about events that occur on the history server. Server logs are stored in separate files for each working day. Here yyyy — year, mm — month, dd — day.   
mt5srvupdater.log | Journal files of the platform [updates](../../Platform-Setup/Live-Update.md).
