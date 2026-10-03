[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / MonthBegin

[Previous](DayBegin.md) | [Next](YearBegin.md)

# SMTTime::MonthBegin

Get the month beginning by the passed date.

C++
    
    
    static INT64  SMTTime::MonthBegin(
       const INT64  ctm      // Date
       )

.NET (Gateway/Manager API)
    
    
    static long  SMTTime.MonthBegin(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get the month beginning, in seconds that have elapsed since 01.01.1970.

### Return Value

The date that corresponds to the beginning of the day (00:00:00 of the first day of the month), the number of seconds since 01.01.1970.

### Note

The method returns the beginning of the month for the passed date. For example, if 1329310800 is passed (it corresponds to 15.02.2012 13:15:30), value 1328054400 will be returned (it corresponds to 01.02.2012 00:00:00).
