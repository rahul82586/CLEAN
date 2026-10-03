[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / EMail

[Previous](Phone.md) | [Next](ID.md)

# IMTUser::EMail

Get the client's email address.

C++
    
    
    LPCWSTR  IMTUser::EMail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.EMail()

### Return Value

If successful, it returns a pointer to a string with the email address. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::EMail

Set the client's email address.

C++
    
    
    MTAPIRES  IMTUser::EMail(
       LPCWSTR  email      // email
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.EMail(
       string   email      // email
       )

### Parameters

**email**  
[in] The email address of a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the address is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
