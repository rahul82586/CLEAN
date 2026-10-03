[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / Data Structure

[Previous](../Holidays.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

A holiday configuration is passed in JSON format as a response to the [/api/holiday/add](Add.md) and [/api/holiday/next](Get-by-Index.md) requests.

Parameter | Type | Purpose  
Description | String | Description of a holiday.  
Mode | Integer | The state of the holiday. Passed as a value of [EnHolidayMode (#enholidaymode)](../../../../Configuration-Interfaces/Holidays/IMTConHoliday/Enumerations.md#enholidaymode).  
Year | Integer | The year of a holiday.  
Month | Integer | The month of a holiday.  
Day | Integer | The day of a holiday.  
From | Integer | The beginning of the range of the server working time on a holiday, in minutes since 00:00.  
To | Integer | The end of the range of the server working time on a holiday, in minutes since 00:00.  
Symbols | Array | [The list of symbols (#symbols)](Data-Structure.md#symbols), to which the holiday applies.  
  
<a id="symbols"></a>
## List of symbols (#symbols)

Parameter | Type | Purpose  
Path | String | Path to the symbol.
