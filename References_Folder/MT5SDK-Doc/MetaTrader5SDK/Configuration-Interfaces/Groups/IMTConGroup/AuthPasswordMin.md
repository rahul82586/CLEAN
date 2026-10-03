[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / AuthPasswordMin

[Previous](AuthOTPMode.md) | [Next](Company.md)

# IMTConGroup::AuthPasswordMin

Get the minimum password length for accounts in the group.

C++
    
    
    UINT  IMTConGroup::AuthPasswordMin()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroup.AuthPasswordMin()

Python (Manager API)
    
    
    MTConGroup.AuthPasswordMin

### Return Value

Minimum password length that can be specified for an account in this group.

# IMTConGroup::AuthPasswordMin

Set the minimum password length for accounts in the group.

C++
    
    
    MTAPIRES  IMTConGroup::AuthPasswordMin(
       const UINT  mode      // Minimum password length
       )

.NET (Gateway/Manager API)
    
    
    MRetCode  CIMTConGroup.AuthPasswordMin(
       uint        mode      // Minimum password length
       )

Python (Manager API)
    
    
    MTConGroup.AuthPasswordMin

### Parameters

**mode**  
[in] Minimum password length.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The minimum possible password length is 8 characters and the maximum is 16 characters.
