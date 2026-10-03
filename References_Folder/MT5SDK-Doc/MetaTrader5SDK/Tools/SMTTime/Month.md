[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / Month

[Previous](Year.md) | [Next](Day.md)

# SMTTime::Month

Get the month from the date passed in the Unix time format.

C++
    
    
    static UINT  SMTTime::Month(
       const INT64  ctm      // Date
       )

.NET (Gateway/Manager API)
    
    
    static uint  SMTTime.Month(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get a month. Passed as a number of seconds that have elapsed since 01.01.1970.

### Return Value

The month number. 1 corresponds to January, 12 - to December.

### Note

Example: for the date 1329310800 (15.02.2012 13:00:00) the method returns 2.
