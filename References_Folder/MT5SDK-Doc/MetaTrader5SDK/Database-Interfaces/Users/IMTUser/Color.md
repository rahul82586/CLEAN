[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Color

[Previous](Comment.md) | [Next](PhonePassword.md)

# IMTUser::Color

Get the color of the client. This is the color of the client's requests shown when handling the requests via the manager terminal.

C++
    
    
    COLORREF  IMTUser::Color()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTUser.Color()

### Return Value

The color of the client's requests shown when handling the requests via the manager terminal.

# IMTUser::Color

Set the color of the client. This is the color of the client's requests shown when handling the requests via the manager terminal.

C++
    
    
    MTAPIRES  IMTUser::Color(
       const COLORREF  color      // Color
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Color(
       uint            color      // Color
       )

### Parameters

**color**  
[in] The color of the client's requests shown when handling the requests via the manager terminal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
