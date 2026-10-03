[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederUnsubscribe

[Previous](FeederSubscribe.md) | [Next](FeederRestart.md)

# IMTAdminAPI::FeederUnsubscribe

Unsubscribe from events associated with the configuration of data feeds.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederUnsubscribe(
       IMTConFeederSink*  sink      // A pointer to the IMTConFeederSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederUnsubscribe(
       CIMTConFeederSink  sink      // CIMTConFeederSink object
       )

Python
    
    
    AdminAPI.FeederUnsubscribe(
       sink      # IMTConFeederSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConFeederSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::FeederSubscribe](FeederSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
