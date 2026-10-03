[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Login

[Previous](Clear.md) | [Next](Group.md)

# IMTUser::Login

Get the login of a user.

C++
    
    
    UINT64  IMTUser::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTUser.Login()

### Return Value

The login of a user.

# IMTUser::Login

Set the login of a user.

C++
    
    
    MTAPIRES  IMTUser::Login(
       const UINT64  login      // User's login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Login(
       ulong         login      // User's login
       )

### Parameters

**login**  
[in] The login of a user.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The login number must match the range set for a trade server, and be greater than the last created one.
