[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Group

[Previous](Requests-ExternalAccount.md) | [Next](Requests-Symbol.md)

# IMTRequest::Group

Get the group of the client who has sent the request.

C++
    
    
    LPCWSTR  IMTRequest::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.Group()

### Return Value

If successful, it returns a pointer to a string with the group of a user. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.
