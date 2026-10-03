[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests PositionPriceTP

[Previous](Requests-PositionPriceSL.md) | [Next](Requests-EOSSessionStart.md)

# IMTExecution::PositionPriceTP

Gets the Take Profit level specified for a position in an external trading system.

C++
    
    
    double  IMTExecution::PositionPriceTP()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.PositionPriceTP()

### Return Value

The Take Profit level specified for a position in an external trading system.

# IMTExecution::PositionPriceTP

Sets the Take Profit level specified for an order in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::PositionPriceTP(
       const double  price      // Take Profit level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.PositionPriceTP(
       double        price      // Take Profit level
       )

### Parameters

**price**  
[in] The Take Profit level specified for a position in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
