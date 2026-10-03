[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserCreate

[Previous](../Users.md) | [Next](UserCreateAccount.md)

# IMTGatewayAPI::UserCreate

Create an object of a client record.

C++
    
    
    IMTUser*  IMTGatewayAPI::UserCreate()

.NET
    
    
    CIMTUser  CIMTGatewayAPI.UserCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTUser](../../../Database-Interfaces/Users/IMTUser.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTUser::Release](../../../Database-Interfaces/Users/IMTUser/Release.md) method of this object.
