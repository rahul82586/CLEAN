[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Common Functions](../Common-Functions.md) / Free

[Previous](Allocate.md) | [Next](LoggerOut.md)

# IMTGatewayAPI::Free

Free memory allocated earlier by [IMTGatewayAPI::Allocate](Allocate.md). It is used to free memory allocated by the functions and interfaces of the MetaTrader 5 Gateway API.
    
    
    void  IMTGatewayAPI::Free(
       void*  ptr      // Pointer to a memory block
       )

### Parameters

**ptr**  
[in] A pointer to the released memory block allocated earlier byIMTGatewayAPI::Allocate.
