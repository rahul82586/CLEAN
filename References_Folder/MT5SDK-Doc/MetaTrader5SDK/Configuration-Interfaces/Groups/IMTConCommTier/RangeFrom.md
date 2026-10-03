[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / RangeFrom

[Previous](Maximal.md) | [Next](RangeTo.md)

# IMTConCommTier::RangeFrom

Get the minimum trade volume (turnover) from which the commission will be charged.

C++
    
    
    double  IMTConCommTier::RangeFrom()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConCommTier.RangeFrom()

Python (Manager API)
    
    
    MTConCommTier.RangeFrom

### Return Value

The minimum trade volume or turnover from which the commission will be charged. The type of range (trade volume or turnover) is defined using the [IMTConCommission::RangeMode](../IMTConCommission/RangeMode.md) method.

# IMTConCommTier::RangeFrom

Set the minimum trade volume (turnover) from which the commission will be charged.

C++
    
    
    MTAPIRES  IMTConCommTier::RangeFrom(
       const double  value      // Minimum volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.RangeFrom(
       double        value      // Minimum volume
       )

Python (Manager API)
    
    
    MTConCommTier.RangeFrom

### Parameters

**value**  
[in] The minimum trade volume or turnover from which the commission will be charged. The type of range (trade volume or turnover) is defined using theIMTConCommission::RangeModemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
