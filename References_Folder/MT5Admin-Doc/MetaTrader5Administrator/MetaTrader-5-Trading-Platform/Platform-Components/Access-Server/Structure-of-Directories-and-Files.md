[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Access Server](../Access-Server.md) / Structure of Directories and Files

[Previous](../Access-Server.md) | [Next](Antiflood-Control.md)

# Structure of Directories and Files

The access server is installed to folder "access_server". This folder contains the following executable files:

  * mt5srvupdater64.exe — the executable file of the live update system of the access server;
  * mt5access64.exe — the executable file of the access server.



The main directory of the access server contains five folders: bases, config, history, liveupdate, logs.

The bases directory contains the news databases, as well as data on the server performance.

Files | Description  
---|---  
performance\ | Monthly access server performance databases and data indexes, which are displayed on the [Monitoring](../../Platform-Setup/Network-cluster/Monitor.md) tab.  
news.dat | Database of news sent to clients.  
news.idx | The index file of the news database.  
performance.dat | Data about the access server performance that are displayed on the ["Monitor"](../../Platform-Setup/Network-cluster/Monitor.md) tab are written to this file.  
  
The config directory contains configuration files:

Files | Description  
---|---  
server.ini | Individual settings of the access server.  
servers.ini | Settings of the internal [network of servers](../../Platform-Setup/Network-cluster.md).  
symbols.ini | Configurations of [symbols](../../Platform-Setup/Symbols/Symbol-Settings.md).  
time.ini | [Time](../../Platform-Setup/Time.md) settings.  
  
The history directory contains the base of history data by symbols, which was received from the history server:

Files and folders | Files | Description  
[2 chars]\\[symbol]\ | yyyy.hsc | Minute data for the symbol, divided by years. '2 chars' are the first two characters in the instrument name; 'symbol' is the name of the instrument. Arranging symbol data in different directories reduces the load on the file system and provides faster data operations.  
[2 chars]\\[symbol]\ | yyyy.tkc | Tick data for the symbol, divided by years. '2 chars' are the first two characters in the instrument name; 'symbol' is the name of the instrument. Arranging symbol data in different directories reduces the load on the file system and provides faster data operations.  
tickers.dat |  | Data by tickers.  
  
The liveupdate directory contains the latest updates of the client, manager and administrator terminals:

Files | Description  
---|---  
mt5adm.build | Live update of the administrator terminal. The build number is specified after the point.  
mt5clw.build | Live update of the client terminal.  
mt5ckwide.build | Live Update of MetaEditor.  
mt5clwmql.build | Live Update of the MQL5 compiler.  
mt5man.build | Live update of the manager terminal.  
  
The logs directory keeps files of the access server operation journal, as well crash logs:

Files and folders | Description  
---|---  
Crash\crash.log.* | The /crash directory contains server crash files. These files are automatically sent to the software developing company for detecting reasons of the crash and eliminating them.  
yyyymmdd.log | [Journal](../../Platform-Setup/Network-cluster/Journal.md) files that contain all the information about events that occur on the access server. Server logs are stored in separate files for each working day. Here yyyy — year, mm — month, dd — day.   
mt5srvupdater.log | Journal files of the platform [updates](../../Platform-Setup/Live-Update.md).
