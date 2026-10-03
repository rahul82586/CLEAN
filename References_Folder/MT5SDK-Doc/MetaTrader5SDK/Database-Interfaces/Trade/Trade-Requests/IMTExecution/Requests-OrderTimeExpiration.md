[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderTimeExpiration

[Previous](Requests-OrderTypeFill.md) | [Next](Requests-OrderTypeTime.md)

# IMTExecution::OrderTimeExpiration

Gets order expiration time set in an external trading system.

C++
    
    
    INT64  IMTExecution::OrderTimeExpiration()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTExecution.OrderTimeExpiration()

### Return Value

Date and time of the expiration of an order, in seconds that have elapsed since 01.01.1970. The 0 value means that the order has no expiration.

# IMTExecution::OrderTimeExpiration

Sets order expiration time set in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::OrderTimeExpiration(
       const INT64  time      // Expiration time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderTimeExpiration(
       long         time      // Expiration time
       )

### Parameters

**time**  
[in] Date and time of the expiration of an order, in seconds that have elapsed since 01.01.1970. The 0 value means that the order has no expiration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
