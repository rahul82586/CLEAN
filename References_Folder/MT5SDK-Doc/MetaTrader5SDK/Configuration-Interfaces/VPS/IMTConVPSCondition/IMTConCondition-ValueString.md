[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueString

[Previous](IMTConCondition-ValueDouble.md) | [Next](IMTConCondition-ValueColor.md)

# IMTConVPSCondition::ValueString

Get the value of a condition of the string type.

C++
    
    
    LPCWSTR  IMTConVPSCondition::ValueString()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConVPSCondition.ValueString()

Python
    
    
    MTConVPSCondition.ValueString

### Return Value

If successful, it returns a pointer to the string with the value. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConVPSCondition](../IMTConCondition.md) object.

To use the string after the object removal (after the call of the [IMTConVPSCondition::Release](IMTConCondition-Release.md) method of this object), you should create the string copy.

# IMTConVPSCondition::ValueString

Set the value of a condition of the string type.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueString(
       LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueString(
       string   value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueString

### Parameters

**value**  
[in] A value of the string type.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The value length is limited to 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncates to the required length.
