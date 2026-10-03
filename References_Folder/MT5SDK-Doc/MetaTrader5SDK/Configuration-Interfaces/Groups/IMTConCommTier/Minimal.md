[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Minimal

[Previous](Value.md) | [Next](Maximal.md)

# IMTConCommTier::Minimal

Get the minimum amount of the commission charged.

C++
    
    
    double  IMTConCommTier::Minimal()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConCommTier.Minimal()

Python (Manager API)
    
    
    MTConCommTier.Minimal

### Return Value

Minimum commission amount. Commission units depend on the charging method, which can be obtained using [IMTConCommTier::Mode](Mode.md). If commission is calculated as a percentage, the values are specified in the client's deposit currency. In all other cases, the values are indicated according to the calculation method — in the base currency, the group currency, in points, etc.

# IMTConCommTier::Minimal

Set the minimum amount of the commission charged.

C++
    
    
    MTAPIRES  IMTConCommTier::Minimal(
       const double  value      // Minimum commission amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.Minimal(
       double        value      // Minimum commission amount
       )

Python (Manager API)
    
    
    MTConCommTier.Minimal

### Parameters

**value**  
[in] Minimum commission amount. Commission units depend on the charging method, which can be obtained usingIMTConCommTier::Mode. If commission is calculated as a percentage, the values are specified in the client's deposit currency. In all other cases, the values are indicated according to the calculation method — in the base currency, the group currency, in points, etc. If you do not want to limit the minimum commission amount, set the 0 value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred which corresponds to the response code.
