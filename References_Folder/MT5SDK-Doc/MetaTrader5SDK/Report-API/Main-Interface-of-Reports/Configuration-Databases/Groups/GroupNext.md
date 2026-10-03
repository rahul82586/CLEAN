[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupNext

[Previous](GroupTotal.md) | [Next](GroupGet.md)

# IMTReportAPI::GroupNext

Get the group configuration by the index.
    
    
    MTAPIRES  IMTReportAPI::GroupNext(
       const UINT    pos,       // Position of the configuration
       IMTConGroup*  group      // Group configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**group**  
[out] An object of group configuration. The group object must be first created using theIMTReportAPI::GroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a group with a specified index to the group object.
