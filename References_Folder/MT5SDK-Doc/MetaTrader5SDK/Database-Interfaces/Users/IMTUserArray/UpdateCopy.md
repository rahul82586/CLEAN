[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTUserArray::UpdateCopy

Change a client record at the specified position of an array by copying the parameters of a passed object of a client record.

C++
    
    
    MTAPIRES  IMTUserArray::UpdateCopy(
       const UINT        pos,       // Position
       const IMTUser*    user       // An object of a client record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.UpdateCopy(
       uint              pos,       // Position
       CIMTUser          user       // An object of a client record
       )

### Parameters

**pos**  
[in] Position of a client record in an array, starting with 0.

**order**  
[in] An object of the client record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the 'user' object into an order object at the specified position of an array.
