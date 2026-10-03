[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSGroup](../IMTConGroup.md) / IMTConGroup Group

[Previous](IMTConGroup-Clear.md) | [Next](IMTConGroup-MinBalance.md)

# IMTConVPSGroup::Group

Get a group of accounts the VPS sponsorship is allowed for.

C++
    
    
    LPCWSTR  IMTConVPSGroup::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConVPSGroup.Group()

Python
    
    
    MTConVPSGroup.Group

### Return Value

If successful, it returns a pointer to a string with the group. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConVPSGroup](../IMTConGroup.md) object.

To use the string after the object removal (call of the [IMTConVPSGroup::Release](IMTConGroup-Release.md) method of this object), a copy of it should be created.

# IMTConVPSGroup::Group

Set a group of accounts the VPS sponsorship is allowed for.

C++
    
    
    MTAPIRES  IMTConVPSGroup::Group(
       LPCWSTR  group      // group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSGroup.Group(
       srting   group      // group
       )

Python
    
    
    MTConVPSGroup.Group

### Parameters

**group**  
[in] Full path to the group or group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
