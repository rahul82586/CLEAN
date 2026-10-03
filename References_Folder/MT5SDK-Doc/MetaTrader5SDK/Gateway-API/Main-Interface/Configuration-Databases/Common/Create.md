[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Create

[Previous](../Common.md) | [Next](Subscribe.md)

# IMTGatewayAPI::CommonCreate

Create a common platform configuration object.

C++
    
    
    IMTConCommon*  IMTGatewayAPI::CommonCreate()

.NET
    
    
    CIMTConCommon  CIMTGatewayAPI.CommonCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConCommon](../../../../Configuration-Interfaces/Common/IMTCon.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConCommon::Release](../../../../Configuration-Interfaces/Common/IMTConCommon/IMTCon-Release.md) method of this object.
