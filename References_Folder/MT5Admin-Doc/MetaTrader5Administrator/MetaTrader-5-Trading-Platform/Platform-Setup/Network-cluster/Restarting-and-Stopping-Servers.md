[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Network cluster](../Network-cluster.md) / Restarting and Stopping Servers

[Previous](Hosted-Access-Servers.md) | [Next](Managing-Machines.md)

# Restarting and Stopping Servers

A number of operations on the trading platform setup require servers being restarted afterwards. To restart a server, select the necessary one in the "Network" section and execute command "![Restart Server](images/restart_server_button.png) Restart server" in the [Service](../../MetaTrader-5-Administrator/User-Interface/Main-Menu/Services.md) menu, in the [Standard](../../MetaTrader-5-Administrator/User-Interface/Toolbar/Standard.md) toolbar or in the [context menu (#context)](../Network-cluster.md#context).

> When the main trade server is restarted, all other components are restarted automatically.

The platform (main trade server) needs to be restarted after the following operations:

  * Addition of a new [server](Configuring-Servers.md);
  * Changing of the [platform name (#name)](../Start-Page.md#name) visible to clients;
  * Changing of parameter "[Risk management (#risk)](../Groups/Group-Settings.md#risk)" in group settings;
  * Changing of [network parameters (#common)](Configuring-Servers.md#common) of the server (address, port, login or password);
  * Changing of [access points (#network)](Configuring-Servers.md#network), [bindings (#network)](Configuring-Servers.md#network) and of the list of serviced [trade servers (#servers)](Configuring-Servers/Access-Server.md#servers) for access servers;
  * Changing of parameters ["Digits" (#digits)](../Symbols/Symbol-Settings/Common.md#digits), ["Tick size" (#tick-size)](../Symbols/Symbol-Settings/Trade.md#tick-size), ["Tick value" (#tick-price)](../Symbols/Symbol-Settings/Trade.md#tick-price) and "[Market depth (#dom)](../Symbols/Symbol-Settings/Common.md#dom)" in symbol settings;
  * Changing of the server [time zone (#time-zone)](../Time.md#time-zone);
  * Changing of the mode of switching to [Daylight Saving Time (#daylight-saving)](../Time.md#daylight-saving);
  * Changing of the [ranges of accounts, orders and deals (#accounts)](Configuring-Servers/Trade-Server.md#accounts);


  * Changing if the "[Datafeeds timeout (#history)](Configuring-Servers/History-Server.md#history)" parameter in the history server settings;


  * Appearance of faults.



  * Servers should be restarted only on weekends and holidays, or at night when the trading activity is minimal. The restart of servers can take from several seconds to a minute. During this time connection to this server is impossible.


  * One should not confuse the restart of a server with the restart of a server's system service. After changing the platform settings, restart the server using the corresponding command in MetaTrader 5 Administrator. If you just restart the trade server's service, the other components of the platform may not be notified of changes in the settings.

  
---  
  
## Stopping and Starting Servers

All MetaTrader 5 servers work as services in the operating system. If you need to temporarily stop them, you need to stop the corresponding services. This can be done in several ways:

  * in the [command line](../../Platform-Installation/Console-Setup.md) execute the command [server executable file] /stop. For example, mt5history.exe \stop.
  * in the command line execute the command sc stop [service name]. For example, sc stop mt5srv.
  * in the Start menu execute the command MetaTrader 5 Platform\\[server name]\Stop [server name]. For example, MetaTrader 5 Platform\History Server\Stop History Server.



In the same way the servers can be started:

  * in the [command line](../../Platform-Installation/Console-Setup.md) execute the command [server executable file] /start. For example, mt5history.exe \start.
  * in the command line execute the command sc start [service name]. For example, sc start mt5srv.
  * in the Start menu execute the command MetaTrader 5 Platform\\[server name]\Start [server name]. For example, MetaTrader 5 Platform\History Server\Start History Server.


