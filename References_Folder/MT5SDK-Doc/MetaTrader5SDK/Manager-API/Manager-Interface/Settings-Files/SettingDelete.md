[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Settings Files](../Settings-Files.md) / SettingDelete

[Previous](SettingSet.md) | [Next](../Subscriptions.md)

# IMTManagerAPI::SettingDelete

Deletes the settings file on the trade server.

C++
    
    
    MTAPIRES  IMTManagerAPI::SettingDelete(
       LPCWSTR        section,        // directory name
       LPCWSTR        key             // file name
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SettingDelete(
       string         section,        // directory name
       string         key             // file name
       )

Python
    
    
    ManagerAPI.SettingDelete(
       section,       # directory name
       key            # file name
       )

### Parameters

**section**  
[in] The name of the subfolder in the manager account directory, from which you want to delete the settings file.

**key**  
[in] The name of the settings file.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned. The [MT_RET_ERR_PARAMS](../../../Return-Codes/Common-errors.md) response code means that invalid parameters were passed: the name of the folder or the file.
