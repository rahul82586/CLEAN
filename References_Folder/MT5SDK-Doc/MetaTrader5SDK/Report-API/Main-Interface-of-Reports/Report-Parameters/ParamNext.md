[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Report Parameters](../Report-Parameters.md) / ParamNext

[Previous](ParamGet.md) | [Next](ParamLogins.md)

# IMTReportAPI::ParamNext

Get a report parameter set from a manager terminal by its position.
    
    
    MTAPIRES  IMTReportAPI::ParamNext(
       const UINT   pos,        // Position of the parameter
       IMTConParam  *param      // An object of a report parameter
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

***param**  
An object of a report parameter. The object must first be created using theIMTReportAPI::ParamCreateobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the report parameter data with a specified index to the param object.
