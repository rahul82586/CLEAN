[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTAccountArray::Detach

Detaches an object of a trading account from an array.

C++
    
    
    IMTAccount*  IMTAccountArray::Detach(
       const UINT  pos      // Position of the trading account
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTAccount  CIMTAccountArray.Detach(
       uint        pos      // Position of the trading account
       )

### Parameters

**pos**  
[in] Position of the trading account in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of the trading account.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
