[🏠 Document Start](../README.md) / [Report API](README.md) / Memory Management

[Previous](Charts.md) | [Next](Multithreading.md)

# Memory Management

The correct approach to the use of memory is one of the key points in the development of reports. There are the following requirements for working with memory:

  * Since the DLL libraries work in the address space of the server, they must be memory efficient. In addition, the report library should have limited memory re-allocation to prevent it from too much fragmentation.
  * All interface objects are allocated using the Create methods and removed using the Release methods.
  * In cases where the API itself allocates memory (e.g., the [IMTReportAPI::UserLogins](Main-Interface-of-Reports/Users/UserLogins.md) function, which returns a dynamic array of clients from the specified group), it is necessary to free the memory using the method [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md).  
Pair to the method IMTReportAPI::Free is the method [IMTReportAPI::Allocate](Main-Interface-of-Reports/Common-Functions/Allocate.md), which allows to allocate memory.


