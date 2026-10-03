[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Report Parameters](../Report-Parameters.md) / ParamLogins

[Previous](ParamNext.md) | [Next](ParamFrom.md)

# IMTReportAPI::ParamLogins

Get an array of the logins, for which a report from a manager terminal is requested.
    
    
    MTAPIRES  IMTReportAPI::ParamLogins(
       UINT64*&  logins,     // An array of client logins
       UINT&     total       // The number of logins 
       )

### Parameters

**logins**  
[out] An array of client logins.

**total**  
[out] The number of logins in the logins array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Logins array is generated based on the "Groups" parameter that was set during a report request through a manager terminal. Both individual users and groups can be indicated in the "Groups" parameter. Indicated groups are arranged as lists of logins included in them. Therefore, the [MTReportParam::TYPE_GROUPS](../../../Structures/MTReportParam.md) mode must be turned on for this method operation in a report.
