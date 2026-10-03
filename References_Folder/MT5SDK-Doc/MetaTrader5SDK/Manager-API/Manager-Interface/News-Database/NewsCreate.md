[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [News Database](../News-Database.md) / NewsCreate

[Previous](../News-Database.md) | [Next](NewsSubscribe.md)

# IMTManagerAPI::NewsCreate

Create an object of a news item.

C++
    
    
    IMTNews*  IMTManagerAPI::NewsCreate()

.NET
    
    
    CIMTNews  CIMTManagerAPI.NewsCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTNews](../../../Database-Interfaces/News-Database/IMTNews.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTManagerAPI::Release](../../../Database-Interfaces/News-Database/IMTNews/Release.md) method of this object.
