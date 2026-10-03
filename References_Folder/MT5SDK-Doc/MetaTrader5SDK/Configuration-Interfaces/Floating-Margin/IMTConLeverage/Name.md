[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / Name

[Previous](Clear.md) | [Next](RuleAdd.md)

# IMTConLeverage::Name

Get the name of a floating margin configuration rule.

C++
    
    
    LPCWSTR  IMTConLeverage::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConLeverage.Name()

Python (Manager API)
    
    
    MTConLeverage.Name

### Return Value

If successful, it returns a pointer to a string with the configuration name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid throughout the lifetime of the [IMTConLeverage](../IMTConLeverage.md) object.

# IMTConLeverage::Name

Set a name for the floating margin configuration.

C++
    
    
    MTAPIRES  IMTConLeverage::Name(
       LPCWSTR  name      // Configuration name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverage.Name(
       srting   name      // Configuration name
       )

Python (Manager API)
    
    
    MTConLeverage.Name

### Parameters

**name**  
[in] Configuration name.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name length is limited to 64 characters (including the end-of-string character). If a longer string is assigned, it will be truncated to this length.
