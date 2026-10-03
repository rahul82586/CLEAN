[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayUnsubscribe

[Previous](HolidaySubscribe.md) | [Next](HolidayUpdate.md)

# IMTAdminAPI::HolidayUnsubscribe

Unsubscribe from events associated with the configuration of holidays.

C++
    
    
    MTAPIRES  IMTAdminAPI::HolidayUnsubscribe(
       IMTConHolidaySink*  sink      // A pointer to the IMTConHolidaySink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HolidayUnsubscribe(
       CIMTConHolidaySink  sink      // CIMTConHolidaySink object
       )

Python
    
    
    AdminAPI.HolidayUnsubscribe(
       sink                # IMTConHolidaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConHolidaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::HolidaySubscribe](HolidaySubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
