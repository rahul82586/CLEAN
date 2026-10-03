[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayUnsubscribe

[Previous](HolidaySubscribe.md) | [Next](HolidayTotal.md)

# IMTManagerAPI::HolidayUnsubscribe

Unsubscribe from events associated with the configuration of holidays.

C++
    
    
    MTAPIRES  IMTManagerAPI::HolidayUnsubscribe(
       IMTConHolidaySink*  sink      // A pointer to the IMTConHolidaySink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.HolidayUnsubscribe(
       CIMTConHolidaySink  sink      // CIMTConHolidaySink object
       )

Python
    
    
    ManagerAPI.HolidayUnsubscribe(
       sink                # IMTConHolidaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConHolidaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::HolidaySubscribe](HolidaySubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
