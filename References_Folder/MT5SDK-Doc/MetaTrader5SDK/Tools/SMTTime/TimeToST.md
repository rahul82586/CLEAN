[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / TimeToST

[Previous](STToTime.md) | [Next](Year.md)

# SMTTime::TimeToST

Converting a date in the Unix time format into the SYSTEMTIME structure.

C++
    
    
    static SYSTEMTIME&  SMTTime::TimeToST(
       INT64        ctm,     // Date
       SYSTEMTIME&  st       // The SYSTEMTIME structure
       )

.NET (Gateway/Manager API)
    
    
    static DateTime  SMTTime.ToDateTime(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date that you want to convert. Passed a the number of seconds since 01.01.1970.

**st**  
[in][out] A link to the SYSTEMTIME structure. The structure contains the following members:

  * wYear \- a value from 1601 to 30827 that indicates the year.
  * wMonth \- a value from 1 to 12 that indicates the month (1 corresponds to January).
  * wDayOfWeek \- a value from 0 to 6 that indicates the weekday (0 corresponds to Sunday).
  * wDay \- a value from 1 to 31 indicating the day of the month.
  * wHour \- a value from 0 to 23 indicating the number of hours since midnight..
  * wMinute \- a value from 0 to 59 indicating the number of minutes.
  * wSecond \- a value from 0 to 59 indicating the number of seconds.
  * wMilliseconds \- a value from 0 to 999 indicating the number of milliseconds.



### Return Value

A reference to the SYSTEMTIME structure.
