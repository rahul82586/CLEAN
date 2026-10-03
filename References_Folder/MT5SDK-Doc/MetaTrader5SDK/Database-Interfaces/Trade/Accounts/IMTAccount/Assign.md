[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTAccount::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTAccount::Assign(
       const IMTAccount*  user      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Assign(
       CIMTAccount        user      // Source object
       )

### Parameters

**user**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
