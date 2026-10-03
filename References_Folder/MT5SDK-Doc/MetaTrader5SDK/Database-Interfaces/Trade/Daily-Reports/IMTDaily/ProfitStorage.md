[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / ProfitStorage

[Previous](Profit.md) | [Next](ProfitCommission.md)

# IMTDaily::ProfitStorage

Get the current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance.

C++
    
    
    double  IMTDaily::ProfitStorage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.ProfitStorage()

### Return Value

The current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance.

# IMTDaily::ProfitStorage

Set the current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance.

C++
    
    
    MTAPIRES  IMTDaily::ProfitStorage(
       const double  storage      // Swaps
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.ProfitStorage(
       double        storage      // Swaps
       )

### Parameters

**storage**  
[in] The current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
