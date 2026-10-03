[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [News Database](../News-Database.md) / NewsUnsubscribe

[Previous](NewsSubscribe.md) | [Next](NewsSend.md)

# IMTServerAPI::NewsUnsubscribe

Undubscribe from events and hooks associated with changes in the news database.
    
    
    MTAPIRES  IMTServerAPI::NewsUnsubscribe(
       IMTNewsSink*  sink      // A pointer to the IMTNewsSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTNewsSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::NewsSubscribe](NewsSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
