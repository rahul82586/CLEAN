[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Comment

[Previous](Status.md) | [Next](Color.md)

# IMTUser::Comment

Get a comment to a client.

C++
    
    
    LPCWSTR  IMTUser::Comment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Comment()

### Return Value

If successful, it returns a pointer to a string with a comment to the client. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Comment

Set a comment to a client.

C++
    
    
    MTAPIRES  IMTUser::Comment(
       LPCWSTR  comment      // Comment
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Comment(
       string   comment      // Comment
       )

### Parameters

**comment**  
[in] A comment to a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum comment length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
