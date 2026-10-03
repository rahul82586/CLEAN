[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / AuthOTPMode

[Previous](AuthMode.md) | [Next](AuthPasswordMin.md)

# IMTConGroup::AuthOTPMode

Gets authentication mode using one-time passwords.

C++
    
    
    UINT  IMTConGroup::AuthOTPMode()  const

.NET (Gateway/Manager API)
    
    
    EnAuthOTPMode  CIMTConGroup.AuthOTPMode()

Python (Manager API)
    
    
    MTConGroup.AuthOTPMode

### Return Value

A value from [IMTConGroup::EnAuthOTPMode (#enauthotpmode)](Enumerations.md#enauthotpmode).

# IMTConGroup::AuthOTPMode

Sets authentication mode using one-time passwords.

C++
    
    
    MTAPIRES  IMTConGroup::AuthOTPMode(
       const UINT     mode   // OTP authentication mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.AuthOTPMode(
       EnAuthOTPMode  mode   // OTP authentication mode
       )

Python (Manager API)
    
    
    MTConGroup.AuthOTPMode

### Parameters

**mode**  
[in] TheIMTConGroup::EnAuthOTPModeenumeration is used for setting the OTP authentication mode..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
