[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSRule](../IMTConRule.md) / IMTConRule Name

[Previous](IMTConRule-Enabled.md) | [Next](IMTConRule-ConditionAdd.md)

# IMTConVPSRule::Name

Get the name of the VPS allocation rule.

C++
    
    
    LPCWSTR  IMTConVPSRule::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConVPSRule.Name()

Python
    
    
    MTConVPSRule.Name

### Return Value

In case of success, the method returns a pointer to a string with the rule name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConVPSRule](../IMTConRule.md) object.

# IMTConVPSRule::Name

Set the name for the VPS allocation rule.

C++
    
    
    MTAPIRES  IMTConVPSRule::Name(
       LPCWSTR  name      // Rule name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSRule.Name(
       string   name      // Rule name
       )

Python
    
    
    MTConVPSRule.Name

### Parameters

**name**  
[in] Rule name.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The name length is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncates to the required length.
