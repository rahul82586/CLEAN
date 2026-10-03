[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupGet

[Previous](GroupNext.md) | [Next](../Floating-Margin.md)

# IMTAdminAPI::GroupGet

Get the group configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::GroupGet(
       LPCWSTR       name,      // Name of the configuration
       IMTConGroup*  group      // Group configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GroupGet(
       string        name,      // Name of the configuration
       CIMTConGroup  group      // Group configuration object
       )

Python
    
    
    AdminAPI.GroupGet(
       name          # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**group**  
[out] An object of group configuration. The group object must be first created using theIMTAdminAPI::GroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGroup::Group()](../../../../Configuration-Interfaces/Groups/IMTConGroup/Group.md) value is used as the name.
