[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCGroup](../IMTConGroup.md) / IMTConGroup Group

[Previous](IMTConGroup-Clear.md) | [Next](../IMTConSink.md)

# IMTConKYCGroup::Group

Get the group of accounts for which the KYC provider is used.

C++
    
    
    LPCWSTR  IMTConKYCGroup::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConKYCGroup.Group()

### Return Value

If successful, the method returns a pointer to a string with the group name, including its path. Otherwise, NULL is returned.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConKYCGroup](../IMTConGroup.md) object.

You should create a copy of the string if you want to use it after deleting the object (calling the [IMTConKYCGroup::Release](IMTConGroup-Release.md) method of this object).

# IMTConKYCGroup::Group

Set the group of accounts for which the KYC provider is used.

C++
    
    
    MTAPIRES  IMTConKYCGroup::Group(
       LPCWSTR  group      // Group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYCGroup.Group(
       srting   group      // Group
       )

### Parameters

**group**  
[in] Full path to the group or group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" means all groups with the names beginning with 'demo', except for the group demoforex.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
