[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Data cache](../Data-cache.md) / KeySetParamLogins

[Previous](KeySetCreate.md) | [Next](../Subscriptions.md)

# IMTReportAPI::KeySetParamLogins

Fill the key set with the logins of trading accounts for which the report is generated.
    
    
    MTAPIRES  IMTReportAPI::KeySetParamLogins(
       IMTReportCacheKeySet*  keyset  // Set of keys
       )

### Parameters

**keyset**  
[in] TheIMTReportCacheKeySetobject which describes the set of keys.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Trading account logins are specified when requesting a report from the MetaTrader 5 Manager.
