[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / Min

[Previous](Hour.md) | [Next](Sec.md)

# SMTTime::Min

Get minutes from the date passed in the Unix time format.

C++
    
    
    static UINT  SMTTime::Min(
       const INT64  ctm      // Date
       )

.NET
    
    
    static uint  SMTTime.Min(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get minutes. Passed as a number of seconds that have elapsed since 01.01.1970.

### Return Value

Minutes.

### Note

Example: for the date 1329310800 (15.02.2012 13:00:00) the method returns 0.
