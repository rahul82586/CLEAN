[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / PriceSettle

[Previous](IEFlags.md) | [Next](PriceLimitMax.md)

# IMTConSymbol::PriceSettle

Get the clearing price of the previous session.

C++
    
    
    double  IMTConSymbol::PriceSettle()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.PriceSettle()

Python (Manager API)
    
    
    MTConSymbol.PriceSettle

### Return Value

The clearing price of the previous session.

# IMTConSymbol::PriceSettle

Set the clearing price of the previous session.

C++
    
    
    MTAPIRES  IMTConSymbol::PriceSettle(
       const double  price      // Clearing price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.PriceSettle(
       double        price      // Clearing price
       )

Python (Manager API)
    
    
    MTConSymbol.PriceSettle

### Parameters

**value**  
[in] The clearing price of the previous session.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
