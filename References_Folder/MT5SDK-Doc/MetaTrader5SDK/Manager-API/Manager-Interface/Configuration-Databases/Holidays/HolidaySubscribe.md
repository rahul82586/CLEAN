[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidaySubscribe

[Previous](HolidayCreate.md) | [Next](HolidayUnsubscribe.md)

# IMTManagerAPI::HolidaySubscribe

Subscribe to events associated with the configuration of holidays.

C++
    
    
    MTAPIRES  IMTManagerAPI::HolidaySubscribe(
       IMTConHolidaySink*  sink      // A pointer to the IMTConHolidaySink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.HolidaySubscribe(
       CIMTConHolidaySink  sink      // CIMTConHolidaySink object
       )

Python
    
    
    ManagerAPI.HolidaySubscribe(
       sink                # IMTConHolidaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConHolidaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConHolidaySink](../../../../Configuration-Interfaces/Holidays/IMTConHolidaySink.md) cannot subscribe to events twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
