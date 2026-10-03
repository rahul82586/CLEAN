[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTOrderArray::Next

Get an object of a trade order by its position.

C++
    
    
    IMTOrder*  IMTOrderArray::Next(
       const UINT  pos      // Position of an order
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTOrder  CIMTOrderArray.Next(
       uint        pos      // Position of an order
       )

### Parameters

**pos**  
[in] Position of an order in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the object of a trade order at the specified position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
