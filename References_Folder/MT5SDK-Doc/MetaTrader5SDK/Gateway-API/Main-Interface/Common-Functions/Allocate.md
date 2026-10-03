[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Common Functions](../Common-Functions.md) / Allocate

[Previous](../Common-Functions.md) | [Next](Free.md)

# IMTGatewayAPI::Allocate

Memory allocation by an application. It is paired to the [IMTGatewayAPI::Free](Free.md) method.
    
    
    void*  IMTGatewayAPI::Allocate(
       const UINT  bytes      // Amount of allocated memory
       )

### Parameters

**bytes**  
[in] Amount of allocated memory in bytes.

### Return Value

If successful, it returns a pointer to the allocated memory block, otherwise it returns NULL.
