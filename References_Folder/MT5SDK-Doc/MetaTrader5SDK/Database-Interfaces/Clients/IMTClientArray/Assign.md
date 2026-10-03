[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTClientArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTClientArray::Assign(
       const IMTClientArray*  array     // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.Assign(
       CIMTClientArray        array     // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
