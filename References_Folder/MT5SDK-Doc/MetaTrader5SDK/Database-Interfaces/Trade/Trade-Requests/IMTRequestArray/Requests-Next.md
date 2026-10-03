[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Next

[Previous](Requests-Total.md) | [Next](Requests-Sort.md)

# IMTRequestArray::Next

Get a trade request by its index.

C++
    
    
    IMTRequest*  IMTRequestArray::Next(
       const UINT  index      // Position of a trade request
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTRequest  CIMTRequestArray.Next(
       uint        index      // Position of a trade request
       )

### Parameters

**index**  
[in] Position of a trade request in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the object of a request with the specified index in the array. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
