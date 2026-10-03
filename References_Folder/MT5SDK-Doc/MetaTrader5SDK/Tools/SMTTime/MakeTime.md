[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / MakeTime

[Previous](ParseTime.md) | [Next](MonthName.md)

# SMTTime::MakeTime

Form a date in the Unix time format from a passed tm structure.
    
    
    static INT64  SMTTime::MakeTime(
       tm  *ttm      // A prepared tm structure
       )

### Parameters

***ttm**  
[in] A prepared tm structure. Members:

  * tm_sec contains a value from 0 to 59 indicating the number of seconds.
  * tm_min contains a value from 0 to 59 indicating the number of minutes.
  * tm_hour contains a value from 0 to 23 indicating the number of hours since midnight.
  * tm_mday contains a value from 1 to 31 indicating the day of the month.
  * tm_mon contains a value from 0 to 11 indicating the month number (0 corresponds to January).
  * tm_year indicates the number of years that have elapsed since 1990.
  * tm_wday contains a value from 0 to 6 indicating the number if the weekday (0 corresponds to Sunday).
  * tm_yday contains a value from 0 to 365 that indicates the number of days since January 1.
  * tm_isdst indicates the use of the daylight saving time (true - enabled, false - disabled).



### Return Value

Date in the number of seconds since 01.01.1970.
