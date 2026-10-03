[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTOrderArray::Delete

Delete an object of a trade order by its position.

C++
    
    
    MTAPIRES  IMTOrderArray::Delete(
       const UINT  pos      // Position of an order
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.Delete(
       uint        pos      // Position of an order
       )

### Parameters

**pos**  
[in] Position of an order in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTOrder::Release](../IMTOrder/Release.md) method.
