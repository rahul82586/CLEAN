[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderExternalID

[Previous](Requests-Order.md) | [Next](Requests-OrderType.md)

# IMTExecution::OrderExternalID

Gets the number of an order in an external trading system.

C++
    
    
    LPCWSTR  IMTExecution::OrderExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.OrderExternalID()

### Return Value

If successful, it returns a pointer to a string with the order number. Otherwise, it returns NULL.

### Note

This is a required trade execution field.

# IMTExecution::OrderExternalID

Sets the number of an order in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::OrderExternalID(
       LPCWSTR  id      // Order number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderExternalID(
       string   id      // Order number
       )

### Parameters

**id**  
[in] The number of an order in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a required trade execution field.
