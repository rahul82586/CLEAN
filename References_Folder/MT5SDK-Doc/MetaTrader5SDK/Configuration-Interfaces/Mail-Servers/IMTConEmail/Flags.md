[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Flags

[Previous](Password.md) | [Next](../IMTConEmailSink.md)

# IMTConEmail::Flags

Get additional mail server settings.

C++
    
    
    UINT64  IMTConEmail::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnFlags  CIMTConEmail.Flags()

Python
    
    
    MTConEmail.Flags

### Return Value

Additional settings as the values of the [IMTConEmail::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

# IMTConEmail::Mode

Set additional mail server settings.

C++
    
    
    MTAPIRES  IMTConEmail::Flags(
       const UINT64  flags   // Mail server settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.Flags(
       EnFlags       flags   // Mail server settings
       )

Python
    
    
    MTConEmail.Flags

### Parameters

**flags**  
[in] Additional settings as the values of theIMTConEmail::EnFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
