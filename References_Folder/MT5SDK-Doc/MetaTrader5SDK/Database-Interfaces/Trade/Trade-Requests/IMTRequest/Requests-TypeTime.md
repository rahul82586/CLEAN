[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests TypeTime

[Previous](Requests-TypeFill.md) | [Next](Requests-Flags.md)

# IMTRequest::TypeTime

Get the type of order expiration specified in a request.

C++
    
    
    UINT  IMTRequest::TypeTime()  const

.NET (Gateway/Manager API)
    
    
    EnOrderTime  CIMTRequest.TypeTime()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](../../Orders/IMTOrder/Enumerations.md#enordertime) enumeration.

# IMTRequest::TypeTime

Set the order expiration type in a request.

C++
    
    
    MTAPIRES  IMTRequest::TypeTime(
       const UINT  type      // Expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.TypeTime(
       EnOrderTime type      // Expiration type
       )

### Parameters

**type**  
[in] Order expiration type. To pass the type, theIMTOrder::EnOrderTimeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
