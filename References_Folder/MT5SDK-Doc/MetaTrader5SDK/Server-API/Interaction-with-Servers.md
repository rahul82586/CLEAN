[🏠 Document Start](../README.md) / [Server API](README.md) / Interaction with Servers

[Previous](Purpose-of-the.md) | [Next](Configuration-of-Plugins.md)

# Interaction with Servers

The information provided in this section will help the developer to clearly understand how the server and the plugin interact.

  * The server can only work with the plugins, whose bit is the same as that of the server. 64-bit servers only work with 64-bit plugins, 32-bit servers — only with 32-bit plugins.  
In connection with this feature, you should always develop plugins in two versions — the 32- and 64-bit.  
It is recommended to give the appropriate names depending on the versions: PluginName.dll and PluginName64.dll. Our company uses the same naming standard.
  * Plugins can run on trade, history and backup servers. Access servers do not support plugins.

  
---  
  
## Initialization of Plugins

The first stage of interaction is the initialization of plugins:

  1. When starting the server scans its directories /plugins and /reports, including all subdirectories, and finds all files with the extension DLL.
  2. The server tries to load all found dll-files and call the [MTServerAbout](Entry-Points/MTServerAbout.md) function in them, which returns the [MTPluginInfo](../Structures/MTPluginInfo.md) structure containing basic information about the plugin. If such a function cannot be called, then the dll-file is not a plugin.
  3. [MTPluginInfo](../Structures/MTPluginInfo.md) informs the server about the version of the API, using which the plugin was compiled. The plugin version must be supported by the server.  
If the version of the plugin is not supported, then it will not be downloaded, and the appropriate entry will appear in the server log. In this case, you should update MetaTrader 5 Server API and recompile the plugin.



## Reading Configuration Files

After viewing the directory and identifying the plugins, the server goes through all created [plugin configurations](Configuration-of-Plugins.md). Further the found plugins are loaded only in accordance with the configurations created previously by the system administrator (via the administrator terminal).

> As compared with MetaTrader 4, in the fifth version of the platform, for each plugin module you can create multiple configurations with different parameters. In such a case, the server will run several instances of the plugin.

For the plugins whose configurations are created (and enabled) on the server, the [MTServerCreate](Entry-Points/MTServerCreate.md) functions are called for creating plugin instances (object of the class that implements the interface [IMTServerPlugin](Plugin-Interface.md)).

## Work of the IMTServerPlugin Interface

The [IMTServerPlugin](Plugin-Interface.md) interface contains three methods:

Method | Description  
---|---  
Release | This method removes the created object. In general, the API objects do not count references (AddRef). Thus, when calling the IMTServerPlugin::Release method, the object is unconditionally removed, and not just the access counter is decreased.  
Start | The IMTServerPlugin::Start method is called by the server to notify the plugin about the start of operation. It passes to the plugin the IMTServerAPI* server parameter — the interface that implements the server API (the interface used for interaction with the server). The IMTServerPlugin::Start method is called by the server at boot time, after preparing all the databases for work. For secondary trade servers and history servers, the IMTServerPlugin::Start method is called after the preparation of databases and synchronization with the main trade server. Also, this method is called when [enabling a plugin configuration (#enable)](Configuration-of-Plugins.md#enable). A plugin starts processing of [events (#events)](Creating-a-Simple-Plugin.md#events) only after the IMTServerPlugin::Start method is executed.  
Stop | This method is called during a server shutdown (e.g. reboot) before removing a plugin. Also, the IMTServerPlugin::Stop method is called when [disabling a plugin configuration (#enable)](Configuration-of-Plugins.md#enable). In this method, the plugin must release all the resources it occupies, and it has no more right to access the server through IMTServerAPI. After the completion of the IMTServerPlugin::Stop method, an object can be destroyed at any time. The DLL-library of a plugin is unloaded from the memory only after all the objects that correspond to it are removed.  
  
> When restarting a server, plugins are completely unloaded and then restarted. In this case, all plugins are disabled simultaneously: they stop receiving events, Stop methods are called for them and after that all their DLL files are unloaded from the memory.
