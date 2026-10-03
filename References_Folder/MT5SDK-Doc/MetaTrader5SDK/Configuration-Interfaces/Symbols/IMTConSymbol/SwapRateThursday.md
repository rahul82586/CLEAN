[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SwapRateThursday

[Previous](SwapRateWednesday.md) | [Next](SwapRateFriday.md)

# IMTConSymbol::SwapRateThursday

Get swap multiplier for Thursdays.

C++
    
    
    double  IMTConSymbol::SwapRateThursday()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.SwapRateThursday()

Python (Manager API)
    
    
    MTConSymbol.SwapRateThursday

### Return Value

Swap multiplier.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.

# IMTConSymbol::SwapRateThursday

Set swap multiplier for Thursdays.

C++
    
    
    MTAPIRES  IMTConSymbol::SwapRateThursday(
       const double  rate      // Swap multiplier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SwapRateThursday(
       double        rate      // Swap multiplier
       )

Python (Manager API)
    
    
    MTConSymbol.SwapRateThursday

### Parameters

**rate**  
[in] Swap multiplier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.
