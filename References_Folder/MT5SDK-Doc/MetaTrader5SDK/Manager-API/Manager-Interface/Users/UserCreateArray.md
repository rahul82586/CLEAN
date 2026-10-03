[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCreateArray

[Previous](UserCreate.md) | [Next](UserCreateAccount.md)

# IMTManagerAPI::UserCreateArray

Create an object of an array of client records.

C++
    
    
    IMTUserArray*  IMTManagerAPI::UserCreateArray()

.NET
    
    
    CIMTUserArray  CIMTManagerAPI.UserCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTUserArray](../../../Database-Interfaces/Users/IMTUserArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTUserArray::Release](../../../Database-Interfaces/Users/IMTUserArray/Release.md) method of this object.
