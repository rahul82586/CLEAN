[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserUpdateBatchArray

[Previous](UserUpdateBatch.md) | [Next](UserRequest.md)

# IMTAdminAPI::UserUpdateBatchArray

Update multiple client records.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserUpdateBatchArray(
       IMTUser**       users,           // Array of accounts
       const UINT      users_total,     // Number of accounts in the array
       MTAPIRES*       results          // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserUpdateBatchArray(
       CIMTUser[]      users,           // Array of accounts
       MTRetCode[]     retcodes         // Array of results
       )

### Parameters

**users**  
[in] A pointer to the array of accountsIMTUser.

**users_total**  
[in] Number of accounts in the 'users' array.

**results**  
[out] An array with the account updating results. The size of the 'results' array must be at least the size of the 'users' array.

### Return Value

Response code [MT_RET_OK](../../../Return-Codes/Successful-completion.md) indicates that all specified accounts have been updated. Response code [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) indicates that only some of them have been updated. Analyze the 'results' array for further details concerning the execution results. This array will contain the result of updating of each individual account from the 'users' array. The index of a result corresponds to the index of an account in the source array.

### Note

It is only possible to update accounts from applications running on the same trade server on which the accounts are created. The [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) response code will be returned for all other applications.
