[🏠 Document Start](../README.md) / [Server API](README.md) / Ready-made Examples

[Previous](Debugging.md) | [Next](Entry-Points.md)

# Ready-made Examples

The installation package of the MetaTrader 5 Server API includes ready-made examples of server plugins represented as source code. Analyzing the examples will help the developer quicker understand the specifics of the Server API and implement their own plugins.

The plugin examples are located in the [/Examples (#exmaples)](../Getting-Started/Files-and-Folders.md#exmaples) folder of the MetaTrader 5 Server API installation directory.

  * ServerPlugin — this plugin demonstrates basic principle of working with the Server API:


  * basics of plugin making, basic concepts;
  * tracking events;
  * getting plugin parameters;
  * creation of server interfaces (objects) and working with them.


  * InterstRates — this plugin demonstrates how to subscribe to events and how to use the hooks of interest charging depending on the state of trade accounts.


  * APIExtension — example of handling custom commands sent from [Manager API](../Manager-API/Manager-Interface/Custom-Functions.md) and [Web API](../Web-API/Protocol-Extension.md). In turn, Web API and Manager API packages contain examples for sending commands handled by that plugin.
  * FeedCommission — example of implementing a custom algorithm for charging standard commissions at the end of a trading month. The plugin shows how to work with [external parameters](../Configuration-Interfaces/Plugins/IMTConPlugin/ParameterGet.md), use event handlers by the example of [IMTEndOfDaySink::OnEOMFinish](Interface-of-End-of-Day-Events/OnEOMFinish.md), calculate a client turnover by trades and charge the commission using a balance transaction.
  * SwapsCopier — example of using Manager API in Server API plugins. The plugin shows how to create a manager connection in a separate thread, subscribe it to symbol change events on a remote server and update swap settings of the symbols on the server, where the plugin is used.
  * StopOutReporter — the plugin sends email notifications to customers informing them of Margin Call or Stop Out on their accounts. The templates from the mc_notify.htm and so_notify.htm files are used for emails. During the first launch, the plugin saves them on the disk to read them afterwards. Thus, users are able to customize templates for their own needs.


  * SingleSessionPlugin — the plugin demonstrates how to limit the number of simultaneous connections per one client login.


