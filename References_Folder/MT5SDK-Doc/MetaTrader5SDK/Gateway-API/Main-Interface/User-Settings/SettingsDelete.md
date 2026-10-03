[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [User Settings](../User-Settings.md) / SettingsDelete

[Previous](SettingsUpdate.md) | [Next](SettingsClear.md)

# IMTGatewayAPI::SettingsDelete

Delete a setting by its position.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsDelete(
       const UINT    pos        // Setting position
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsDelete(
       uint          pos        // Setting position
       )

### Parameters

**pos**  
[in] The position of a setting in the settings.dat file, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

# IMTGatewayAPI::SettingsDelete

Delete a setting by its name.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsDelete(
       LPCWSTR       name       // Setting name
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsDelete(
       string        name       // Setting name
       )

### Parameters

**name**  
[in] The name of the setting you want to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method deletes the first found setting with the specified name.
