[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [MetaTrader 5 Administrator](../../MetaTrader-5-Administrator.md) / [Getting Started](../Getting-Started.md) / Structure of Directories and Files

[Previous](Start-Terminal.md) | [Next](Add-or-Remove-Servers.md)

# Structure of Directories and Files

This section contains the description of directory and file storing structure in the administrator terminal. In the [guest (#guest)](Start-Terminal.md#guest) terminal start mode storages are divided into those containing changeable and unchangeable files.

## Unchangeable Files

These files are located in /Program Files/MetaTrader 5 Administrator/. They are:

  * MT5Admin.exe — executable file of the administrator terminal;
  * Uninstall.exe — program for [deinstalling](Uninstall-Terminal.md) the administrator terminal;
  * /help/*.chm — built-in help files of the terminal.



## Changeable Files

The main directory of the terminal contains several folders: config, logs, profiles, roles, templates. The special command "![Open Data Folder](images/open_data_folder_button_1.png) Open Data Folder" located in the ["File" (#terminal-data)](../User-Interface/Main-Menu/File.md#terminal-data) of the terminal menu allows quick accessing the location of this data storage.

> All text files are of Unicode format. The corresponding software should be used for their editing.

The config directory contains the files of terminal settings, including servers added for administration:

Files | Description  
---|---  
mt5admin.ini | Contains [settings](../Terminal-Settings.md) of the administrator terminal, all interface parameters of the terminal, last used values of window positions, etc.  
servers.dat | Contains parameters of [connection](Connect-to-Server.md) to the administered servers.  
  
The logs directory contains log files of terminal operation, as well as crash logs:

Folders and Files | Description  
---|---  
/Crash/crash.log.* | Directory /crash contains files of terminal crashes. These files are automatically sent to the developer for finding out reasons for the crash and eliminating them.  
yyyymmdd.log | [Log](../User-Interface/Toolbox/Journal.md) files containing all the information about events occurring in the administrator terminal. Terminal logs are saved in separate files for each working day. Here: yyyy denotes a year, mm — month, dd — day.   
  
The profiles directory contains databases of the terminal distributed by administered servers and some settings:

Folders | Description | Files | Description  
---|---|---|---  
certificates | Contains files of certificates. | *.pfx | Files of certificates that can be installed to the system storage or e-token for further [authorization](Connect-to-Server/Extended-Authorization.md) on the server.  
config | Contains files of settings related to this server. | performance.dat | File that contains the history of server performance displayed at the ["Monitor"](../../Platform-Setup/Network-cluster/Monitor.md) tab.  
symbols-*.dat | List of [symbols](../../Platform-Setup/Symbols.md) of the server and their settings.  
mail | Contains mail database of the terminal. | mail-*.dat | Files of [mail database](../../Platform-Setup/Mailbox.md) separately for each login. The login number is specified after a hyphen in the file name.  
news | Contains news database of the terminal. | news-*.dat | Files of [news database](../User-Interface/Toolbox/News.md) separately for each login. The login is specified after a hyphen in the file name.  
  
The roles folder contains sets of permissions for manager accounts:

Files | Description  
---|---  
*.rol | These files contain the sets of settings of permission for the [accounts of managers (#permissions)](../../Platform-Setup/Managers.md#permissions).  
  
The templates directory contains templates of news and messages for sending:

Folders | Description | Files | Description  
---|---|---|---  
mail | Contains mail templates. | *.htm | HTM-files of [mail templates (#templates)](../../Platform-Setup/Mailbox.md#templates) saved using the corresponding command in the window of message writing.  
news | Contains news templates. | *.htm | HTM-files of [news templates (#templates)](../User-Interface/Toolbox/News.md#templates) saved using the corresponding command in the window of news sending.
