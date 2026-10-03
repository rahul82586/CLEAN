[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Comment

[Previous](Requests-TickLast.md) | [Next](Requests-Flags.md)

# IMTConfirm::Comment

Get a comment to the confirmation of a trade request.

C++
    
    
    LPCWSTR  IMTConfirm::Comment()  const

.NET (Gateway/Manager API)
    
    
    sting  CIMTConfirm.Comment()

### Return Value

If successful, it returns a pointer to the string a comment. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConfirm](../Requests-IMTConfirm.md) object.

# IMTConfirm::Comment

Set a comment to the confirmation of a trade request.

C++
    
    
    MTAPIRES  IMTConfirm::Comment(
       LPCWSTR  comment      // Comment
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Comment(
       string   comment      // Comment
       )

### Parameters

**comment**  
[in] A comment to request confirmation.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This comment is displayed in the trading dialog of a client.
