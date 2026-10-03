[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyCommRound

[Previous](DailyCommInstant.md) | [Next](DailyCommFee.md)

# IMTDaily::DailyCommRound

Get the amount of turnover [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged to the client for a reported day.

C++
    
    
    double  IMTDaily::DailyCommRound()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyCommRound()

### Return Value

The amount of turnover positions charged to the client for a reported day.

# IMTDaily::DailyCommRound

Set the amount of turnover [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged to the client for a reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyCommRound(
       const double  comm      // Daily turnover commissions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyCommRound(
       double        comm      // Daily turnover commissions
       )

### Parameters

**comm**  
[in] The amount of turnover positions charged to the client for a reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
