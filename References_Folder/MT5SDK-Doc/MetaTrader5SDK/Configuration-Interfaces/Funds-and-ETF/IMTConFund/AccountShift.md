[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / AccountShift

[Previous](AccountClear.md) | [Next](AccountTotal.md)

# IMTConFund::AccountShift

Change the position of a manager account in the list.

C++
    
    
    MTAPIRES  IMTConFund::AccountShift(
       const UINT  pos,       // Manager position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.AccountShift(
       uint        pos,       // Manager position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Manager position in the list, starting at 0.

**shift**  
[in] The shift of a manager account relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
