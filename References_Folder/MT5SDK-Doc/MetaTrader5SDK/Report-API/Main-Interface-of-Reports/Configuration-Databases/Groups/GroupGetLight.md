[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupGetLight

[Previous](GroupGet.md) | [Next](../Symbols.md)

# IMTReportAPI::GroupGetLight

Get an eased configuration of a group.
    
    
    MTAPIRES  IMTReportAPI::GroupGetLight(
       LPCWSTR      name,       // Name of agroup
       IMTConGroup  *group      // Group configuration object
       )

### Parameters

**name**  
[in] Name of a group. TheIMTConGroup::Group()value is used as a name.

***group**  
[out] An object of group configuration. The group object must be first created using theIMTReportAPI::GroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method submits all group parameters except symbols ([IMTConGroup::Symbol*](../../../../Configuration-Interfaces/Groups/IMTConGroup/SymbolAdd.md)) and commissions settings ([IMTConGroup::Commission*](../../../../Configuration-Interfaces/Groups/IMTConGroup/CommissionAdd.md)).
