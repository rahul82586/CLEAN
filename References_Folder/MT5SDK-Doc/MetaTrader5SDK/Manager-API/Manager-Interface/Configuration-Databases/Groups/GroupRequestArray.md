[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupRequestArray

[Previous](GroupRequest.md) | [Next](../Symbols.md)

# IMTManagerAPI::GroupRequestArray

Request from the server an array of groups by mask.

C++
    
    
    MTAPIRES  IMTManagerAPI::GroupRequestArray(
       LPCWSTR            mask,   // Mask
       IMTConGroupArray*  groups  // Object of the group array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.GroupRequestArray(
       string             mask,  // Mask
       CIMTConGroupArray  group  // Object of the group array
       )

Python
    
    
    ManagerAPI.GroupRequestArray(
       mask               # Mask
       )

### Parameters

**mask**  
[in] One or more groups separated by commas. Specify the full name of the group, including the path. For example, demo\demoforex. The group name can be obtained using theIMTConGroup::Groupmethod. Groups can also be specified using wildcard characters: "*" (any value) and "!" (exclude). For example: "demo*,!demoforex" — all groups whose names begin with 'demo', except for the group demoforex.

**groups**  
[out] Group array objectIMTConGroupArray. Must be previously created by using theIMTManagerAPI::GroupCreateArrayobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
