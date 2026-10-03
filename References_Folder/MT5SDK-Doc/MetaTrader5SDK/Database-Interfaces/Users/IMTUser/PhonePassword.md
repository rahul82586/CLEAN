[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / PhonePassword

[Previous](Color.md) | [Next](LastPassChange.md)

# IMTUser::PhonePassword

Get a client's phone password.

C++
    
    
    LPCWSTR  IMTUser::PhonePassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.PhonePassword()

### Return Value

If successful, it returns a pointer to a string with the phone password. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

To use the string after the object removal (call of the [IMTUser::Release](Release.md) method of this object), a copy of it should be created.

# IMTUser::PhonePassword

Set a client's phone password.

C++
    
    
    MTAPIRES  IMTUser::PhonePassword(
       LPCWSTR  password      // Phone password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.PhonePassword(
       string   password      // Phone password
       )

### Parameters

**password**  
[in] Client's phone password.

### Return Value

### Note

The phone password length is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
