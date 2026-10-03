[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Datetime

[Previous](Clear.md) | [Next](DatetimePrev.md)

# IMTDaily::Datetime

Get the date and time of the daily report generation.

C++
    
    
    INT64  IMTDaily::Datetime()   const

.NET (Gateway/Manager API)
    
    
    long  CIMTDaily.Datetime()

### Return Value

Date and time of the daily report generation, in seconds that have elapsed since 01.01.1970.

# IMTDaily::Datetime

Set the date and time of the daily report generation.

C++
    
    
    MTAPIRES  IMTDaily::Datetime(
       const INT64  datetime      // Date and time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Datetime(
       long         datetime      // Date and time
       )

### Parameters

**datetime**  
[in] Date and time of the daily report generation, in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
