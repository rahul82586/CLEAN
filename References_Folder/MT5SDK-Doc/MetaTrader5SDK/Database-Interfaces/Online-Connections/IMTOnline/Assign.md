[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnline](../IMTOnline.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTOnline::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTOnline::Assign(
       const IMTOnline*  online      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnline.Assign(
       CIMTOnline        online      // Source object
       )

### Parameters

**online**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
