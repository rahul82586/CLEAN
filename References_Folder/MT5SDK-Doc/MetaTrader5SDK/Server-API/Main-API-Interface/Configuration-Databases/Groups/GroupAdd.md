[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupAdd

[Previous](GroupUnsubscribe.md) | [Next](GroupDelete.md)

# IMTServerAPI::GroupAdd

Adds or updates a group configuration.
    
    
    MTAPIRES  IMTServerAPI::GroupAdd(
       IMTConGroup*  group      // Group configuration object
       )

### Parameters

**group**  
[in] An object of group configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the name of the group [IMTConGroup::Group()](../../../../Configuration-Interfaces/Groups/IMTConGroup/Group.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConGroupSink::OnGroupUpdate](../../../../Configuration-Interfaces/Groups/IMTConGroupSink/OnGroupUpdate.md) notification method is not called.
