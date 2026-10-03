[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon GroupShift

[Previous](IMTCon-GroupClear.md) | [Next](IMTCon-GroupTotal.md)

# IMTConKYC::GroupShift

Shift a group in the KYC provider settings.

C++
    
    
    MTAPIRES  IMTConKYC::GroupShift(
       const UINT  pos,       // Group position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.GroupShift(
       uint        pos,       // Group position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Group position in the list, starting from 0.

**shift**  
[in] Shift of a group relative to its current position. A negative value means shift towards the top of the list; a positive value shifts the item towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
