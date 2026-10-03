[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon MQL5Login

[Previous](IMTCon-Flags.md) | [Next](IMTCon-MQL5Password.md)

# IMTConVPS::MQL5Login

Get the MQL5 account login used for the Sponsored VPS.

C++
    
    
    LPCWSTR  IMTConVPS::MQL5Login()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConVPS.MQL5Login()

Python
    
    
    MTConVPS.MQL5Login

### Return Value

If successful, the method returns a pointer to a string with the login. Otherwise, it returns NULL.

### Note

The method is obsolete and is no longer used.

# IMTConVPS::MQL5Login

Set the MQL5 account login used for the Sponsored VPS.

C++
    
    
    MTAPIRES  IMTConVPS::MQL5Login(
       LPCWSTR  login    // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.MQL5Login(
       srting   login    // Login
       )

Python
    
    
    MTConVPS.MQL5Login

### Parameters

**login**  
[in] MQL5 account login.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
