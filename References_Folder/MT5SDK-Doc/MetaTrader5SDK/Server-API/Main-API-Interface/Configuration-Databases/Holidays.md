[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Holidays

[Previous](Time/Set.md) | [Next](Holidays/HolidayCreate.md)

# Holiday Configuration

Using the functions and interfaces described in this section, you can add holidays to the work timetable of the server, both for groups of symbols and for each symbol individually. On holidays, clients can connect, view charts and history of trades, but cannot trade.

Functions described in this section allow managing the holidays configuration, as well subscribe and unsubscribe from events associated with its change.

Function | Purpose  
---|---  
[HolidayCreate](Holidays/HolidayCreate.md) | Create an object of the configuration of holidays.  
[HolidaySubscribe](Holidays/HolidaySubscribe.md) | Subscribe to events and hooks associated with the configuration of holidays.  
[HolidayUnsubscribe](Holidays/HolidayUnsubscribe.md) | Unsubscribe from events and hooks associated with the configuration of holidays.  
[HolidayAdd](Holidays/HolidayAdd.md) | Add or update a holiday configuration.  
[HolidayDelete](Holidays/HolidayDelete.md) | Delete a holiday configuration by the index.  
[HolidayShift](Holidays/HolidayShift.md) | Changes the position of a holiday configuration in the list.  
[HolidayTotal](Holidays/HolidayTotal.md) | The total number of configurations of holidays available in the platform.  
[HolidayNext](Holidays/HolidayNext.md) | Gets a holiday configuration with the specified index.
