[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon TableSet

[Previous](IMTCon-TableGet.md) | [Next](IMTCon-Daylight.md)

# IMTConTime::TimeTableSet

Set the working time of a trading platform for a specified week and hour.

C++
    
    
    MTAPIRES  IMTConTime::TimeTableSet(
       const UINT  wday,     // Day of the week
       const UINT  hour,     // Hour
       const UINT  mode      // Operation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConTime.TimeTableSet(
       uint        wday,     // Day of the week
       uint        hour,     // Hour
       uint        mode      // Operation mode
       )

Python (Manager API)
    
    
    MTConTime.TimeTableSet(
       wday,       # Day of the week
       hour,       # Hour
       mode        # Operation mode
       )
    
    
    MTConTime.TimeTableSet(
       timetable   # Time configuration object
       )
    
    
    MTConTime.TimeTable()

### Parameters

**wday**  
[in] To specify the day of the week, values 0 to 6 are used. 0 - Sunday, 6 - Saturday.

**hour**  
[in] The hour for which we set the working schedule.

**mode**  
[in] Server working schedule. To pass the mode, theIMTConTime::EnTimeTableModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
