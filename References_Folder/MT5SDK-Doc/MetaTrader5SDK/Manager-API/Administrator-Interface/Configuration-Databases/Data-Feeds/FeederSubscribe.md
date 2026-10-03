[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederSubscribe

[Previous](FeederTranslateCreate.md) | [Next](FeederUnsubscribe.md)

# IMTAdminAPI::FeederSubscribe

Subscribe to events associated with the configuration of data feeds.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederSubscribe(
       IMTConFeederSink*  sink      // A pointer to the IMTConFeederSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederSubscribe(
       CIMTConFeederSink  sink      // CIMTConFeederSink object
       )

Python
    
    
    AdminAPI.FeederSubscribe(
       sink      # IMTConFeederSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConFeederSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConFeederSink](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
