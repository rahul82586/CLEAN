[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupGet

[Previous](GroupNext.md) | [Next](GroupRequest.md)

# IMTManagerAPI::GroupGet

Get the group configuration by the name.

C++
    
    
    MTAPIRES  IMTManagerAPI::GroupGet(
       LPCWSTR       name,      // Name of the configuration
       IMTConGroup*  group      // Group configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.GroupGet(
       string        name,      // Name of the configuration
       CIMTConGroup  group      // Group configuration object
       )

Python
    
    
    ManagerAPI.GroupGet(
       name          # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration.TheIMTConGroup::Group()value is used as the name..

**group**  
[out] An object of group configuration. The group object must be first created using theIMTManagerAPI::GroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_GROUPS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
