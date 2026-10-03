[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConEmail::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConEmail::Assign(
       const IMTConEmail*   email      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.Assign(
       CIMTConEmail         email      // Source object
       )

### Parameters

**email**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
