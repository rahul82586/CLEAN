[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests OrderID

[Previous](Requests-DealID.md) | [Next](Requests-PositionExternalID.md)

# IMTConfirm::OrderID

Gets the number of an order in an external trading system.

C++
    
    
    LPCWSTR  IMTConfirm::OrderID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConfirm.OrderID()

### Return Value

If successful, it returns a pointer to a string with the order number. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of [IMTConfirm](../Requests-IMTConfirm.md) object.

# IMTConfirm::OrderID

Sets the number of an order in an external trading system.

C++
    
    
    MTAPIRES  IMTConfirm::OrderID(
       LPCWSTR  order_id      // Order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.OrderID(
       srting   order_id      // Order ticket
       )

### Parameters

**order_id**  
[in] The number of an order in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The ticket length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
