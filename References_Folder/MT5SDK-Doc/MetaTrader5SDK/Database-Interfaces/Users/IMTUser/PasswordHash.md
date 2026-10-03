[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / PasswordHash

[Previous](LastPassChange.md) | [Next](OTPSecret.md)

# IMTUser::PasswordHash

Get the password hash of a client record.

C++
    
    
    MTAPIRES  IMTUser::PasswordHash(
       const UINT  type               // password type
       MTAPISTR&   password_hash      // password hash
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.PasswordHash(
       uint        type               // password type
       out string  password_hash      // password hash
       )

### Parameters

**type**  
[in] The type of the password, the hash of which should be received. The type is specified using theIMTUser::EnUsersPasswordsenumeration.

**password_hash**  
[out] A pointer to a string containing a password hash.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

For security reasons, client passwords are stored in the trading platform in the form of password hashes. In fact, the function returns a hash of a password hash.

This method is used only in the MetaTrader 5 Server API. When called from the Manager API, the method always returns an empty string for security reasons.
