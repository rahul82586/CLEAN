[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederTranslateCreate

[Previous](FeederParamCreate.md) | [Next](../Gateways.md)

# IMTGatewayAPI::FeederTranslateCreate

Create an object of setup of converting the information transmitted from a data feed.

C++
    
    
    IMTConFeederTranslate*  IMTGatewayAPI::FeederTranslateCreate()

.NET
    
    
    CIMTConFeederTranslate  CIMTGatewayAPI.FeederTranslateCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFeederTranslate](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederTranslate.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConFeederTranslate::Release](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederTranslate/Release.md) method of this object.
