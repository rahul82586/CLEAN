[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederParamCreate

[Previous](FeederCreate.md) | [Next](FeederTranslateCreate.md)

# IMTGatewayAPI::FeederParamCreate

Create an object of the parameter of the data feeds.

C++
    
    
    IMTConParam*  IMTGatewayAPI::FeederParamCreate()

.NET
    
    
    CIMTConParam  CIMTGatewayAPI.FeederParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParam](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParam::Release](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Release.md) method of this object.
