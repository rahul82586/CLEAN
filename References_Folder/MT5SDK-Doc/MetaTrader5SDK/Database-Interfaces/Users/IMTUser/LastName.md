[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LastName

[Previous](FirstName.md) | [Next](MiddleName.md)

# IMTUser::LastName

Get the client's last name.

C++
    
    
    LPCWSTR  IMTUser::LastName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.LastName()

### Return Value

If successful, it returns a pointer to a string with the client's last name. Otherwise NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::LastName

Set the client's last name.

C++
    
    
    MTAPIRES  IMTUser::LastName(
       LPCWSTR  last_name  // Client's last name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.LastName(
       string   last_name  // Client's last name
       )

### Parameters

**name**  
[in] Client's last name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum last name length is limited to 128 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
