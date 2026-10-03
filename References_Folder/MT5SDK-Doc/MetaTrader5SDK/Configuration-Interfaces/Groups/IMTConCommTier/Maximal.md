[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Maximal

[Previous](Minimal.md) | [Next](RangeFrom.md)

# IMTConCommTier::Maximal

Get the maximum amount of the commission charged.

C++
    
    
    double  IMTConCommTier::Maximal()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConCommTier.Maximal()

Python (Manager API)
    
    
    MTConCommTier.Maximal

### Return Value

Maximum commission amount. Commission units depend on the charging method, which can be obtained using [IMTConCommTier::Mode](Mode.md). If commission is calculated as a percentage, the values are specified in the client's deposit currency. In all other cases, the values are indicated according to the calculation method — in the base currency, the group currency, in points, etc.

# IMTConCommTier::Maximal

Set the maximum amount of the commission charged.

C++
    
    
    MTAPIRES  IMTConCommTier::Maximal(
       const double  value      // Maximum commission amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.Maximal(
       double        value      // Maximum commission amount
       )

Python (Manager API)
    
    
    MTConCommTier.Maximal

### Parameters

**value**  
[in] Maximum commission amount. Commission units depend on the charging method, which can be obtained usingIMTConCommTier::Mode. If commission is calculated as a percentage, the values are specified in the client's deposit currency. In all other cases, the values are indicated according to the calculation method — in the base currency, the group currency, in points, etc. If you do not want to limit the maximum commission amount, set the 0 value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum commission value cannot be less than the minimum commission ([IMTConCommTier::Minimal](Minimal.md)).
