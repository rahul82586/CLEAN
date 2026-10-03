[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Common Functions](../Common-Functions.md) / Free

[Previous](Allocate.md) | [Next](LoggerOut.md)

# IMTServerAPI::Free

Free memory allocated earlier by [IMTServerAPI::Allocate](Allocate.md). It is used to free memory allocated by the functions and interfaces of the MetaTrader 5 Server API.
    
    
    void  IMTServerAPI::Free(
       void*  ptr      // Pointer to a memory block
       )

### Parameters

**ptr**  
[in] A pointer to the released memory block allocated earlier byIMTServerAPI::Allocate.
