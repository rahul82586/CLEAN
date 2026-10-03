[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests PositionPriceSL

[Previous](Requests-PositionByExternalID.md) | [Next](Requests-PositionPriceTP.md)

# IMTExecution::PositionPriceSL

Gets the Stop Loss level specified for a position in an external trading system.

C++
    
    
    double  IMTExecution::PositionPriceSL()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.PositionPriceSL()

### Return Value

The Stop Loss level specified for an order in an external trading system.

# IMTExecution::PositionPriceSL

Sets the Stop Loss level specified for a position in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::PositionPriceSL(
       const double  price      // Stop Loss level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.PositionPriceSL(
       double        price      // Stop Loss level
       )

### Parameters

**price**  
[in] The Stop Loss level specified for a position in the external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
