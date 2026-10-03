[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserUpdate

[Previous](UserDeleteBatch.md) | [Next](UserUpdateBatch.md)

# IMTAdminAPI::UserUpdate

Update a user.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserUpdate(
       IMTUser*  user      // An object of the user
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserUpdate(
       CIMTUser  user      // An object of the user
       )

Python
    
    
    AdminAPI.UserUpdate(
       user      # An object of the user
       )

### Parameters

**user**  
[in] An object of the user.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A client record can be updated only from the applications that run on the trade server where the record was created. For all other applications the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
