[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserCreateAccount

[Previous](UserCreate.md) | [Next](UserSubscribe.md)

# IMTServerAPI::UserCreateAccount

Create an object of a client's trading account.
    
    
    IMTAccount*  IMTServerAPI::UserCreateAccount()

### Return Value

It returns a pointer to the created object that implements the [IMTAccount](../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTAccount::Release](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Release.md) method of this object.
