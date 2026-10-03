[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal TimeMsc

[Previous](IMTHistoryDeal-ExternalID.md) | [Next](IMTHistoryDeal-Symbol.md)

# IMTECNHistoryDeal::TimeMsc

Get deal execution time at the gateway.

C++
    
    
    INT64  IMTECNHistoryDeal::TimeMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTECNHistoryDeal.TimeMsc()

### Return Value

The time of deal execution on the gateway, in milliseconds since 01.01.1970.

# IMTECNHistoryDeal::TimeMsc

Set deal execution time at the gateway.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::TimeMsc(
       const INT64   time      // execution time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.TimeMsc(
       long          time      // execution time
       )

### Parameters

**time**  
[in] The time of deal execution on the gateway, in milliseconds since 01.01.1970.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
