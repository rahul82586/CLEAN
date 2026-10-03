[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MarginFloatingLeverage

[Previous](MarginFlags.md) | [Next](DemoLeverage.md)

# IMTConGroup::MarginFloatingLeverage

Get the [floating margin](../../Floating-Margin/IMTConLeverage.md) profile applied to the group.

C++
    
    
    LPCWSTR  IMTConGroup::MarginFloatingLeverage()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.MarginFloatingLeverage()

Python (Manager API)
    
    
    MTConGroup.MarginFloatingLeverage

### Return Value

If successful, a pointer to a string with the profile name is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid throughout the lifetime of the [IMTConGroup](../IMTConGroup.md) object.

# IMTConGroup::MarginFloatingLeverage

Set a [floating margin](../../Floating-Margin/IMTConLeverage.md) profile for the group.

C++
    
    
    MTAPIRES  IMTConGroup::MarginFloatingLeverage(
       LPCWSTR  name      // Profile name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MarginFloatingLeverage(
       string   name      // Profile name
       )

Python (Manager API)
    
    
    MTConGroup.MarginFloatingLeverage

### Parameters

**name**  
[in] Name of the floating margin profile. Corresponds toIMTConLeverage::Name.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name length is limited to 64 characters (including the end-of-string character). If a longer string is assigned, it will be truncated to this length.
