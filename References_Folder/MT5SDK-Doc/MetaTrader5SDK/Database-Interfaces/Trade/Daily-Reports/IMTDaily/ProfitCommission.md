[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / ProfitCommission

[Previous](ProfitStorage.md) | [Next](ProfitEquity.md)

# IMTDaily::ProfitCommission

Get the current unfixed commission of a client in a daily report.

C++
    
    
    double  IMTDaily::ProfitCommission()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.ProfitCommission()

### Return Value

The current unfixed commission of a client in a daily report (commissions that have been charged but not yet reflected in the balance).

### Note

The field is deprecated and is no longer used.

# IMTDaily::ProfitCommission

Set the current unfixed commission of a client in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::ProfitCommission(
       const double  commission      // Commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.ProfitCommission(
       double        commission      // Commission
       )

### Parameters

**commission**  
[in] The current unfixed commission of a client in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The current unfixed commission includes commissions already charged but not yet reflected in the balance.
