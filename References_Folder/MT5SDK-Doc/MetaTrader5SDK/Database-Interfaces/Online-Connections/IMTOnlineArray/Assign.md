[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTOnlineArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTOnlineArray::Assign(
       const IMTOnlineArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.Assign(
       CIMTOnlineArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
