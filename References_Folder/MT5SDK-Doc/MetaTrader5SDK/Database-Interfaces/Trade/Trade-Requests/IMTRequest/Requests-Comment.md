[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Comment

[Previous](Requests-SpreadDiffBalance.md) | [Next](Requests-ResultRetcode.md)

# IMTRequest::Comment

Get a comment to a trade request.

C++
    
    
    LPCWSTR  IMTRequest::Comment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.Comment()

### Return Value

If successful, it returns a pointer to the string a comment. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.

# IMTRequest::Comment

Set a comment to a trade request.

C++
    
    
    MTAPIRES  IMTRequest::Comment(
       LPCWSTR  comment      // Comment
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Comment(
       string   comment      // Comment
       )

### Parameters

**comment**  
[in] A comment to a request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum comment length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
