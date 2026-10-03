[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TimeExpiration

[Previous](TimeStart.md) | [Next](SessionQuoteAdd.md)

# IMTConSymbol::TimeExpiration

Get the date of trading expiration for a symbol.

C++
    
    
    INT64  IMTConSymbol::TimeExpiration()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConSymbol.TimeExpiration()

Python (Manager API)
    
    
    long  MTConSymbol.TimeExpiration

### Return Value

The date of trading expiration for a symbol. The date is specified as seconds that have elapsed since 01.01.1970.

### Note

It is considered that there is no time limitation for trading by a symbol if both [IMTConSymbol::TimeStart](TimeStart.md) and IMTConSymbol::TimeExpiration are equal to 0.

# IMTConSymbol::TimeExpiration

Set the date of trading expiration for a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::TimeExpiration(
       const INT64  expiration      // Trading expiration date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TimeExpiration(
       ulong        expiration      // Trading expiration date
       )

Python (Manager API)
    
    
    long  MTConSymbol.TimeExpiration

### Parameters

**expiration**  
[in] Trading expiration date. The date is specified as seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

It is considered that there is no time limitation for trading by a symbol if both [IMTConSymbol::TimeStart](TimeStart.md) and IMTConSymbol::TimeExpiration are equal to 0.
