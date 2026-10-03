[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupNext

[Previous](GroupTotal.md) | [Next](GroupGet.md)

# IMTManagerAPI::GroupNext

Get the group configuration by the index.

C++
    
    
    MTAPIRES  IMTManagerAPI::GroupNext(
       const UINT    pos,       // Position of the configuration
       IMTConGroup*  group      // Group configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.GroupNext(
       uint          pos,       // Position of the configuration
       CIMTConGroup  group      // Group configuration object
       )

Python
    
    
    ManagerAPI.GroupNext(
       pos           # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**group**  
[out] An object of group configuration. The group object must be first created using theIMTManagerAPI::GroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a group with a specified index to the group object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_GROUPS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
