[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealBackupRestore

[Previous](DealBackupRequest.md) | [Next](DealPerform.md)

# IMTAdminAPI::DealBackupRestore

Recover a deal from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealBackupRestore(
       IMTDeal*  deal      // A deal to recover
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealBackupRestore(
       CIMTDeal  deal      // A deal to recover
       )

Python
    
    
    AdminAPI.DealBackupRestore(
       MTDeal    deal      # A deal to recover
       )

### Parameters

**deal**  
[in] An object of the deal to recover.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Recovered deals are not deleted from the backup copy.
