[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyStorage

[Previous](DailyBonus.md) | [Next](DailyCommInstant.md)

# IMTDaily::DailyStorage

Get the amount of swaps charged to a client for a reported day.

C++
    
    
    double  IMTDaily::DailyStorage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyStorage()

### Return Value

The amount of swaps charged to a client for a reported day.

# IMTDaily::DailyStorage

Set the amount of swaps charged to a client for a reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyStorage(
       const double  storage      // Daily swaps
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyStorage(
       double        storage      // Daily swaps
       )

### Parameters

**storage**  
[in] The amount of swaps charged to a client for a reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
