[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Country

[Previous](Account.md) | [Next](Language.md)

# IMTUser::Country

Get the client's country of residence.

C++
    
    
    LPCWSTR  IMTUser::Country()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Country()

### Return Value

If successful, it returns a pointer to the string with the country of residence. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Country

Set the client's country of residence.

C++
    
    
    MTAPIRES  IMTUser::Country(
       LPCWSTR  account      // Country
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Country(
       string   account      // Country
       )

### Parameters

**account**  
[in] The client's country of residence.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The country name length is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
