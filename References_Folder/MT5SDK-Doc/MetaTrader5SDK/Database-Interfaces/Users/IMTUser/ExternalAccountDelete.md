[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / ExternalAccountDelete

[Previous](ExternalAccountUpdate.md) | [Next](ExternalAccountClear.md)

# IMTUser::ExternalAccountDelete

Deletes the number of a trading account in the external trading system by position.

C++
    
    
    MTAPIRES  IMTUser::ExternalAccountDelete(
       const UINT  pos      // Position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ExternalAccountDelete(
       uint        pos      // Position
       )

### Parameters

**pos**  
[in] Account position starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
