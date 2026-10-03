[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [User Settings](../User-Settings.md) / SettingsClear

[Previous](SettingsDelete.md) | [Next](SettingsTotal.md)

# IMTGatewayAPI::SettingsClear

Delete all settings.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SettingsClear()

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SettingsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method deletes all settings and the settings.dat file.
