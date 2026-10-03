[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeManagementAssets

[Previous](FeeManagementValue.md) | [Next](FeeSuccessCalc.md)

# IMTConFund::FeeManagementAssets

Get the fund management fee calculation mode.

C++
    
    
    UINT  IMTConFund::FeeManagementAssets()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeeManagementAssets()

### Return Value

Fund management fee calculation mode as a value of the [IMTConFund::EnFeeAssests (#enfeeassests)](Enumerations.md#enfeeassests) enumeration.

# IMTConFund::FeeManagementAssets

Set the fund management fee calculation mode.

C++
    
    
    MTAPIRES  IMTConFund::FeeManagementAssets(
       const UINT  mode      // Calculation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeManagementAssets(
       uint        mode      // Calculation mode
       )

### Parameters

**mode**  
[in] Fund management fee calculation mode as a value of theIMTConFund::EnFeeAssestsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
