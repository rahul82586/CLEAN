[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Data Structure

[Previous](../Time.md) | [Next](Get-Server.md)

# Data Structure

Time configuration is passed in JSON format as a response to the [/api/time/get](Get-Settings.md) request. The time configuration includes the following parameters:

Option Field | Type | Description  
Daylight | Integer  | The mode of switching to the daylight saving time. 0 — DST switching disabled, 1 — enabled.  
DaylightState | Integer | The presence of the daylight saving time in the platform time zone. 0 means no daylight saving time is applied in the platform time zone. Otherwise, any non-zero value is used.  
TimeZone | Integer  | The time zone of the server. Specified in minutes from GMT. For example: 0 = GMT; -60 = GMT - 1; 60 = GMT + 1.  
TimeServer | String | The address of a server for synchronizing time.  
Days | Array of integer numbers | A two-dimensional array [7][24], where the first dimension denotes days of the week (starting with Sunday), the second one denotes hours. The sign of the working/nonworking hour is passed in a value of the [EnTimeTableMode (#entimetablemode)](../../../../Configuration-Interfaces/Time/IMTConTime/IMTCon-Enumerations.md#entimetablemode) enumeration.
