[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTPositionArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTPositionArray::Assign(
       const IMTPositionArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.Assign(
       CIMTPositionArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
