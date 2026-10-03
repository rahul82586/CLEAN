[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderPriceSL

[Previous](Requests-OrderPriceTrigger.md) | [Next](Requests-OrderPriceTP.md)

# IMTExecution::OrderPriceSL

Gets the Stop Loss level specified for an order in an external trading system.

C++
    
    
    double  IMTExecution::OrderPriceSL()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.OrderPriceSL()

### Return Value

The Stop Loss level specified for an order in an external trading system.

# IMTExecution::OrderPriceSL

Sets the Stop Loss level specified for an order in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::OrderPriceSL(
       const double  price      // Stop Loss level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderPriceSL(
       double        price      // Stop Loss level
       )

### Parameters

**price**  
[in] The Stop Loss level specified for an order in the external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
