[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailyUnsubscribe

[Previous](DailySubscribe.md) | [Next](DailyGet.md)

# IMTServerAPI::DailyUnsubscribe

Unsubscribe from the events and hooks associated with changes in the database of daily reports.
    
    
    MTAPIRES  IMTServerAPI::DailyUnsubscribe(
       IMTDailySink*  sink      // A pointer to the IMTDailySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDailySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a paid method to [IMTServerAPI::DailySubscribe](DailySubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
