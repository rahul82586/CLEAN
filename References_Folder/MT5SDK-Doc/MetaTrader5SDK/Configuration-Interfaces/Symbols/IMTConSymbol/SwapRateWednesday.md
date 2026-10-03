[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SwapRateWednesday

[Previous](SwapRateTuesday.md) | [Next](SwapRateThursday.md)

# IMTConSymbol::SwapRateWednesday

Get swap multiplier for Wednesdays.

C++
    
    
    double  IMTConSymbol::SwapRateWednesday()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.SwapRateWednesday()

Python (Manager API)
    
    
    MTConSymbol.SwapRateWednesday

### Return Value

Swap multiplier.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.

# IMTConSymbol::SwapRateWednesday

Set swap multiplier for Wednesdays.

C++
    
    
    MTAPIRES  IMTConSymbol::SwapRateWednesday(
       const double  rate      // Swap multiplier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SwapRateWednesday(
       double        rate      // Swap multiplier
       )

Python (Manager API)
    
    
    MTConSymbol.SwapRateWednesday

### Parameters

**rate**  
[in] Swap multiplier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.

### Note

This multiplier is applied to the calculated swap value before charging on the specified day. With the value of 1 a regular amount is charged, 3 triples the swap, and no swap is charged with 0.
