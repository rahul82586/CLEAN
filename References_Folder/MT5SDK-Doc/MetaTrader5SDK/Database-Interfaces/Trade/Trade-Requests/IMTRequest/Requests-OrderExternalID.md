[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests OrderExternalID

[Previous](Requests-Order.md) | [Next](Requests-PriceOrder.md)

# IMTRequest::OrderExternalID

Get the order ID in external trading systems.

C++
    
    
    LPCWSTR  IMTRequest::OrderExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.OrderExternalID()

### Return Value

If successful, it returns a pointer to the string with the identifier. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.

  * When a dealer confirms a trade request to open a new order (a market or a pending order). In this case the field is filled with a value of [IMTConfirm::OrderID](../IMTConfirm/Requests-OrderID.md).
  * When the server receives a request to modify\delete\execute an existing order. In this case the field is filled with a value of [IMTOrder::ExternalID](../../Orders/IMTOrder/ExternalID.md).



# IMTRequest::OrderExternalID

Set the order ID in external trading systems.

C++
    
    
    MTAPIRES  IMTRequest::OrderExternalID(
       LPCWSTR  id      // External ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.OrderExternalID(
       string   id      // External ID
       )

### Parameters

**id**  
[in] The order ID in external systems.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The ID length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

  * When a dealer confirms a trade request to open a new order (a market or a pending order). In this case the field is filled with a value of [IMTConfirm::OrderID](../IMTConfirm/Requests-OrderID.md).
  * When the server receives a request to modify\delete\execute an existing order. In this case the field is filled with a value of [IMTOrder::ExternalID](../../Orders/IMTOrder/ExternalID.md).


