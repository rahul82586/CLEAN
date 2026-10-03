[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHolidaySink](../IMTConHolidaySink.md) / OnHolidayUpdate

[Previous](OnHolidayAdd.md) | [Next](OnHolidayDelete.md)

# IMTConHolidaySink::OnHolidayUpdate

A handler of the event of updating a holiday configuration.

C++
    
    
    virtual void  IMTConHolidaySink::OnHolidayUpdate(
       const IMTConHoliday*  config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConHolidaySink.OnHolidayUpdate(
       CIMTConHoliday        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the updated configuration object.

### Note

This method is called by the API to notify that a holiday configuration has changed.
