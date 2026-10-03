[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConGroupArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConGroupArray::Assign(
       const IMTConGroupArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupArray.Assign(
       CIMTConGroupArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
