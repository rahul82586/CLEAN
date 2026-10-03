[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTTime](../SMTTime.md) / MonthName

[Previous](MakeTime.md) | [Next](MonthNameShort.md)

# SMTTime::MonthName

Get the name of a month by its number.
    
    
    static LPCWSTR  SMTTime::MonthName(
       const UCHAR  month      // Month number
       )

### Parameters

**month**  
[in] The number of the month starting with 0. The value 0 corresponds to January, 11 - to December.

### Return Value

The name of the month.

### Note

If a number outside the range 0-11 is given, the Unknown value is returned.
