[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FilterGapTicks

[Previous](FilterGap.md) | [Next](SubscriptionsDelay.md)

# IMTConSymbol::FilterGapTicks

Get the number of ticks for disabling the gap mode. If no new gap occurs within the specified number of quotes, the mode is disabled.

C++
    
    
    UINT  IMTConSymbol::FilterGapTicks()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.FilterGapTicks()

Python (Manager API)
    
    
    MTConSymbol.FilterGapTicks

### Return Value

The number of ticks for disabling the gap mode. If no new gap occurs within the specified number of quotes, the mode is disabled.

### Note

The number includes the tick, on which the gap started. For example, suppose that we have the values of 100 points and 3 ticks. When a gap is detected, the tick counter is increased by 1. If no new price spike for the specified number of points occurs at the two subsequent ticks, the gap mode will be disabled at the next (fourth) tick:

  * The first tick, on which a gap occurred. The tick counter is set to 1.
  * The second tick without a gap. The tick counter is increased to 2. It is the first tick, which confirms the new price.
  * The third tick without a gap. The tick counter is increased to 3. It is the second tick, which confirms the new price.
  * The fourth tick without a gap. It is the third tick, which confirms the new price. The gap mode is switched off.



# IMTConSymbol::FilterGapTicks

Set the number of ticks for disabling the gap mode. If no new gap occurs within the specified number of quotes, the mode is disabled.

C++
    
    
    MTAPIRES  IMTConSymbol::FilterGapTicks(
       const UINT  ticks      // Number of ticks
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FilterGapTicks(
       uint        ticks      // Number of ticks
       )

Python (Manager API)
    
    
    MTConSymbol.FilterGapTicks

### Parameters

**ticks**  
[in] The number of ticks for disabling the gap mode. If no new gap occurs within the specified number of quotes, the mode is disabled.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The number includes the tick, on which the gap started. For example, suppose that we have the values of 100 points and 3 ticks. When a gap is detected, the tick counter is increased by 1. If no new price spike for the specified number of points occurs at the two subsequent ticks, the gap mode will be disabled at the next (fourth) tick:

  * The first tick, on which a gap occurred. The tick counter is set to 1.
  * The second tick without a gap. The tick counter is increased to 2. It is the first tick, which confirms the new price.
  * The third tick without a gap. The tick counter is increased to 3. It is the second tick, which confirms the new price.
  * The fourth tick without a gap. It is the third tick, which confirms the new price. The gap mode is switched off.


