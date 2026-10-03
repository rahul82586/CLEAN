[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / Macros

[Previous](../SMTTime.md) | [Next](ParseTime.md)

# Macros

The include file MT5APITime.h contains definitions of the macros of minutes and seconds that improve the readability of the code by replacing numeric expressions by clear identifiers.

C++ ID | .NET function | Value | Description  
---|---|---|---  
SECONDS_IN_MINUTE | long MinutesInDay() | INT64(60) | The number of seconds in a minute.  
SECONDS_IN_HOUR | long SecondsInHour() | INT64(60*SECONDS_IN_MINUTE) | The number of seconds in an hour.  
SECONDS_IN_DAY | long SecondsInDay() | INT64(24*SECONDS_IN_HOUR) | The number of seconds in a day.  
SECONDS_IN_WEEK | long SecondsInWeek() | INT64(7*SECONDS_IN_DAY) | The number of seconds in a week.  
SECONDS_IN_MONTH | long SecondsInMonth() | INT64(30*SECONDS_IN_DAY) | The number of seconds in a month.  
MINUTES_IN_HOUR | long MinutesInHour() | (60) | Number of minutes in an hour.  
MINUTES_IN_DAY | long MinutesInDay() | (24*MINUTES_IN_HOUR) | Number of minutes in a day.  
MINUTES_IN_WEEK | long MinutesInWeek() | (7*MINUTES_IN_DAY) | Number of hours in a week.
