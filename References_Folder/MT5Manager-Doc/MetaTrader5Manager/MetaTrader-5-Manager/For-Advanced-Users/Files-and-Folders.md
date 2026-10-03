[🏠 Document Start](../../README.md) / [MetaTrader 5 Manager](../../MetaTrader-5-Manager.md) / [For Advanced Users](../For-Advanced-Users.md) / Files and Folders

[Previous](Installing-the-Terminal.md) | [Next](Extended-Authentication.md)

# Files and Folders

This section describes the storage structure of directories and files of the Manager terminal. In the [guest mode (#guest)](../Terminal-Start.md#guest) of the terminal launch, changeable and unchangeable files of the terminal are stored separately.

## Unchangeable files

These files are located in the directory /Program Files/Terminal/, they include:

  * mt5manager.exe — executable file of the Manager terminal.
  * Uninstall.exe — program for the terminal [deinstallation](Terminal-Deinstallation.md).
  * /help/*.chm — built-in help files of the terminal.



## Changeable files

The main directory of the terminal contains three folders: bases, config, logs. A special command is used in the terminal for quick access to data storage location — "![Open Data Folder](images/open_data_folder_button.png) Open Data Folder" located in the [File (#file)](../../User-Interface/Main-Menu.md#file) menu.

> All text files are of Unicode format. Use appropriate software to edit them.

The bases directory contains terminal databases arranged by trade servers, and some settings:

Folders and files | Description | Sub-folders | Description  
---|---|---|---  
Default | Default folder of the terminal database | Certificates | *.pfx certificate files.  
History | History data of financial instruments. Each symbol is stored in a separate directory that also contains ticks.dat file with tick data.  
Mail | All [emails (#mail)](../../User-Interface/Toolbox.md#mail) received or sent from the terminal. Mail databases are stored in *.dat files. For each account opened in the terminal, a separate file is created for storing emails. For example, mail-xxxxx.dat, where xxxxx is an account number.  
News | One news.dat file containing the database of all [news (#news)](../../User-Interface/Toolbox.md#news) ever received in the terminal from a selected trade server.  
MetaTrader 5 Server 1 — N | Terminal database folders for different trade servers | Orders | The current base of [orders](../../Trading-Operations/Working-with-Trading-Orders.md) available to a manager account. Bases of orders are stored in separate orders-xxxxxx.dat files for each account. Here xxxxxx is a number of the manager account.  
Positions | The current base of [positions](../../Trading-Operations/Working-with-Trading-Positions.md) available to the manager account. Bases of positions are stored in separate positions-xxxxxx.dat files for each account. Here xxxxxx is a number of the manager account.  
Symbols | selected-xxxxx.dat file contains the symbol base currently selected in the [Market Watch](../../Trading-Operations/Market-Watch.md) window. symbols-xxxxx.dat file contains the common database of symbols available on this trade server.  
Users | The current base of [accounts](../../Clients-and-Trading-Accounts/README.md) available to a manager account. Bases of accounts are stored in separate users-xxxxxx.dat files for each account. Here xxxxxx is a number of the manager account.  
profiles | Files of the Market Watch window symbol [profiles (#profile)](../../Dealing-and-Risk-Management/Quoting-and-Symbol-Management.md#profile) (*.prf).  
alerts.dat | The database of created [alerts](../../Trading-Operations/Trading-Notifications.md).  
books.dat | A list of currently open windows of request queues.  
dnslookups.dat | IP addresses of the currently [connected accounts](../../Clients-and-Trading-Accounts/Online-Accounts.md) and name of hosts they are attached to.   
  
config directory contains terminal configuration files:

Files | Description  
---|---  
accounts.dat | The database of manager accounts, using which [connections](../Connecting-to-the-Server.md) to server were established.  
common.ini | [Settings](../Terminal-Settings.md) of the Manager terminal.  
mt5admin.ini | All configurations of the terminal interface, the last used values for window positions, etc.  
servers.dat | Parameters of the servers you [connect](../Connecting-to-the-Server.md) to.  
  
The logs directory contains files of the terminal journal and crash logs:

Folders and files | Description  
---|---  
/Crash/crash.log.* | The /crash directory contains files of the terminal crashes. These files are automatically sent to the developer company to determine and eliminate their causes.  
yyyymmdd.log | Files of the [journal (#journal)](../../User-Interface/Toolbox.md#journal) that contain all the information about events occurring in the manager terminal. Terminal logs are stored in separate files for each day it runs. Here yyyy is a year, mm is a month, dd is a day.   
dealing.log | The [journal (#journal)](../../Dealing-and-Risk-Management/Dealing.md#journal) file of trade request processing by a dealer.  
  
The templates directory contains mail and news templates:

Folders | Description | Files | Description  
---|---|---|---  
mail | Email templates. | *.htm | HTM files of [mail templates (#mail-template)](../../Clients-and-Trading-Accounts/Push-Notifications-SMS-and-Mail.md#mail-template), which were saved by the appropriate command in the email writing window.  
news | News templates. | *.htm | HTM files of [news templates (#news-template)](../../User-Interface/Toolbox.md#news-template), which were saved by the appropriate command of the news sending window.
