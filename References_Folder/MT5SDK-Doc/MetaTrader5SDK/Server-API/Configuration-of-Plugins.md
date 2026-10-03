[🏠 Document Start](../README.md) / [Server API](README.md) / Configuration of Plugins

[Previous](Interaction-with-Servers.md) | [Next](Requirements-for-Plugins.md)

<a id="configuration-of-plugins"></a>
# Configuration of Plugins (#configuration-of-plugins)

In order for the server to start to use the plugin, you need to add its configuration via the administrator terminal:

![Plugins](images/admin_plugin_list.png)

To add or change the configuration of a plugin, click "![Add](images/add_button.png)Add" and "![Edit](images/edit_button.png)Edit", respectively. They can be found in the Edit menu, on the toolbar or in the context menu. When clicking them, the following window appears:

![Editing the plugin settings](images/plugin_edit.png)

Fill in the following fields in this window:

  * Enable — enable/disable the plugin. The plugin starts operating immediately after the option is enabled and the configuration is saved. To get started, server restart is not required. If you disable the option, the server will completely unload the plugin from memory. This enables update of plug-in DLL files without the need to reload the platform.
  * Configurable by managers — if this option is enabled, it will be possible to change the settings of the plugin via the manager terminal. To be able to change the plugin settings, a manager account must have the [IMTConManager::RIGHT_CFG_PLUGINS (#enmanagerrights)](../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission enabled.
  * Enable plugin profiling — after enabling the [profiling (#enable)](Configuration-of-Plugins.md#enable), the server will start collecting the statistics on the plugin, what allows estimating its performance and detecting possible problems of its operation. It is not recommended to keep this option always enabled, as profiling decreases the plugin performance.
  * Name — the name of the plugin configuration.
  * Module — select one of the plugin modules in the first field. This field displays all the plugins that are located in the folders /plugins and /reports of the server selected in the next field.



  * Each configuration of the plugin is bound to a specific server and thus influences the operation only of this server.


  * In case of any change in plugin settings, the server will try to reinitialize (call [IMTServerPlugin::Start](Plugin-Interface/Start.md)) all enabled plugins, which previously failed to initialize.

  
---  
  
Parameters

The block of managing external parameters of the plugin is available in the bottom part of the window. Such parameters can be implemented during the development of plugin modules; they allow managing them from the outside.

The following commands are used for managing parameters:

  * Add — add a new parameter. A line appears upon pressing this button. Specify the parameter name in the "Parameter" field, and the value of this parameter in the "Value" field. String type parameters are created by default. To select another type (integer or fractional) click the arrow on the "Add" button.
  * Edit — edit a selected parameter. The same action can be performed by a double click on the required field.
  * Delete — delete a selected parameter.



<a id="info"></a>
### Information (#info)

![Information](images/plugin_information.png)

This tab displays various information on the plugin module: description, copyright, author, version of the plugin module and version of MetaTrader 5 Server API used for developing this plugin.

<a id="profiling"></a>
## Profiling (#profiling)

The profiling is enabled using the "Enable plugin profiling option" in the plugin settings. This procedure allows estimating the plugin performance by measuring the time of calls of hooks and event handlers within the plugin. The time is estimated separately for each hook and handler in the plugin.

After enabling the profiling, the server will start gathering the statistics on the plugin operation and outputting the results in the [journal](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_journal) every 5 minutes. To request the journal records, use "Profile" keyword.

  * It is recommended to enable profiling during testing only, as it slows down plugins.
  * Profiling should be enabled before enabling the plugin. If the plugin is already enabled, it should be re-launched after enabling profiling. This is necessary for the correct data collection.

  
---  
  
The following information is gathered during profiling:

  * Hook/event handler state — two states are possible: active state (the hook/event handler was executing during estimation), unactive state (the hook/event handler was not executing during estimation). If a hook/handler stays in the active state for more than 5 seconds, a message about a possible deadlock is displayed (the second line in the example). If a hook/handler stays active for more than 0.5 seconds, a message informing that the hook/handler is too slow is displayed (third line in the example).



14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: unactive state   
14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: possible deadlock: 6000 msc in active state   
14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: too slow: max process time 1000 msc  
---  
  
  * Number of calls — the total number of calls of the hook/handler during the plugin operation.



14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: 5 calls   
---  
  
  * Time of last call — time of the last call of the hook/handler accurate to millisecond.



14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: last call at 2013.06.26 14:09:37.603  
---  
  
  * Minimal execution time — minimal time of execution of the hook/handler (in milliseconds) during the plugin operation.



14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: time min 0 msc  
---  
  
  * Maximal execution time — maximal time of execution of the hook/handler (in milliseconds) during the plugin operation.



14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: time max 2 msc  
---  
  
  * Average execution time — average time of execution of the hook/handler (in milliseconds) during the plugin operation.



14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: time avg 0 msc  
---  
  
  * Total execution time — total time of execution of the hook/handler (all calls in milliseconds) during the plugin operation.



14:10:01 Simple Plugin Profile IMTConSymbolSink::OnSymbolUpdate: time total 0 msc  
---
