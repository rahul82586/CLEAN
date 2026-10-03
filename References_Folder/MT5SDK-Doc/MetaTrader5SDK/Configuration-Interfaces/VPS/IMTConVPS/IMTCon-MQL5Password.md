[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon MQL5Password

[Previous](IMTCon-MQL5Login.md) | [Next](IMTCon-RuleAdd.md)

# IMTConVPS::MQL5Password

Get the MQL5 account password used for the Sponsored VPS.

C++
    
    
    LPCWSTR  IMTConVPS::MQL5Password()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConVPS.MQL5Password()

Python
    
    
    MTConVPS.MQL5Password

### Return Value

If successful, the method returns a pointer to a string with the password. Otherwise, it returns NULL.

### Note

The method is obsolete and is no longer used.

# IMTConVPS::MQL5Password

Set the MQL5 account password used for the Sponsored VPS.

C++
    
    
    MTAPIRES  IMTConVPS::MQL5Password(
       LPCWSTR  password    // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.MQL5Password(
       srting   password    // Password
       )

Python
    
    
    MTConVPS.MQL5Password

### Parameters

**password**  
[in] MQL5 account password.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
