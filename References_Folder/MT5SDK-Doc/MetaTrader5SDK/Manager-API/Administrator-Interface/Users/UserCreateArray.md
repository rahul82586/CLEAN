[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserCreateArray

[Previous](UserCreate.md) | [Next](UserAdd.md)

# IMTAdminAPI::UserCreateArray

Create an object of an array of client records.

C++
    
    
    IMTUserArray*  IMTAdminAPI::UserCreateArray()

.NET
    
    
    CIMTUserArray  CIMTAdminAPI.UserCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTUserArray](../../../Database-Interfaces/Users/IMTUserArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTUserArray::Release](../../../Database-Interfaces/Users/IMTUserArray/Release.md) method of this object.
