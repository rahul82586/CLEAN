[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Address

[Previous](ZipCode.md) | [Next](Phone.md)

# IMTUser::Address

Get the address of a client.

C++
    
    
    LPCWSTR  IMTUser::Address()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Address()

### Return Value

If successful, it returns a pointer to the string with the address. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Address

Set the address of a client.

C++
    
    
    MTAPIRES  IMTUser::Address(
       LPCWSTR  code      // Address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Address(
       string   code      // Address
       )

### Parameters

**code**  
[in] The address of a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the address is 128 characters (including the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
