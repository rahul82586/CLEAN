[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Funds and ETF](../Funds-and-ETF.md) / FundGet

[Previous](FundNext.md) | [Next](../../Clients.md)

# IMTReportAPI::FundGet

Get a fund configuration by name.
    
    
    MTAPIRES  IMTReportAPI::FundGet(
       LPCWSTR      name,     // Configuration name
       IMTConFund*  config    // Fund configuration object
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConSubscription::Namevalue is used for the configuration name.

**config**  
[out]Fundconfiguration object. The 'config' object must be previously created using theIMTReportAPI::FundCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
