[🏠 Document Start](../README.md) / [Return Codes](README.md) / User management

[Previous](Configuration-Management.md) | [Next](Trade-management.md)

# User management

This group of codes is returned by the server when working with a database of [users](../Database-Interfaces/Users.md):

Constant | Value | Description  
MT_RET_USR_LAST_ADMIN | 3001 | The last administrator account has been deleted.  
MT_RET_USR_LOGIN_EXHAUSTED | 3002 | The range of logins has been exhausted.  
MT_RET_USR_LOGIN_PROHIBITED | 3003 | The login is reserved on another server.  
MT_RET_USR_LOGIN_EXIST | 3004 | The account already exists.  
MT_RET_USR_SUICIDE | 3005 | An attempt of self-deletion.  
MT_RET_USR_INVALID_PASSWORD | 3006 | Incorrect account password.  
MT_RET_USR_LIMIT_REACHED | 3007 | Reached the limit on the number of users.  
MT_RET_USR_HAS_TRADES | 3008 | The accounts has open positions.  
MT_RET_USR_DIFFERENT_SERVERS | 3009 | An attempt to move an account to another server.  
MT_RET_USR_DIFFERENT_CURRENCY | 3010 | An attempt to move an accounts to a group with a different deposit currency.  
MT_RET_USR_IMPORT_BALANCE | 3011 | Failed to import account balance.  
MT_RET_USR_IMPORT_GROUP | 3012 | The account is imported with the wrong group.  
MT_RET_USR_ACCOUNT_EXIST | 3013 | [A trading account in an external system](../Database-Interfaces/Users/IMTUser/ExternalAccountAdd.md) already exists for a specified login.  
MT_RET_USR_IMPORT_ACCOUNT | 3014 | Failed to [import](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt) account's trading data.  
MT_RET_USR_IMPORT_POSITIONS | 3015 | Failed to import account's trading positions.  
MT_RET_USR_IMPORT_ORDERS | 3016 | Failed to import account's open orders.  
MT_RET_USR_IMPORT_DEALS | 3017 | Failed to import account's deal history.  
MT_RET_USR_IMPORT_HISTORY | 3018 | Failed to import account's order history.  
MT_RET_USR_API_LIMIT_REACHED | 3019 | Reached the limit on the number of users with the permission to connect via the API ([IMTUser::USER_RIGHT_API_ENABLED (#enusersrights)](../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)). The current limit is 100 users.
