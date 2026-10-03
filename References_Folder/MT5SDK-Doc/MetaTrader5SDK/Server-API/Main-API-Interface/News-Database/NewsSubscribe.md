[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [News Database](../News-Database.md) / NewsSubscribe

[Previous](NewsCreate.md) | [Next](NewsUnsubscribe.md)

# IMTServerAPI::NewsSubscribe

Subscribe to events and hooks associated with changes in the news database.
    
    
    MTAPIRES  IMTServerAPI::NewsSubscribe(
       IMTNewsSink*  sink      // A pointer to the IMTNewsSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTNewsSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTNewsSink](../../../Database-Interfaces/News-Database/IMTNewsSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
