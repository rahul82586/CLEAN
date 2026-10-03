[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderTypeTime

[Previous](Requests-OrderTimeExpiration.md) | [Next](Requests-OrderPriceTrigger.md)

# IMTExecution::OrderTypeTime

Gets order expiration type set in an external trading system.

C++
    
    
    UINT  IMTExecution::OrderTypeTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.OrderTypeTime()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](../../Orders/IMTOrder/Enumerations.md#enordertime) enumeration.

# IMTExecution::OrderTypeTime

Sets order expiration type set in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::OrderTypeTime(
       const UINT  type      // Expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderTypeTime(
       uint        type      // Expiration type
       )

### Parameters

**type**  
[in] Order expiration type. To pass the type, theIMTOrder::EnOrderTimeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
