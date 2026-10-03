[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Phone

[Previous](Address.md) | [Next](EMail.md)

# IMTUser::Phone

Get a client's phone number.

C++
    
    
    LPCWSTR  IMTUser::Phone()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Phone()

### Return Value

If successful, it returns a pointer to the string with the phone number. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Phone

Set a client's phone number.

C++
    
    
    MTAPIRES  IMTUser::Phone(
       LPCWSTR  phone      // Phone
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Phone(
       string   phone      // Phone
       )

### Parameters

**phone**  
[in] Client's phone number.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The phone number length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
