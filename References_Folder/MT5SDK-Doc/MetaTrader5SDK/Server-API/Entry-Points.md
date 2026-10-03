[🏠 Document Start](../README.md) / [Server API](README.md) / Entry Points

[Previous](Ready-made-Examples.md) | [Next](Entry-Points/MTServerAbout.md)

# Entry Points

Any DLL of a server plugin must implement two entry points (exported functions):

Entry point | Purpose  
---|---  
[MTServerAbout](Entry-Points/MTServerAbout.md) | The method that provides the initial information about the plugin to the server.  
[MTServerCreate](Entry-Points/MTServerCreate.md) | The method called by the server to create an instance of an object of the server plugin.  
  
An example of implementation is given in section ["Creating a simple plugin" (#entry)](Creating-a-Simple-Plugin.md#entry).
