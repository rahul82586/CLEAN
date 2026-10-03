[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [History Data](../History-Data.md) / ChartSubscribe

[Previous](../History-Data.md) | [Next](ChartUnsubscribe.md)

# IMTServerAPI::ChartSubscribe

Subscribe to events and hooks associated with changes in the database of one-minute data.
    
    
    MTAPIRES  IMTServerAPI::ChartSubscribe(
       IMTChartSink*  sink      // Pointer to the IMTChartSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implements theIMTChartSinkinterface.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread-safe. The same [IMTChartSink](../../../Database-Interfaces/Price-Data/IMTChartSink.md) interface cannot subscribe to an event twice  in this case, the [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) response code is returned.
