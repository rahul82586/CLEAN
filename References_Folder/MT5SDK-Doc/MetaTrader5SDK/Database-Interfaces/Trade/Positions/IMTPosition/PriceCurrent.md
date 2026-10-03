[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / PriceCurrent

[Previous](PriceOpen.md) | [Next](PriceSL.md)

# IMTPosition::PriceCurrent

Get the current price of the symbol, for which a trade position has been opened.

C++
    
    
    double  IMTPosition::PriceCurrent()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.PriceCurrent()

### Return Value

The current price of the symbol, for which a trade position has been opened.

# IMTPosition::PriceCurrent

Set the current price of the symbol, for which a trade position has been opened.

C++
    
    
    MTAPIRES  IMTPosition::PriceCurrent(
       const double  price      // Current price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.PriceCurrent(
       double        price      // Current price
       )

### Parameters

**price**  
[in] The current price of the symbol, for which a trade position has been opened.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
