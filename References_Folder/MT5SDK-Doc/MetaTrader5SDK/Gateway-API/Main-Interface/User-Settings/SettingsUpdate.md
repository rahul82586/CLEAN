[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [User Settings](../User-Settings.md) / SettingsUpdate

[Previous](SettingsAdd.md) | [Next](SettingsDelete.md)

# IMTGatewayAPI::SettingsUpdate

Change a setting at the specified position.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsUpdate(
       const UINT          pos        // Setting position
       const IMTConParam*  param      // Setting object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsUpdate(
       uint                pos        // Setting position
       CIMTConParam        param      // Setting object
       )

### Parameters

**pos**  
[in] The position of a setting in the settings.dat file, starting with 0.

**param**  
[in]An object of a new setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A setting object must be created using the method [IMTGatewayAPI::FeederParamCreate](../Configuration-Databases/Data-Feeds/FeederParamCreate.md) or [IMTGatewayAPI::GatewayParamCreate](../Configuration-Databases/Gateways/GatewayParamCreate.md). Further, assign a name and a value to the param object using methods [IMTConParam::Name](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Name.md) and [IMTConParamValue](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Value.md) respectively.

# IMTGatewayAPI::SettingsUpdate

Change a setting by its name.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsUpdate(
       const IMTConParam*  param      // Setting object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsUpdate(
       CIMTConParam        param      // Setting object
       )

### Parameters

**param**  
[in]An object of a new setting. The name of the setting to modify and the new value to assign to the setting are specified in the object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A setting object must be created using the method [IMTGatewayAPI::FeederParamCreate](../Configuration-Databases/Data-Feeds/FeederParamCreate.md) or [IMTGatewayAPI::GatewayParamCreate](../Configuration-Databases/Gateways/GatewayParamCreate.md). Further, assign a name and a value to the param object using methods [IMTConParam::Name](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Name.md) and [IMTConParamValue](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Value.md) respectively.
