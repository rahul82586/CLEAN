[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerRange](../IMTConServerRange.md) / To

[Previous](From.md) | [Next](UsedFrom.md)

# IMTConServerRange::To

Get the end of the range of accounts, orders or deals of a trade server.

C++
    
    
    UINT64  IMTConServerRange::To()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConServerRange.To()

Python (Manager API)
    
    
    MTConServerRange.To

### Return Value

The end of the range of accounts, orders or deals of a trade server.

# IMTConServerRange::To

Set the end of the range of accounts, orders or deals of a trade server.

C++
    
    
    MTAPIRES  IMTConServerRange::To(
       const UINT64  to      // The end of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerRange.To(
       ulong         to      // The end of the range
       )

Python (Manager API)
    
    
    MTConServerRange.To

### Parameters

**to**  
[in] The end of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
