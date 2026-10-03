[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCreateAccountArray

[Previous](UserCreateAccount.md) | [Next](UserSubscribe.md)

# IMTManagerAPI::UserCreateAccountArray

Create an object of an array trading accounts.

C++
    
    
    IMTAccountArray*  IMTManagerAPI::UserCreateAccountArray()

.NET
    
    
    CIMTAccountArray  CIMTManagerAPI.UserCreateAccountArray()

### Return Value

It returns a pointer to the created object that implements the [IMTAccountArray](../../../Database-Interfaces/Trade/Accounts/IMTAccountArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTAccountArray::Release](../../../Database-Interfaces/Trade/Accounts/IMTAccountArray/Release.md) method of this object.
