[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / TranslateShift

[Previous](TranslateClear.md) | [Next](TranslateTotal.md)

# IMTConGateway::TranslateShift

Shift a setting of conversion of price data transmitted by the gateway in the list.

C++
    
    
    MTAPIRES  IMTConGateway::TranslateShift(
       const UINT  pos,       // Setting position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.TranslateShift(
       uint        pos,       // Setting position
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConGateway.TranslateShift(
       pos,        # Setting position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Setting position, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
