[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTAccountArray::Next

Gets an object of a trading account by position.

C++
    
    
    IMTAccount*  IMTAccountArray::Next(
       const UINT  pos      // Position of the trading account
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTAccount  CIMTAccountArray.Next(
       uint        pos      // Position of the trading account
       )

### Parameters

**pos**  
[in] Position of the trading account in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the client position object at the appropriate array position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
