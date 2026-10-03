[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / Text

[Previous](Extra.md) | [Next](CommentType.md)

# IMTComment::Text

Get the comment text.

C++
    
    
    LPCWSTR  IMTComment::Text()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTComment.Text()

### Return Value

If successful, a pointer to the string with a text is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTComment](../IMTComment.md) object.

# IMTComment::Text

Set the comment text.

C++
    
    
    MTAPIRES  IMTComment::Text(
       LPCWSTR       text        // Comment text
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.Text(
       string        text        // Comment text
       )

### Parameters

**text**  
[in] Comment text.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Text length is not limited.

### 
