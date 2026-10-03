[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / Ratio

[Previous](TimeTo.md) | [Next](RatioDbl.md)

# IMTConSpreadLeg::Ratio

Getting symbol volume ratio (weight) in a spread leg.

C++
    
    
    UINT64  IMTConSpreadLeg::Ratio()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSpreadLeg.Ratio()

Python (Manager API)
    
    
    MTConSpreadLeg.Ratio

### Return Value

Symbol volume ratio (weight) in a spread leg.

# IMTConSpreadLeg::Ratio

Setting symbol volume ratio (weight) in a spread leg.

C++
    
    
    MTAPIRES  IMTConSpreadLeg::Ratio(
       const UINT64  ratio      // volume ratio
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpreadLeg.Ratio(
       ulong         ratio      // volume ratio
       )

Python (Manager API)
    
    
    MTConSpreadLeg.Ratio

### Parameters

**open**  
[in] Symbol volume ratio (weight) in a spread leg.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Several symbols can be configured for each leg. A volume ratio at this spread leg can be specified for each of them.

  * leg A consists of GAZR-9.12 and GAZR-3.13 symbols having the ratios of 1 and 2 respectively
  * leg B consists of GAZR-6.13 having the ratio of 1.


