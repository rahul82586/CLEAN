[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TimeStart

[Previous](SwapRateSaturday.md) | [Next](TimeExpiration.md)

# IMTConSymbol::TimeStart

Get the start date of trading for a symbol.

C++
    
    
    INT64  IMTConSymbol::TimeStart()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConSymbol.TimeStart()

Python (Manager API)
    
    
    MTConSymbol.TimeStart

### Return Value

The start date of trading for a symbol. The date is specified as seconds that have elapsed since 01.01.1970.

# IMTConSymbol::TimeStart

Set the start date of trading for a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::TimeStart(
       const INT64  start      // Trading start date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TimeStart(
       ulong        start      // Trading start date
       )

Python (Manager API)
    
    
    MTConSymbol.TimeStart

### Parameters

**start**  
[in] Symbol trading start date. The date is specified as seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
