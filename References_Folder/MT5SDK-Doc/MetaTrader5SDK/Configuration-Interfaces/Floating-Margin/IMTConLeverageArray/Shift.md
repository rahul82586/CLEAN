[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTConLeverageArray::Shift

Change the position of a floating margin configuration in the array.

C++
    
    
    MTAPIRES  IMTConLeverageArray::Shift(
       const UINT  pos,       // Configuration position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.Shift(
       uint        pos,       // Position configuration
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the configuration in the array, starting from 0.

**shift**  
[in] Configuration shift relative to its current position. Negative value indicates a shift towards the beginning of the array, while a positive value indicates a shift towards the end.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
