[🏠 Document Start](../README.md) / [Tools](README.md) / SMTTime

[Previous](CMTThread/Priority.md) | [Next](SMTTime/Macros.md)

# SMTTime

This class is used for working with dates and times. It contains the following methods:

Method | Purpose  
---|---  
[ParseTime](SMTTime/ParseTime.md) | Parse a date in the Unix time format into a tm structure.  
[MakeTime](SMTTime/MakeTime.md) | Form a date in the Unix time format from a passed tm structure.  
[MonthName](SMTTime/MonthName.md) | Get the name of a month by its number.  
[MonthNameShort](SMTTime/MonthNameShort.md) | Get the short name of a month by its number.  
[WeekBegin](SMTTime/WeekBegin.md) | Get the week beginning by the passed date.  
[DayBegin](SMTTime/DayBegin.md) | Get the day beginning by the passed date.  
[MonthBegin](SMTTime/MonthBegin.md) | Get the month beginning by the passed date.  
[YearBegin](SMTTime/YearBegin.md) | Get the year beginning by the passed date.  
[STToTime](SMTTime/STToTime.md) | Converting a date in the SYSTEMTIME structure to the Unix time format.  
[TimeToST](SMTTime/TimeToST.md) | Converting a date in the Unix time format into the SYSTEMTIME structure.  
[Year](SMTTime/Year.md) | Get the year from the date passed in the Unix time format.  
[Month](SMTTime/Month.md) | Get the month from the date passed in the Unix time format.  
[Day](SMTTime/Day.md) | Get the day from the date passed in the Unix time format.  
[Hour](SMTTime/Hour.md) | Get the hour from the date passed in the Unix time format.  
[Min](SMTTime/Min.md) | Get minutes from the date passed in the Unix time format.  
[Sec](SMTTime/Sec.md) | Get seconds from the date passed in the Unix time format.  
  
The include file MT5APITime.h contains definitions of the [macros](SMTTime/Macros.md) of minutes and seconds that improve the readability of the code by replacing numeric expressions by clear identifiers.
