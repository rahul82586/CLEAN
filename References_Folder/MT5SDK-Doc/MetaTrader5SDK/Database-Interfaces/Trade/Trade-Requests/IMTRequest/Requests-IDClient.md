[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests IDClient

[Previous](Requests-ResultComment.md) | [Next](Requests-IP.md)

# IMTRequest::IDClient

Get the request ID on the side of the client who has sent the request.

C++
    
    
    UINT  IMTRequest::IDClient()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTRequest.IDClient()

### Return Value

The request ID on the side of the client who has sent the request.

### Note

This method is used for identifying own requests of an API application. When calling [IMTManagerAPI::DealerSend](../../../../Manager-API/Manager-Interface/Trade-Activity/Dealing/DealerSend.md), the identifier assigned to a request is passed to the ID parameter. This identifier is assigned to the IMTRequest::IDClient field.
