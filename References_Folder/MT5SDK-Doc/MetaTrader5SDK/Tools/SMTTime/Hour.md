[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / Hour

[Previous](Day.md) | [Next](Min.md)

# SMTTime::Hour

Get the hour from the date passed in the Unix time format.

C++
    
    
    static UINT  SMTTime::Hour(
       const INT64  ctm      // Date
       )

.NET (Gateway/Manager API)
    
    
    static uint  SMTTime.Hour(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get an hour. Passed as a number of seconds that have elapsed since 01.01.1970.

### Return Value

Hour.

### Note

Example: for the date 1329310800 (15.02.2012 13:00:00) the method returns 13.
