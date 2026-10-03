[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ResultComment

[Previous](Requests-ResultMarketLast.md) | [Next](Requests-IDClient.md)

# IMTRequest::ResultComment

Gets the comment added by a dealer after confirming the request.

C++
    
    
    LPCWSTR  IMTRequest::ResultComment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.ResultComment()

### Return Value

If successful, it returns a pointer to the string a comment. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.
