[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Controlling Orders in External System](../Controlling-Orders-in-External-System.md) / GatewayOrdersAnswer

[Previous](GatewayOrderArrayCreate.md) | [Next](../Synchronizing-Trading-Data.md)

# IMTGatewayAPI::GatewayOrdersAnswer

The method is used to display in MetaTrader 5 Administrator the client's current pending orders placed at the external trading system.

The functionality is currently under development.  
---  
      
    
    MTAPIRES  IMTGatewayAPI::GatewayOrdersAnswer(
       const MTAPIRES          result,           // Result
       const INT64*            orders_time,      // Order fixing time
       const IMTOrderArray*    orders            // Array of orders
       )

### Parameters

**result**  
[in] MT_RET_OK response code is used if data on positions has been successfully received from an external system. Otherwise, the appropriateerror codeis to be returned.

**orders_time**  
[in] Orders state fixing time, specified in seconds that have elapsed since 01.01.1970.

**orders**  
[in]An object of the array of ordersreceived from an external system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
