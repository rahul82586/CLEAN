[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [User Settings](../User-Settings.md) / SettingsGet

[Previous](SettingsNext.md) | [Next](../../Event-Interface.md)

# IMTGatewayAPI::SettingsGet

Get a setting by its name.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsGet(
       LPCWSTR       name,      // Setting name
       IMTConParam*  param      // Setting object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsGet(
       string        name,      // Setting name
       CIMTConParam  param      // Setting object
       )

### Parameters

**name**  
[in] The name of the setting.

**param**  
[out]An object of the parameter setting. The param object must first be created using the methodIMTGatewayAPI::FeederParamCreateorIMTGatewayAPI::GatewayParamCreate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method returns the first found setting with the specified name.
