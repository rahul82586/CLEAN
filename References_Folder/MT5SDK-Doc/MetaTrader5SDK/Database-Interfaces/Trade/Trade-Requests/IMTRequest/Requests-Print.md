[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Print

[Previous](Requests-Clear.md) | [Next](Requests-ID.md)

# IMTRequest::Print

Get a string description of a trade request.

C++
    
    
    LPCWSTR  IMTRequest::Print(
       MTAPISTR&  string      // Request description string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.Print()

### Parameters

**string**  
[out] The request description string.

### Return Value

A pointer to string that is passed as a parameter.

### Note

The description string does not include the login of the client, to whom the request belongs.
