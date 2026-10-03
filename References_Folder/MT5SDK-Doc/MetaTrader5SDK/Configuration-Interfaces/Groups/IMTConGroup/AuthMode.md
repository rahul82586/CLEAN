[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / AuthMode

[Previous](PermissionsFlags.md) | [Next](AuthOTPMode.md)

# IMTConGroup::AuthMode

Get the authorization mode for accounts in the group.

C++
    
    
    UINT  IMTConGroup::AuthMode()  const

.NET (Gateway/Manager API)
    
    
    EnAuthMode  CIMTConGroup.AuthMode()

Python (Manager API)
    
    
    MTConGroup.AuthMode

### Return Value

A value from [IMTConGroup::EnAuthMode (#enauthmode)](Enumerations.md#enauthmode).

# IMTConGroup::AuthMode

Set the authorization mode for accounts in the group.

C++
    
    
    MTAPIRES  IMTConGroup::AuthMode(
       const UINT  mode      // Authorization mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.AuthMode(
       EnAuthMode  mode      // Authorization mode
       )

Python (Manager API)
    
    
    MTConGroup.AuthMode

### Parameters

**mode**  
[in] TheIMTConGroup::EnAuthModeenumeration is used to pass the authorization mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
