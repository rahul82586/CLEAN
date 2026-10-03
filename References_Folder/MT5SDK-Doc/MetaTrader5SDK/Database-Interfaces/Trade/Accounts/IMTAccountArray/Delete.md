[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTAccountArray::Delete

Deletes an object of a trading account by position.

C++
    
    
    MTAPIRES  IMTAccountArray::Delete(
       const UINT  pos      // Position of the trading account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.Delete(
       uint        pos      // Position of the trading account
       )

### Parameters

**pos**  
[in] Position of the trading account in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTAccount::Release](../IMTAccount/Release.md) method.
