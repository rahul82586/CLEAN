[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / Name

[Previous](Clear.md) | [Next](Description.md)

# IMTConLeverageRule::Name

Get the name of a rule in a floating margin configuration.

C++
    
    
    LPCWSTR  IMTConLeverageRule::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConLeverageRule.Name()

Python (Manager API)
    
    
    MTConLeverageRule.Name

### Return Value

If successful, the method returns a pointer to a string with the rule name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid throughout the lifetime of the [IMTConLeverageRule](../IMTConLeverageRule.md) object.

# IMTConLeverageRule::Name

Set the name of a rule in a floating margin configuration.

C++
    
    
    MTAPIRES  IMTConLeverageRule::Name(
       LPCWSTR  name      // Rule name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageRule.Name(
       srting   name      // Rule name
       )

Python (Manager API)
    
    
    MTConLeverageRule.Name

### Parameters

**name**  
[in] Rule name.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name length is limited to 64 characters (including the end-of-string character). If a longer string is assigned, it will be truncated to this length.
