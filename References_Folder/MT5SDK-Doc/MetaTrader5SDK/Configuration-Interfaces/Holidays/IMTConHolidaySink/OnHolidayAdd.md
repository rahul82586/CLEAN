[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHolidaySink](../IMTConHolidaySink.md) / OnHolidayAdd

[Previous](../IMTConHolidaySink.md) | [Next](OnHolidayUpdate.md)

# IMTConHolidaySink::OnHolidayAdd

A handler of the event of adding a new holiday configuration.

C++
    
    
    virtual void  IMTConHolidaySink::OnHolidayAdd(
       const IMTConHoliday*  config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConHolidaySink.OnHolidayAdd(
       CIMTConHoliday        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by the API to notify that a new holiday configuration has been added.
