[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueString

[Previous](ValueDouble.md) | [Next](ValueColor.md)

# IMTConCondition::ValueString

Get the value of a condition of the string type.

C++
    
    
    LPCWSTR  IMTConCondition::ValueString()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCondition.ValueString()

Python (Manager API)
    
    
    MTConCondition.ValueString

### Return Value

If successful, it returns a pointer to the string with the value. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConCondition](../IMTConCondition.md) object.

To use the line after the object removal (call of the [IMTConCondition::Release](Release.md) method of this object), a copy of it should be created.

# IMTConCondition::ValueString

Set the value of a condition of the string type.

C++
    
    
    MTAPIRES  IMTConCondition::ValueString(
       LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueString(
       string   value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueString

### Parameters

**value**  
[in] A value of the string type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum value length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
