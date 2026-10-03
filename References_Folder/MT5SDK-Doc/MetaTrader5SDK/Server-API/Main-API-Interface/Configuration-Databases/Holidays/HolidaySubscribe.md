[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidaySubscribe

[Previous](HolidayCreate.md) | [Next](HolidayUnsubscribe.md)

# IMTServerAPI::HolidaySubscribe

Subscribe to events and hooks associated with the configuration of holidays.
    
    
    MTAPIRES  IMTServerAPI::HolidaySubscribe(
       IMTConHolidaySink*  sink      // A pointer to the IMTConHolidaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConHolidaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConHolidaySink](../../../../Configuration-Interfaces/Holidays/IMTConHolidaySink.md) cannot subscribe to events twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
