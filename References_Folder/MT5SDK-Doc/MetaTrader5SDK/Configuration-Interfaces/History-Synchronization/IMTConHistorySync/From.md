[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / From

[Previous](TimeCorrection.md) | [Next](To.md)

# IMTConHistorySync::From

Get the beginning date of the period for which history data are synchronized.

C++
    
    
    INT64  IMTConHistorySync::From()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConHistorySync.From()

Python (Manager API)
    
    
    MTConHistorySync.From

### Return Value

The beginning date of the period for which history data are synchronized, in seconds that have elapsed since 01.01.1970.

# IMTConHistorySync::From

Set the beginning date of the period for which history data are synchronized.

C++
    
    
    MTAPIRES  IMTConHistorySync::From(
       const INT64  from      // Beginning of the period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.From(
       long         from      // Beginning of the period
       )

Python (Manager API)
    
    
    MTConHistorySync.From

### Parameters

**from**  
[in] The beginning date of the period for which history data are synchronized. The date is specified in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
