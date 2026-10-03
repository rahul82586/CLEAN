[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Common Functions](../Common-Functions.md) / Allocate

[Previous](../Common-Functions.md) | [Next](Free.md)

# IMTServerAPI::Allocate

Memory allocation by a server plugin. This is a pair method to [IMTServerAPI::Free](Free.md).
    
    
    void*  IMTServerAPI::Allocate(
       const UINT  bytes      // Amount of allocated memory
       )

### Parameters

**bytes**  
[in] Amount of allocated memory in bytes.

### Return Value

If successful, it returns a pointer to the allocated memory block, otherwise it returns NULL.

### Note

Allocation of memory by the IMTServerAPI::Allocate method is controlled by the server and checked for possible leaks.
