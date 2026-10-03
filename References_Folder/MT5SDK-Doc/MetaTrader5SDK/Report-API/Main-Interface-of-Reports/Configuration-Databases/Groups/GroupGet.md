[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupGet

[Previous](GroupNext.md) | [Next](GroupGetLight.md)

# IMTReportAPI::GroupGet

Get the group configuration by the name.
    
    
    MTAPIRES  IMTReportAPI::GroupGet(
       LPCWSTR       name,      // Name of the configuration
       IMTConGroup*  group      // Group configuration object
       )

### Parameters

**name**  
[in] The name of the configuration.

**group**  
[out] An object of group configuration. The group object must be first created using theIMTReportAPI::GroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGroup::Group()](../../../../Configuration-Interfaces/Groups/IMTConGroup/Group.md) value is used as the name.
