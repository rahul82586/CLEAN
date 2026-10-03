[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / FirstName

[Previous](Name.md) | [Next](LastName.md)

# IMTUser::FirstName

Get the client name.

C++
    
    
    LPCWSTR  IMTUser::FirstName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.FirstName()

### Return Value

If successful, it returns a pointer to a string with the client name. Otherwise NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::FirstName

Set the client name.

C++
    
    
    MTAPIRES  IMTUser::FirstName(
       LPCWSTR  first_name  // Client name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.FirstName(
       string   first_name  // Client name
       )

### Parameters

**name**  
[in] Client name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum client name length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
