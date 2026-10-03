[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / Create

[Previous](../Exposure.md) | [Next](CreateArray.md)

# IMTManagerAPI::ExposureCreate

Create an object of an exposure record.

C++
    
    
    IMTExposure*  IMTManagerAPI::ExposureCreate()

.NET
    
    
    CIMTExposure  CIMTManagerAPI.ExposureCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTExposure](../../../Database-Interfaces/Trade/Assets/IMTExposure.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTExposure::Release](../../../Database-Interfaces/Trade/Assets/IMTExposure/Release.md) method of this object.
