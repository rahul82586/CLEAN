[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Common Functions](../Common-Functions.md) / Allocate

[Previous](../Common-Functions.md) | [Next](Free.md)

# IMTReportAPI::Allocate

Memory allocation by a server plugin. It is paired to the [IMTReportAPI::Free](Free.md) method.
    
    
    void*  IMTReportAPI::Allocate(
       const UINT  bytes      // Amount of allocated memory
       )

### Parameters

**bytes**  
[in] Amount of allocated memory in bytes.

### Return Value

If successful, it returns a pointer to the allocated memory block, otherwise it returns NULL.

### Note

Allocation of memory by the Allocate method is controlled by the server and checked for possible leaks.
