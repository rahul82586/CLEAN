[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderTypeFill

[Previous](Requests-OrderActivationMode.md) | [Next](Requests-OrderTimeExpiration.md)

# IMTExecution::OrderTypeFill

Gets order filling type set in an external trading system.

C++
    
    
    UINT  IMTExecution::OrderTypeFill()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.OrderTypeFill()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](../../Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.

# IMTExecution::OrderTypeFill

Sets order filling type set in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::OrderTypeFill(
       const UINT  type      // Type of filling
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderTypeFill(
       uint        type      // Type of filling
       )

### Parameters

**type**  
[in] Order filling type. To pass the type, theIMTOrder::EnOrderFillingenumeration is used..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
