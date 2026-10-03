[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [History Data](../History-Data.md) / ChartUnsubscribe

[Previous](ChartSubscribe.md) | [Next](ChartGet.md)

# IMTServerAPI::ChartUnsubscribe

Unsubscribe from the events and hooks associated with changes in the database of one-minute data.
    
    
    MTAPIRES  IMTServerAPI::ChartUnsubscribe(
       IMTChartSink*  sink      // Pointer to the IMTChartSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implements theIMTChartSinkinterface.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is paired with [IMTServerAPI::ChartSubscribe](ChartSubscribe.md). If an attempt is made to unsubscribe from the interface that was not previously subscribed to, the [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
