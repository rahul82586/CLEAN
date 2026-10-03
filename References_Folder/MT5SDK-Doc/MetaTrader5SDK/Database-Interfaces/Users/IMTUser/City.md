[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / City

[Previous](Language.md) | [Next](State.md)

# IMTUser::City

Get the client's city of residence.

C++
    
    
    LPCWSTR  IMTUser::City()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.City()

### Return Value

If successful, it returns a pointer to a string with the client's city. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::City

Set the client's city of residence.

C++
    
    
    MTAPIRES  IMTUser::City(
       LPCWSTR  city      // City
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.City(
       string   city      // City
       )

### Parameters

**city**  
[in] The client's city of residence.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The city name length is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
