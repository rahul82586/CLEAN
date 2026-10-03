[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHolidaySink](../IMTConHolidaySink.md) / OnHolidayDelete

[Previous](OnHolidayUpdate.md) | [Next](OnHolidaySync.md)

# IMTConHolidaySink::OnHolidayDelete

A handler of the event of removing a holiday configuration.

C++
    
    
    virtual void  IMTConHolidaySink::OnHolidayDelete(
       const IMTConHoliday*  config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConHolidaySink.OnHolidayDelete(
       CIMTConHoliday        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify that a holiday configuration has been deleted.
