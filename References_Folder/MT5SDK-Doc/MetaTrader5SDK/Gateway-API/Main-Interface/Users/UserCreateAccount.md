[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserCreateAccount

[Previous](UserCreate.md) | [Next](UserSubscribe.md)

# IMTGatewayAPI::UserCreateAccount

Create an object of a client's trading account.

C++
    
    
    IMTAccount*  IMTGatewayAPI::UserCreateAccount()

.NET
    
    
    CIMTAccount  CIMTGatewayAPI.UserCreateAccount()

### Return Value

It returns a pointer to the created object that implements the [IMTAccount](../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTAccount::Release](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Release.md) method of this object.
