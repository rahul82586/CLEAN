[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCreateAccount

[Previous](UserCreateArray.md) | [Next](UserCreateAccountArray.md)

# IMTManagerAPI::UserCreateAccount

Create an object of a client's trading account.

C++
    
    
    IMTAccount*  IMTManagerAPI::UserCreateAccount()

.NET
    
    
    CIMTAccount  CIMTManagerAPI.UserCreateAccount()

### Return Value

It returns a pointer to the created object that implements the [IMTAccount](../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTAccount::Release](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Release.md) method of this object.
