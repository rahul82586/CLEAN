[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Get

[Previous](CreateAgreement.md) | [Next](../Network.md)

# IMTReportAPI::CommonGet

Gets the common platform configuration.
    
    
    MTAPIRES  IMTReportAPI::CommonGet(
       IMTConCommon*  common      // A comment
       )

### Parameters

**common**  
[out] An object of the common configuration. The object must first be created using theIMTReportAPI::CommonCreateobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
