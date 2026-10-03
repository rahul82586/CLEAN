[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / OTPSecret

[Previous](PasswordHash.md) | [Next](Leverage.md)

# IMTUser::OTPSecret

Get a secret key which links a trading account and a one-time password generator.

C++
    
    
    LPCWSTR  IMTUser::OTPSecret()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.OTPSecret()

### Return Value

If successful, it returns a pointer to a string with a comment to the client. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::OTPSecret

Set a secret key which links a trading account and a one-time password generator.

C++
    
    
    MTAPIRES  IMTUser::OTPSecret(
       LPCWSTR  otp_secret    // Secret key
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.OTPSecret(
       string   otp_secret    // Secret key
       )

### Parameters

**otp_secret**  
[in] Secret key.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum key length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed down to this number of characters.
