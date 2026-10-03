[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Common Functions](../Common-Functions.md) / Free

[Previous](Allocate.md) | [Next](LoggerOut.md)

# IMTManagerAPI::Free

Free memory allocated earlier by [IMTManagerAPI::Allocate](../../Administrator-Interface/Common-Functions/Allocate.md). It is used to free memory allocated by the functions and interfaces of the MetaTrader 5 Manager API.
    
    
    void  IMTManagerAPI::Free(
       void*  ptr      // Pointer to a memory block
       )

### Parameters

**ptr**  
[in] A pointer to the released memory block allocated earlier byIMTManagerAPI::Allocate.
