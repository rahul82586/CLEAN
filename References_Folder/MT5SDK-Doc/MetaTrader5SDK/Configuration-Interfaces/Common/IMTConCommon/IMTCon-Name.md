[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon Name

[Previous](IMTCon-Clear.md) | [Next](IMTCon-NameFull.md)

# IMTConCommon::Name

Get the name of the platform.

C++
    
    
    LPCWSTR  IMTConCommon::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.Name()

Python (Manager API)
    
    
    MTConCommon.Name

### Return Value

If successful, it returns a pointer to a string with the name of the . Otherwise, it returns NULL.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConCommon](../IMTCon.md) object.

# IMTConCommon::Name

Set the platform name.

C++
    
    
    MTAPIRES  IMTConCommon::Name(
       LPCWSTR  name      // Platform name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommon.Name(
       string   name      // Platform name
       )

Python (Manager API)
    
    
    MTConCommon.Name

### Parameters

**name**  
[in] The name of the platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
