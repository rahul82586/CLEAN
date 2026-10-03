[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Create

[Previous](../Time.md) | [Next](Subscribe.md)

# IMTManagerAPI::TimeCreate

Create an object of the time configuration.

C++
    
    
    IMTConTime*  IMTManagerAPI::TimeCreate()

.NET
    
    
    CIMTConTime  CIMTManagerAPI.TimeCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConTime](../../../../Configuration-Interfaces/Time/IMTCon.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConTime::Release](../../../../Configuration-Interfaces/Time/IMTConTime/IMTCon-Release.md) method of this object.
