[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayUnsubscribe

[Previous](HolidaySubscribe.md) | [Next](HolidayAdd.md)

# IMTServerAPI::HolidayUnsubscribe

Unsubscribe from events and hooks associated with the configuration of holidays.
    
    
    MTAPIRES  IMTServerAPI::HolidayUnsubscribe(
       IMTConHolidaySink*  sink      // A pointer to the IMTConHolidaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConHolidaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::HolidaySubscribe](HolidaySubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
