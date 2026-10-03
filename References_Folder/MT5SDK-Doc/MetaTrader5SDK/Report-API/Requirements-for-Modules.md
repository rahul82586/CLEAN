[🏠 Document Start](../README.md) / [Report API](README.md) / Requirements for Modules

[Previous](Request-for-Reports.md) | [Next](Creating-a-Simple-Report.md)

# Requirements for Modules

When developing the modules, it is necessary to meet the following requirements:

  * The bitness of the modules must comply with the bitness of the servers they are used on. 64-bit reports modules do not work on 32-bit servers and vice versa.
  * Since the module is running in the server address space, it:


  * should use the memory very efficiently;
  * should fragment memory as little as possible;
  * should not cause memory leaks.
  * A module should in no case generate unhandled exceptions.
  * A module must quickly return control from event handlers and hooks.


