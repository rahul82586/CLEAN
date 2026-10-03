[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / WeekBegin

[Previous](MonthNameShort.md) | [Next](DayBegin.md)

# SMTTime::WeekBegin

Get the week beginning by the passed date.

C++
    
    
    static INT64  SMTTime::WeekBegin(
       const INT64  ctm      // Date
       )

.NET (Gateway/Manager API)
    
    
    static long  SMTTime.WeekBegin(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get the week beginning, in seconds that have elapsed since 01.01.1970.

### Return Value

The date that corresponds to the beginning of the week (00:00:00 Sunday), the number of seconds since 01.01.1970.

### Note

The method returns the beginning of the week for the passed date. For example, if 1328102130 is passed (it corresponds to 01.02.2012 13:15:30), value 1327795200 will be returned (it corresponds to 29.01.2012 00:00:00, Sunday).
