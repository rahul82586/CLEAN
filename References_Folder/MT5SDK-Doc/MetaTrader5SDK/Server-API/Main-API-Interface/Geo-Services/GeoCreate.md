[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Geo Services](../Geo-Services.md) / GeoCreate

[Previous](../Geo-Services.md) | [Next](GeoResolve.md)

# IMTServerAPI::GeoCreate

Create an IP address description object.
    
    
    IMTGeo*  IMTServerAPI::GeoCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTGeo](../../../Database-Interfaces/Geo-Services/IMTGeo.md) interface. NULL is returned in case of failure.

### Note

The created object should be destroyed by calling the [IMTGeo::Release](../../../Database-Interfaces/Geo-Services/IMTGeo/Release.md) method of this object.
