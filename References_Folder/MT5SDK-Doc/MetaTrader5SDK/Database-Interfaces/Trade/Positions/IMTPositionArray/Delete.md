[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTPositionArray::Delete

Delete the object of a trade position by the index.

C++
    
    
    MTAPIRES  IMTPositionArray::Delete(
       const UINT  pos      // Position index
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.Delete(
       uint        pos      // Position index
       )

### Parameters

**pos**  
[in] The index of a trade position in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by calling the [IMTPosition::Release](../IMTPosition/Release.md) method.
