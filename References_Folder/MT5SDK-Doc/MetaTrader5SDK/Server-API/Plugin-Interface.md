[🏠 Document Start](../README.md) / [Server API](README.md) / Plugin Interface

[Previous](Entry-Points/MTServerCreate.md) | [Next](Plugin-Interface/Release.md)

# Plugin Interface IMTServerPlugin

Every plugin written using the MetaTrader 5 Server API must implement the plugin interface IMTServerPlugin. This interface is used for managing the plugin from the server side.

Interface IMTServerPlugin contains the following methods:

Method | Description  
---|---  
[Release](Plugin-Interface/Release.md) | This method removes the created object. In general, the API objects do not count references (AddRef). Thus, when calling the IMTServerPlugin::Release method, the object is unconditionally removed, and not just the access counter is decreased.  
[Start](Plugin-Interface/Start.md) | The IMTServerPlugin::Start method is called by the server to notify the plugin about the start of operation. It passes to the plugin the IMTServerAPI* server parameter — the interface that implements the server API (the interface used for interaction with the server). The IMTServerPlugin::Start method is called by the server at boot time, after preparing all the databases for work. For secondary trade servers and history servers, the IMTServerPlugin::Start method is called after the preparation of databases and synchronization with the main trade server. Also, this method is called when [enabling a plugin configuration (#enable)](Configuration-of-Plugins.md#enable).  
[Stop](Plugin-Interface/Stop.md) | This method is called during a server shutdown (e.g. reboot) before removing a plugin. Also, the IMTServerPlugin::Stop method is called when [disabling a plugin configuration (#enable)](Configuration-of-Plugins.md#enable). In this method, the plugin must release all the resources it occupies, and it has no more right to access the server through IMTServerAPI. After the completion of the IMTServerPlugin::Stop method, an object can be destroyed at any time. The DLL-library of a plugin is unloaded from the memory only after all the objects that correspond to it are removed.
