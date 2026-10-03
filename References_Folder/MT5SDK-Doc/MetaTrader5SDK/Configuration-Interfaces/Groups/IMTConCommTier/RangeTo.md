[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / RangeTo

[Previous](RangeFrom.md) | [Next](Currency.md)

# IMTConCommTier::RangeTo

Get the maximum trade volume (turnover) from which the commission will be charged.

C++
    
    
    double  IMTConCommTier::RangeTo()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConCommTier.RangeTo()

Python (Manager API)
    
    
    MTConCommTier.RangeTo

### Return Value

The maximum trade volume or turnover from which the commission will be charged. The type of range (trade volume or turnover) is defined using the [IMTConCommission::RangeMode](../IMTConCommission/RangeMode.md) method.

# IMTConCommTier::RangeTo

Set the maximum trade volume (turnover) from which the commission will be charged.

C++
    
    
    MTAPIRES  IMTConCommTier::RangeTo(
       const double  value      // Maximum volume
       )

Python (Manager API)
    
    
    MTConCommTier.RangeTo()

.NET (Gateway/Manager API)s
    
    
    MTRetCode  CIMTConCommTier.RangeTo(
       double        value      // Maximum volume
       )

Python (Manager API)
    
    
    MTConCommTier.RangeTo

### Parameters

**value**  
[in] The maximum trade volume or turnover from which the commission will be charged. The type of range (trade volume or turnover) is defined using theIMTConCommission::RangeModemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
