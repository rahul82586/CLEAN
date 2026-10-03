[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / YearBegin

[Previous](MonthBegin.md) | [Next](STToTime.md)

# SMTTime::YearBegin

Get the year beginning by the passed date.

C++
    
    
    static INT64  SMTTime::YearBegin(
       const INT64  ctm      // Date
       )

.NET (Gateway/Manager API)
    
    
    static long  SMTTime::YearBegin(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get the year beginning, in seconds that have elapsed since 01.01.1970.

### Return Value

The date that corresponds to the beginning of the year (January 1st 00:00:00), the number of seconds since 01.01.1970.

### Note

The method returns the beginning of the month for the passed date. For example, if 1329310800 is passed (it corresponds to 15.02.2012 13:15:30), value 1325376000 will be returned (it corresponds to 01.01.2012 00:00:00).
