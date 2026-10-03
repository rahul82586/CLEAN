[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Recalculation

[Previous](Type.md) | [Next](StartDate.md)

# IMTConFund::Recalculation

Get fund chart recalculation mode.

C++
    
    
    UINT  IMTConFund::Recalculation()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.Recalculation()

### Return Value

Fund chart recalculation mode as an [IMTConFund::EnRecalculation (#enrecalculation)](Enumerations.md#enrecalculation) enumeration value.

# IMTConFund::Recalculation

Set fund chart recalculation mode.

C++
    
    
    MTAPIRES  IMTConFund::Recalculation(
       const UINT  recalculation  // Recalculation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Recalculation(
       uint        recalculation  // Recalculation mode
       )

### Parameters

**recalculation**  
[in] Fund chart recalculation mode as anIMTConFund::EnRecalculationenumeration value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
