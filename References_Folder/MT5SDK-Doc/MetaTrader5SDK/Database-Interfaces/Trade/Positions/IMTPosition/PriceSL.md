[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / PriceSL

[Previous](PriceCurrent.md) | [Next](PriceTP.md)

# IMTPosition::PriceSL

Gets the [Stop Loss (#stop-loss)](../../General-Principles/Types-of-Orders.md#stop-loss) level of a trade position.

C++
    
    
    double  IMTPosition::PriceSL()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.PriceSL()

### Return Value

The Stop Loss level of a trade position.

# IMTPosition::PriceSL

Sets the [Stop Loss (#stop-loss)](../../General-Principles/Types-of-Orders.md#stop-loss) level of a trade position.

C++
    
    
    MTAPIRES  IMTPosition::PriceSL(
       const double  price      // The Stop Loss level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.PriceSL(
       double        price      // The Stop Loss level
       )

### Parameters

**price**  
[in] The Stop Loss level of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
