[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateClear

[Previous](TranslateDelete.md) | [Next](TranslateShift.md)

# IMTConGateway::TranslateClear

Clear the list of price data conversion parameters of a gateway.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateClear()

Python (Manager API)
    
    
    MTConGateway.TranslateClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of data conversion of a gateway.
