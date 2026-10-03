[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon TableGet

[Previous](IMTCon-Server.md) | [Next](IMTCon-TableSet.md)

# IMTConTime::TimeTableGet

Get the working time of a trading platform for a specified week and hour.

C++
    
    
    MTAPIRES  IMTConTime::TimeTableGet(
       const UINT  wday,     // Day of the week
       const UINT  hour,     // Hour
       UINT&       mode      // Mode of operation
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConTime.TimeTableGet(
       uint        wday,     // Day of the week
       uint        hour,     // Hour
       out uint    mode      // Mode of operation
       )

Python (Manager API)
    
    
    MTConTime.TimeTableGet(
       wday,       # Day of the week
       hour        # Hour
       )
    
    
    MTConTime.TimeTableGet()
    
    
    MTConTime.TimeTable()

### Parameters

**wday**  
[in] To specify the day of the week, values 0 to 6 are used. 0 - Sunday, 6 - Saturday.

**hour**  
[in] The hour for which we get the working schedule.

**mode**  
[out] Server working schedule. To pass the mode, theIMTConTime::EnTimeTableModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
