[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Report Parameters](../Report-Parameters.md) / ParamGet

[Previous](ParamTotal.md) | [Next](ParamNext.md)

# IMTReportAPI::ParamGet

Get a report parameter set in a manager terminal by its name.
    
    
    MTAPIRES  IMTReportAPI::ParamGet(
       LPCWSTR      name,       // Parameter name
       IMTConParam  *param      // An object of a report parameter
       )

### Parameters

**name**  
[in] Parameter Name.

***param**  
[out] An object of a report parameter. The object must first be created using theIMTReportAPI::ParamCreateobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the report parameter data with a specified name to the param object.
