[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapRateSunday

[Previous](SwapFlagsDefault.md) | [Next](SwapRateSundayDefault.md)

# IMTConGroupSymbol::SwapRateSunday

Get the Sunday swap multiplier specified in symbol settings for the given group.

C++
    
    
    double  IMTConGroupSymbol::SwapRateSunday()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.SwapRateSunday()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapRateSunday

### Return Value

Swap multiplier.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.

# IMTConGroupSymbol::SwapRateSunday

Set Sunday swap multiplier in symbol settings for the given group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapRateSunday(
       const double  rate      // Swap multiplier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapRateSunday(
       double        rate      // Swap multiplier
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapRateSunday

### Parameters

**rate**  
[in] Swap multiplier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.
