[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / CreateArray

[Previous](Create.md) | [Next](Subscribe.md)

# IMTManagerAPI::ExposureCreateArray

Create an array of objects of exposure records.

C++
    
    
    IMTExposureArray*  IMTManagerAPI::ExposureCreateArray()

.NET
    
    
    CIMTExposureArray  CIMTManagerAPI.ExposureCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTExposureArray](../../../Database-Interfaces/Trade/Assets/IMTExposureArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTExposureArray::Release](../../../Database-Interfaces/Trade/Assets/IMTExposureArray/Release.md) method of this object.
