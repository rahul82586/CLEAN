[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Common Functions](../Common-Functions.md) / Free

[Previous](Allocate.md) | [Next](LoggerOut.md)

# IMTAdminAPI::Free

Free memory allocated earlier by [IMTAdminAPI::Allocate](Allocate.md) method. It is used to free memory allocated by the functions and interfaces of the MetaTrader 5 Manager API.
    
    
    void  IMTAdminAPI::Free(
       void*  ptr      // Pointer to a memory block
       )

### Parameters

**ptr**  
[in] A pointer to the released memory block allocated earlier byIMTAdminAPI::Allocate.
