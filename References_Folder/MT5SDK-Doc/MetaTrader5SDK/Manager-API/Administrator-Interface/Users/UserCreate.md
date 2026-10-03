[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserCreate

[Previous](Enumerations.md) | [Next](UserCreateArray.md)

# IMTAdminAPI::UserCreate

Create an object of a client record.

C++
    
    
    IMTUser*  IMTAdminAPI::UserCreate()

.NET
    
    
    CIMTUser  CIMTAdminAPI.UserCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTUser](../../../Database-Interfaces/Users/IMTUser.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTUser::Release](../../../Database-Interfaces/Users/IMTUser/Release.md) method of this object.
