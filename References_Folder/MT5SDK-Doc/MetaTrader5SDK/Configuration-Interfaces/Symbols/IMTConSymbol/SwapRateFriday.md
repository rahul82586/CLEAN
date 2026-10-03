[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SwapRateFriday

[Previous](SwapRateThursday.md) | [Next](SwapRateSaturday.md)

# IMTConSymbol::SwapRateFriday

Get swap multiplier for Fridays.

C++
    
    
    double  IMTConSymbol::SwapRateFriday()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.SwapRateFriday()

Python (Manager API)
    
    
    MTConSymbol.SwapRateFriday

### Return Value

Swap multiplier.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.

# IMTConSymbol::SwapRateFriday

Set swap multiplier for Fridays.

C++
    
    
    MTAPIRES  IMTConSymbol::SwapRateFriday(
       const double  rate      // Swap multiplier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SwapRateFriday(
       double        rate      // Swap multiplier
       )

Python (Manager API)
    
    
    MTConSymbol.SwapRateFriday

### Parameters

**rate**  
[in] Swap multiplier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.
