[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserDeleteBatch

[Previous](UserDelete.md) | [Next](UserUpdate.md)

# IMTManagerAPI::UserDeleteBatch

Delete multiple accounts.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserDeleteBatch(
       const UINT64*      logins,       // Logins
       const UINT         logins_total, // Number of logins
       MTAPIRES*          results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserDeleteBatch(
       ulong[]            logins,       // Logins
       MTRetCode[]        res           // Array of results
       )

Python
    
    
    ManagerAPI.UserDeleteBatch(
       logins,            # Logins
       res                # Array of results
       )

### Parameters

**logins**  
[in] An array of account logins which should be deleted.

**logins_total**  
[in] Number of logins in the 'logins' array.

**results**  
[out] An array with account deleting results. The size of the 'results' array must be at least the size of the 'logins' array.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified accounts have been deleted. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the accounts have been deleted. Analyze the 'results' array for further details concerning the execution results. This array will contain the result of deleting of each individual account from the 'logins' array. The index of a result corresponds to the index of an account in the source array.

### Note

It is only possible to delete accounts from applications running on the same trade server on which the accounts are created. The [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) response code will be returned for all other applications.
