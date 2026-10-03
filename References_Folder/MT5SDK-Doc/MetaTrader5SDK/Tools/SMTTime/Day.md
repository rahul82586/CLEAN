[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / Day

[Previous](Month.md) | [Next](Hour.md)

# SMTTime::Day

Get the day from the date passed in the Unix time format.

C++
    
    
    static UINT  SMTTime::Day(
       const INT64  ctm      // Date
       )

.NET (Gateway/Manager API)
    
    
    static uint  SMTTime.Day(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get a day. Passed as a number of seconds that have elapsed since 01.01.1970.

### Return Value

Day.

### Note

Example: for the date 1329310800 (15.02.2012 13:00:00) the method returns 15.
