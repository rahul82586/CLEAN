[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Type

[Previous](Flags.md) | [Next](Recalculation.md)

# IMTConFund::Type

Get the fund type.

C++
    
    
    UINT  IMTConFund::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.Type()

### Return Value

Fund type as a value of the [IMTConFund::EnType (#entype)](Enumerations.md#entype) enumeration.

# IMTConFund::Type

Set the fund type.

C++
    
    
    MTAPIRES  IMTConFund::Type(
       const UINT  type      // Fund type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Type(
       uint        type      // Fund type
       )

### Parameters

**type**  
[in] Fund type as a value of theIMTConFund::EnTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
