[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyCommInstant

[Previous](DailyStorage.md) | [Next](DailyCommRound.md)

# IMTDaily::DailyCommInstant

Get the amount of instant [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged to a client during the reported day.

C++
    
    
    double  IMTDaily::DailyCommInstant()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyCommInstant()

### Return Value

The amount of instant commissions charged to the client during the reported day.

# IMTDaily::DailyCommInstant

Set the amount of instant [commissions](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) charged to a client during the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyCommInstant(
       const double  comm      // Instant commissions for a day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyCommInstant(
       double        comm      // Instant commissions for a day
       )

### Parameters

**comm**  
[in] The amount of instant commissions charged to the client during the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
