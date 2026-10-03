[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests TypeFill

[Previous](Requests-Type.md) | [Next](Requests-TypeTime.md)

# IMTRequest::TypeFill

Get the type of order filling specified in a request.

C++
    
    
    UINT  IMTRequest::TypeFill()  const

.NET (Gateway/Manager API)
    
    
    EnOrderFilling  CIMTRequest.TypeFill()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](../../Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.

# IMTRequest::TypeFill

Sets the order filling type in a request.

C++
    
    
    MTAPIRES  IMTRequest::TypeFill(
       const UINT      type  // Filling type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.TypeFill(
       EnOrderFilling  type  // Filling type
       )

### Parameters

**type**  
[in] Type of filling. To pass the type, theIMTOrder::EnOrderFillingenumeration is used..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
