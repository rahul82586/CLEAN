[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTUserArray::Delete

Delete a client record object by its position.

C++
    
    
    MTAPIRES  IMTUserArray::Delete(
       const UINT  pos      // The position of a client record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.Delete(
       uint        pos      // The position of a client record
       )

### Parameters

**pos**  
[in] Position of a client record in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTUser::Release](../IMTUser/Release.md) method.
