[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / Extra

[Previous](Flags.md) | [Next](Text.md)

# Extra

Get additional information about the comment.

C++
    
    
    LPCWSTR  IMTComment::Text()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTComment.Text()

### Return Value

If successful, the method returns a pointer to a string with information. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTComment](../IMTComment.md) object.

# IMTComment::Text

Set additional information for the comment.

C++
    
    
    MTAPIRES  IMTComment::Text(
       LPCWSTR       extra       // Additional information
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.Text(
       string        extra       // Additional information
       )

### Parameters

**extra**  
[in] Additional information.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The IMTComment::Extra field can be used for adding additional information to a comment. For example, you can indicate a phone number on which the call was made.
