[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateDelete

[Previous](TranslateUpdate.md) | [Next](TranslateClear.md)

# IMTConGateway::TranslateDelete

Remove a setting of conversion of data transmitted by the gateway by the index.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateDelete(
       const UINT  pos      // Setting position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateDelete(
       uint        pos      // Setting position
       )

Python (Manager API)
    
    
    MTConGateway.TranslateDelete(
       pos         # Setting position
       )

### Parameters

**pos**  
[in] Setting position, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
