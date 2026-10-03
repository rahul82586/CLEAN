[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / DailyBonus

[Previous](DailyCorrection.md) | [Next](DailyStorage.md)

# IMTDaily::DailyBonus

Get the amount of bonuses added to the client's balance for the reported day.

C++
    
    
    double  IMTDaily::DailyBonus()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.DailyBonus()

### Return Value

The amount of bonuses added to the client's balance for the reported day.

# IMTDaily::DailyBonus

Set the amount of bonuses added to the client's balance for the reported day.

C++
    
    
    MTAPIRES  IMTDaily::DailyBonus(
       const double  bonus      // Bonus for the day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.DailyBonus(
       double        bonus      // Bonus for the day
       )

### Parameters

**bonus**  
[in] the bonuses added to the client's balance for the reported day.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
