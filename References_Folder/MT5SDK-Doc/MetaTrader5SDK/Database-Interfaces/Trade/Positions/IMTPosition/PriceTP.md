[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / PriceTP

[Previous](PriceSL.md) | [Next](Volume.md)

# IMTPosition::PriceTP

Gets the [Take Profit (#take-profit)](../../General-Principles/Types-of-Orders.md#take-profit) level of a trade position.

C++
    
    
    double  IMTPosition::PriceTP()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.PriceTP()

### Return Value

The Take Profit level of a trade position.

# IMTPosition::PriceTP

Sets the [Take Profit (#take-profit)](../../General-Principles/Types-of-Orders.md#take-profit) level of a trade position.

C++
    
    
    MTAPIRES  IMTPosition::PriceTP(
       const double  price      // The Take Profit level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.PriceTP(
       double        price      // The Take Profit level
       )

### Parameters

**price**  
[in] The Take Profit level of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
