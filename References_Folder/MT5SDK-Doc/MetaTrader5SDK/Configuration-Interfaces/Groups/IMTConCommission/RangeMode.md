[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / RangeMode

[Previous](Mode.md) | [Next](ChargeMode.md)

# IMTConCommission::RangeMode

Get the type of commission ranges - by trade volume or turnover.

C++
    
    
    UINT  IMTConCommission::RangeMode()  const

.NET (Gateway/Manager API)
    
    
    EnCommRangeMode  CIMTConCommission.RangeMode()

Python (Manager API)
    
    
    MTConCommission.RangeMode

### Return Value

One of the values of the [IMTConCommission::EnCommRangeMode (#encommrangemode)](Enumerations.md#encommrangemode) enumeration.

# IMTConCommission::RangeMode

Set the type of commission ranges - by trade volume or turnover.

C++
    
    
    MTAPIRES  IMTConCommission::RangeMode(
       const UINT       mode  // Type of commission ranges
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.RangeMode(
       EnCommRangeMode  mode  // Type of commission ranges
       )

Python (Manager API)
    
    
    MTConCommission.RangeMode

### Parameters

**mode**  
[in] Type of commission ranges. TheIMTConCommission::EnCommRangeModeenumeration is used to pass the commission ranges..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
