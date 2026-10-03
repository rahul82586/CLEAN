[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTAccountArray::UpdateCopy

Changes a trading account at the specified position of an array by copying the parameters of a passed object of the trading account.

C++
    
    
    MTAPIRES  IMTAccountArray::UpdateCopy(
       const UINT         pos,       // Position
       const IMTAccount*  user       // An object of a trading account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.UpdateCopy(
       uint               pos,       // Position
       CIMTAccount        user       // An object of a trading account
       )

### Parameters

**pos**  
[in] Position of the trading account in an array, starting with 0.

**order**  
[in] Trading account object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the 'account' object into an order object at the specified position of an array.
