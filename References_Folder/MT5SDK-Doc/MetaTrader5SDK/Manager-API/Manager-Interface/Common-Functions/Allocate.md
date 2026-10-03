[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Common Functions](../Common-Functions.md) / Allocate

[Previous](../Common-Functions.md) | [Next](Free.md)

# IMTManagerAPI::Allocate

Memory allocation by an application. This is a pair method to [IMTManagerAPI::Free](Free.md).
    
    
    void*  IMTManagerAPI::Allocate(
       const UINT  bytes      // Amount of allocated memory
       )

### Parameters

**bytes**  
[in] Amount of allocated memory in bytes.

### Return Value

If successful, it returns a pointer to the allocated memory block, otherwise it returns Null.
