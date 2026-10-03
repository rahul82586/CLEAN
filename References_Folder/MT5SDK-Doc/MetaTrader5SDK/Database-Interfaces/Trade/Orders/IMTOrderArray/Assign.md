[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTOrderArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTOrderArray::Assign(
       const IMTOrderArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.Assign(
       CIMTOrderArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
