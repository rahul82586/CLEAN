[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Server

[Previous](IMTHistoryDeal-Login.md) | [Next](IMTHistoryDeal-ExternalID.md)

# IMTECNHistoryDeal::Server

Get the identifier of the trade server on which the original order was placed.

C++
    
    
    UINT64  IMTECNHistoryDeal::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryDeal.Server()

### Return Value

The identifier of the trade server on which the original order was placed.

# IMTECNHistoryDeal::Server

Set the identifier of the trade server on which the original order was placed.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Server(
       const UINT64  server     // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Server(
       ulong         server     // identifier
       )

### Parameters

**server**  
[in] The identifier of the trade server on which the original order was placed.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
