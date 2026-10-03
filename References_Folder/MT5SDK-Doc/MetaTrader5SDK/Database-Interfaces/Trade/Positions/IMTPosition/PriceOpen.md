[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / PriceOpen

[Previous](TimeUpdateMsc.md) | [Next](PriceCurrent.md)

# IMTPosition::PriceOpen

Gets the weighted average open price of a position.

C++
    
    
    double  IMTPosition::PriceOpen()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.PriceOpen()

### Return Value

The weighted average open price of a position.

### Note

The weighted average price is calculated by the following formula: (price of deal 1 * volume of deal 1 1 + ... + price of deal N * volume of deal N) / (volume of deal 1 + ... + volume of deal N).

# IMTPosition::PriceOpen

Set the weighted average open price of a position.

C++
    
    
    MTAPIRES  IMTPosition::PriceOpen(
       const double  price      // Open price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.PriceOpen(
       double        price      // Open price
       )

### Parameters

**price**  
[in] The weighted average open price of a position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
