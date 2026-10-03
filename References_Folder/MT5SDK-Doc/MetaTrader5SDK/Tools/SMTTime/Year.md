[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / Year

[Previous](TimeToST.md) | [Next](Month.md)

# SMTTime::Year

Get the year from the date passed in the Unix time format.

C++
    
    
    static UINT  SMTTime::Year(
       const INT64  ctm      // Date
       )

.NET (Gateway/Manager API)
    
    
    static uint  SMTTime.Year(
       long         ctm      // Date
       )

### Parameters

**ctm**  
[in] The date for which you want to get a year. Passed as a number of seconds that have elapsed since 01.01.1970.

### Return Value

Year.

### Note

The year is passed as is. For example, 2012, 2011 etc.
