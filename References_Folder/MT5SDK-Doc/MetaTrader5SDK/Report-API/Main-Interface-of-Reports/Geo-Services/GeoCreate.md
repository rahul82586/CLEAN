[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Geo Services](../Geo-Services.md) / GeoCreate

[Previous](../Geo-Services.md) | [Next](GeoResolve.md)

# IMTReportAPI::GeoCreate

Create an IP address description object.
    
    
    IMTGeo*  IMTReportAPI::GeoCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTGeo](../../../Database-Interfaces/Geo-Services/IMTGeo.md) interface. NULL is returned in case of failure.

### Note

The created object should be destroyed by calling the [IMTGeo::Release](../../../Database-Interfaces/Geo-Services/IMTGeo/Release.md) method of this object.
