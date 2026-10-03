[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Funds and ETF](../Funds-and-ETF.md) / FundNext

[Previous](FundTotal.md) | [Next](FundGet.md)

# IMTReportAPI::FundNext

Get a fund configuration by index.
    
    
    MTAPIRES  IMTReportAPI::FundNext(
       const UINT   pos,      // Configuration position
       IMTConFund*  config    // Fund configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out]Fundconfiguration object. The 'config' object must be previously created using theIMTReportAPI::FundCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the fund configuration with a specified index to the 'config' object.
