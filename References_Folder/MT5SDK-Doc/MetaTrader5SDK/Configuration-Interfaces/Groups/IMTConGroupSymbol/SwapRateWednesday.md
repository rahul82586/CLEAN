[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapRateWednesday

[Previous](SwapRateTuesdayDefault.md) | [Next](SwapRateWednesdayDefault.md)

# IMTConGroupSymbol::SwapRateWednesday

Get the Wednesday swap multiplier specified in symbol settings for the given group.

C++
    
    
    double  IMTConGroupSymbol::SwapRateWednesday()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.SwapRateWednesday()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapRateWednesday

### Return Value

Swap multiplier.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.

# IMTConGroupSymbol::SwapRateWednesday

Set the Wednesday swap multiplier in symbol settings for the given group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapRateWednesday(
       const double  rate      // Swap multiplier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapRateWednesday(
       double        rate      // Swap multiplier
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapRateWednesday

### Parameters

**rate**  
[in] Swap multiplier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.
