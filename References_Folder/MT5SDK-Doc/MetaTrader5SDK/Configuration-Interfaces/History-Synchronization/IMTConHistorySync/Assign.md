[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySync](../IMTConHistorySync.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConHistorySync::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConHistorySync::Assign(
       const IMTConHistorySync*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHistorySync.Assign(
       CIMTConHistorySync        param      // Source object
       )

### Parameters

**param**  
Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
