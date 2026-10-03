[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTDealArray::Next

Get an object of a deal by its position.

C++
    
    
    IMTDeal*  IMTDealArray::Next(
       const UINT  index      // Position of a deal
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTDeal  CIMTDealArray.Next(
       uint        index      // Position of a deal
       )

### Parameters

**index**  
[in] Position of a deal in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the object of a deal at the specified position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
