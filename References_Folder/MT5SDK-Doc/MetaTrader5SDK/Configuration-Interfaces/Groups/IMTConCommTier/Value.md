[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Value

[Previous](Type.md) | [Next](Minimal.md)

# IMTConCommTier::Value

Get the amount of commission.

C++
    
    
    double  IMTConCommTier::Value()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConCommTier.Value()

Python (Manager API)
    
    
    MTConCommTier.Value

### Return Value

Commission amount. Commission units depend on the charging method, which can be obtained using [IMTConCommTier::Mode](Mode.md).

# IMTConCommTier::Value

Set the amount of commission.

C++
    
    
    MTAPIRES  IMTConCommTier::Value(
       const double  value      // Commission amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.Value(
       double        value      // Commission amount
       )

Python (Manager API)
    
    
    MTConCommTier.Value

### Parameters

**value**  
[in] Commission amount. Commission units depend on the charging method, which can be obtained usingIMTConCommTier::Mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
