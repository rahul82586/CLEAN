[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [User Settings](../User-Settings.md) / SettingsNext

[Previous](SettingsTotal.md) | [Next](SettingsGet.md)

# IMTGatewayAPI::SettingsNext

Get a setting by its position.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsNext(
       const UINT    pos,       // Setting position
       IMTConParam*  param      // Setting object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsNext(
       uint          pos,       // Setting position
       CIMTConParam  param      // Setting object
       )

### Parameters

**pos**  
[in] The position of a setting in the settings.dat file, starting with 0.

**param**  
[out]An object of the setting. The param object must first be created using the methodIMTGatewayAPI::FeederParamCreateorIMTGatewayAPI::GatewayParamCreate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
