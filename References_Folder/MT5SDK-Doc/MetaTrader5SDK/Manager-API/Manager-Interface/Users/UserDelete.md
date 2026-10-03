[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserDelete

[Previous](UserAdd.md) | [Next](UserDeleteBatch.md)

# IMTManagerAPI::UserDelete

Delete a user.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserDelete(
       const UINT64  login      // Login
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserDelete(
       ulong         login      // Login
       )

Python
    
    
    ManagerAPI.UserDelete(
       login         # Login
       )

### Parameters

**login**  
[in] The login of a user.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A client record can be deleted only from the applications that run on the trade server where the record was created. For all other applications the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
