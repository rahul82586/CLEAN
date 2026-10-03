[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / To

[Previous](From.md) | [Next](SymbolAdd.md)

# IMTConHistorySync::To

Get the end date of the period for which history data are synchronized.

C++
    
    
    INT64  IMTConHistorySync::To()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConHistorySync.To()

Python (Manager API)
    
    
    MTConHistorySync.To

### Return Value

The end date of the period for which history data are synchronized, in seconds that have elapsed since 01.01.1970.

# IMTConHistorySync::To

Set the end date of the period for which history data are synchronized.

C++
    
    
    MTAPIRES  IMTConHistorySync::To(
       const INT64  to      // End of period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.To(
       long         to      // End of period
       )

Python (Manager API)
    
    
    MTConHistorySync.To

### Parameters

**to**  
[in] The end date of the period for which history data are synchronized. The date is specified in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
