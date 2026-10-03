[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / ParseTime

[Previous](Macros.md) | [Next](MakeTime.md)

# SMTTime::ParseTime

Parse a date in the Unix time format into a tm structure.
    
    
    static bool  SMTTime::ParseTime(
       const INT64  ctm,      // Date
       tm           *ttm      // A tm structure
       )

### Parameters

**ctm**  
[in] Date in seconds that have elapsed since 01.01.1970.

***ttm**  
[out] The tm structure that contains the following members:

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

In case of a successful parse returns true, otherwise returns false.
