[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderPriceTrigger

[Previous](Requests-OrderTypeTime.md) | [Next](Requests-OrderPriceSL.md)

# IMTExecution::OrderPriceTrigger

Gets the activation price of a stop-limit order set in an external trading system.

C++
    
    
    double  IMTExecution::OrderPriceTrigger()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.OrderPriceTrigger()

### Return Value

Order activation price in an external trading system.

# IMTExecution::OrderPriceTrigger

Sets the activation price of a stop-limit order set in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::OrderPriceTrigger(
       const double  price      // Order activation price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderPriceTrigger(
       double        price      // Order activation price
       )

### Parameters

**price**  
[in] Order activation price in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
