[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ID

[Previous](Requests-Print.md) | [Next](Requests-Login.md)

# IMTRequest::ID

Get the request ID.

C++
    
    
    UINT  IMTRequest::ID()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTRequest.ID()

### Return Value

Request ID.

### Note

Identifiers provide a uniqueness of trade requests, they are stored until server restart.
