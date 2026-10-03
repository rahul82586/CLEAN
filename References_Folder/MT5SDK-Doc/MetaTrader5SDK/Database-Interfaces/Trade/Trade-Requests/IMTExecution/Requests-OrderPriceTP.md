[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderPriceTP

[Previous](Requests-OrderPriceSL.md) | [Next](Requests-DealExternalID.md)

# IMTExecution::OrderPriceTP

Gets the Take Profit level specified for an order in an external trading system.

C++
    
    
    double  IMTExecution::OrderPriceTP()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.OrderPriceTP()

### Return Value

The Take Profit level specified for an order in an external trading system.

# IMTExecution::OrderPriceTP

Sets the Take Profit level specified for an order in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::OrderPriceTP(
       const double  price      // Take Profit level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderPriceTP(
       double        price      // Take Profit level
       )

### Parameters

**price**  
[in] The Take Profit level specified for an order in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
