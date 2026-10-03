[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [History Server](../History-Server.md) / Console Commands

[Previous](Quotes-Filtration.md) | [Next](../Backup-Server.md)

# Console Commands

The history server component [mt5srvupdater64.exe](Structure-of-Directories-and-Files.md) has several console commands that allow updating and activating the platform if servers are unavailable for connection via the administrator terminal.

In order to execute these commands, start file mt5srvupdater64.exe from the root directory of the history server, specifying corresponding keys:

  * /update — download updated files of all the system components, if there are such files, from the developer's update server;
  * /upgrade — install [updates](../../Platform-Setup/Live-Update.md) of all the platform components. This command can be executed only of the updates have been downloaded;
  * /activate — [activate](../../Platform-Installation/Activation.md) the platform.



For example, after you execute command "mt5srvupdater64.exe /update /upgrade", the platform updates will be downloaded and installed.

> The protocol of the update process is kept in , located in folder .
