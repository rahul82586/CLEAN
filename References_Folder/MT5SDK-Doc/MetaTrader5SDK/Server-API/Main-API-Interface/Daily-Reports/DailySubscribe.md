[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailySubscribe

[Previous](DailyCreateArray.md) | [Next](DailyUnsubscribe.md)

# IMTServerAPI::DailySubscribe

Subscribe to events and hooks associated with changes in the database of daily reports.
    
    
    MTAPIRES  IMTServerAPI::DailySubscribe(
       IMTDailySink*  sink      // A pointer to the IMTDailySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDailySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTDailySink](../../../Database-Interfaces/Trade/Daily-Reports/IMTDailySink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
