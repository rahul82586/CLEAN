[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserRestoreBatchArray

[Previous](UserRestoreBatch.md) | [Next](UserBalanceCheck.md)

# IMTAdminAPI::UserRestoreBatchArray

Restore multiple accounts from an archive or backup database.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserRestoreBatchArray(
       IMTUser**       users,        // Array of accounts
       const UINT      users_total,  // Number of accounts in the array
       MTAPIRES*       results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserRestoreBatchArray(
       CIMTUser[]      users,        // Array of accounts
       MTRetCode[]     res           // Array of results
       )

### Parameters

**users**  
[in] A pointer to the array of accountsIMTUser.

**users_total**  
[in] Number of accounts in the 'users' array.

**results**  
[out] An array with account recovery results. The size of the 'results' array must be at least the size of the 'logins' array.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified accounts have been restored. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only part of the accounts gave been restored. Analyze the 'results' array for further details concerning the execution results. This array will contain the result of restoring of each individual account from the 'logins' array. The index of a result corresponds to the index of an account in the source array.

### Note

Restored users are not deleted from the archive.
