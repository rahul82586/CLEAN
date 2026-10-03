[🏠 Document Start](../README.md) / [Server API](README.md) / Requirements for Plugins

[Previous](Configuration-of-Plugins.md) | [Next](Creating-a-Simple-Plugin.md)

# Requirements for Plugins

When developing plugins, it is necessary to meet the following requirements:

  * The bitness of plugins must comply with the bitness of the servers they are used on. 64-bit plugins do not work on 32-bit servers and vice versa.
  * Since the plugin is running in the server address space, it:


  * should use the memory very efficiently;
  * should fragment memory as little as possible;
  * should not cause memory leaks.
  * A plugin in no case should generate unhandled exceptions.
  * A plugin must quickly return control from event handlers and hooks.


