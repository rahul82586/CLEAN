[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / PriceLimitMax

[Previous](PriceSettle.md) | [Next](PriceLimitMin.md)

# IMTConSymbol::PriceLimitMax

Get the maximum allowed price of the symbol.

C++
    
    
    double  IMTConSymbol::PriceLimitMax()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.PriceLimitMax()

Python (Manager API)
    
    
    MTConSymbol.PriceLimitMax

### Return Value

The maximum allowed price of the symbol.

# IMTConSymbol::PriceLimitMax

Set the maximum allowed price of the symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::PriceLimitMax(
       const double  price      // Maximum price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.PriceLimitMax(
       double        price      // Maximum price
       )

Python (Manager API)
    
    
    MTConSymbol.PriceLimitMax

### Parameters

**value**  
[in] The maximum allowed price of the symbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
