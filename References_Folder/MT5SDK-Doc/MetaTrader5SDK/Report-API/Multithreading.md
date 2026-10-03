[🏠 Document Start](../README.md) / [Report API](README.md) / Multithreading

[Previous](Memory-Management.md) | [Next](Ready-made-Examples.md)

# Multithreading

When writing a multithreaded application, a programmer must take into account some specific features of MetaTrader 5 Report API:

  * Calling Report API methods (IMTReportAPI interface methods, e.g., [IMTReportAPI::Chart*](Main-Interface-of-Reports/HTML-Reports/Charts.md), [IMTReport::HTML*](Main-Interface-of-Reports/HTML-Reports/HTML.md) etc.) are not thread safe. When accessing the same object from two threads, the programmer must ensure synchronization of access.
  * Calling the common interface methods (e.g., configuration bases interface: [IMTConGroup](../Configuration-Interfaces/Groups/IMTConGroup.md), [IMTConSymbol](../Configuration-Interfaces/Symbols/IMTConSymbol.md), [IMTConGroup](../Configuration-Interfaces/Groups/IMTConGroup.md) etc.) are also not thread safe. When accessing the same object from two threads, the programmer must ensure synchronization of access.



> All report module components must be thread safe.
