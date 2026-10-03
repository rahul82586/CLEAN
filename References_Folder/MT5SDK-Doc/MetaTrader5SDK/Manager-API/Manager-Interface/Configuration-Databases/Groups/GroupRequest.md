[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupRequest

[Previous](GroupGet.md) | [Next](GroupRequestArray.md)

# IMTManagerAPI::GroupRequest

Request a group configuration from a server by the name.

C++
    
    
    MTAPIRES  IMTManagerAPI::GroupRequest(
       LPCWSTR       name,      // Group name
       IMTConGroup*  group      // Group configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.GroupRequest(
       string        name,      // Group name
       CIMTConGroup  group      // Group configuration object
       )

Python
    
    
    ManagerAPI.GroupRequest(
       name          # Group name
       )

### Parameters

**name**  
[in] Group name.

**group**  
[out] An object of group configuration. The group object must be first created using theIMTManagerAPI::GroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGroup::Group()](../../../../Configuration-Interfaces/Groups/IMTConGroup/Group.md) value is used as the name.
