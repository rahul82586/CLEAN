[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapRateTuesday

[Previous](SwapRateMondayDefault.md) | [Next](SwapRateTuesdayDefault.md)

# IMTConGroupSymbol::SwapRateTuesday

Get the Tuesday swap multiplier specified in symbol settings for the given group.

C++
    
    
    double  IMTConGroupSymbol::SwapRateTuesday()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.SwapRateTuesday()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapRateTuesday

### Return Value

Swap multiplier.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.

# IMTConGroupSymbol::SwapRateTuesday

Set the Tuesday swap multiplier in symbol settings for the given group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapRateTuesday(
       const double  rate      // Swap multiplier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapRateTuesday(
       double        rate      // Swap multiplier
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapRateTuesday

### Parameters

**rate**  
[in] Swap multiplier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.
