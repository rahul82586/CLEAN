[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayUpdateBatch

[Previous](HolidayUpdate.md) | [Next](HolidayDelete.md)

# IMTAdminAPI::HolidayUpdateBatch

Add or edit multiple holiday configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::HolidayUpdateBatch(
       IMTConHoliday**  configs,      // An array of configurations
       const UINT       config_total, // The number of configurations in the array
       MTAPIRES*        results       // An array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HolidayUpdateBatch(
       CIMTConHoliday[] configs,      // An array of configurations
       MTRetCode[]      results       // An array of results
       )

Python.NET
    
    
    AdminAPI.HolidayUpdateBatch(
       holidays         # An array of configurations
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to add/delete.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of applying of each configuration change on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful sending of changes to a server; results of applying the changes are passed in the 'results' parameter.

### Further Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. The key fields for comparison are the date ([IMTConHoliday::Year](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Year.md), [IMTConHoliday::Month](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Month.md), [IMTConHoliday::Day](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Day.md)), time ([IMTConHoliday::WorkFrom](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/WorkFrom.md), [IMTConHoliday::WorkTo](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/WorkTo.md)) and description ([IMTConHoliday::Description](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Description.md)). When you try to add a completely identical record, no changes are made, and therefore the [IMTConHolidaySink::OnHolidayUpdate](../../../../Configuration-Interfaces/Holidays/IMTConHolidaySink/OnHolidayUpdate.md) notification method is not called.
