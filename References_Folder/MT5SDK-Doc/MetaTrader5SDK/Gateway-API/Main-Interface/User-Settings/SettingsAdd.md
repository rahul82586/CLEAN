[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [User Settings](../User-Settings.md) / SettingsAdd

[Previous](../User-Settings.md) | [Next](SettingsUpdate.md)

# IMTGatewayAPI::SettingsAdd

Add a setting.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsAdd(
       const  IMTConParam*  param      // Setting object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsAdd(
       CIMTConParam         param      // Setting object
       )

### Parameters

**param**  
[in]Setting object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A setting object must be created using the method [IMTGatewayAPI::FeederParamCreate](../Configuration-Databases/Data-Feeds/FeederParamCreate.md) or [IMTGatewayAPI::GatewayParamCreate](../Configuration-Databases/Gateways/GatewayParamCreate.md). Further, assign a name and a value to the param object using methods [IMTConParam::Name](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Name.md) and [IMTConParamValue](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Value.md) respectively.
