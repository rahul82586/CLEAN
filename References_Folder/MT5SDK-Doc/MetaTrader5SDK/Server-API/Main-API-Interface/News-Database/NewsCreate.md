[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [News Database](../News-Database.md) / NewsCreate

[Previous](../News-Database.md) | [Next](NewsSubscribe.md)

# IMTServerAPI::NewsCreate

Create an object of a news item.
    
    
    IMTNews*  IMTServerAPI::NewsCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTNews](../../../Database-Interfaces/News-Database/IMTNews.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTNews::Release](../../../Database-Interfaces/News-Database/IMTNews/Release.md) method of this object.
