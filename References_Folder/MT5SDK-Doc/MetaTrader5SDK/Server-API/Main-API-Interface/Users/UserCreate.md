[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserCreate

[Previous](../Users.md) | [Next](UserCreateAccount.md)

# IMTServerAPI::UserCreate

Create an object of a client record.
    
    
    IMTUser*  IMTServerAPI::UserCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTUser](../../../Database-Interfaces/Users/IMTUser.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTUser::Release](../../../Database-Interfaces/Users/IMTUser/Release.md) method of this object.
