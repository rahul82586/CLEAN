[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderBackupRestore

[Previous](OrderBackupRequestHistory.md) | [Next](OrderReopen.md)

# IMTAdminAPI::OrderBackupRestore

Restore an order from a backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderBackupRestore(
       IMTOrder*  order      // An order object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderBackupRestore(
       CIMTOrder  order      // An order object
       )

Python
    
    
    MTAdminAPI.OrderBackupRestore(
       MTOrder    order      # An order object
       )

### Parameters

**order**  
[in] An object of the order to restore.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Restored orders are not deleted from the backup copy.
