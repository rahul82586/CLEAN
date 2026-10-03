[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCreate

[Previous](Enumerations.md) | [Next](UserCreateArray.md)

# IMTManagerAPI::UserCreate

Create an object of a client record.

C++
    
    
    IMTUser*  IMTManagerAPI::UserCreate()

.NET
    
    
    CIMTUser  CIMTManagerAPI.UserCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTUser](../../../Database-Interfaces/Users/IMTUser.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTUser::Release](../../../Database-Interfaces/Users/IMTUser/Release.md) method of this object.
