[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling VolumeCurrentExt

[Previous](IMTHistoryFilling-VolumeInitialExt.md) | [Next](IMTHistoryFilling-Price.md)

# IMTECNHistoryFilling::VolumeCurrentExt

Get the current filled volume of the request created in the ECN for the filling of the client order.

C++
    
    
    UINT64  IMTECNHistoryFilling::VolumeCurrentExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryFilling.VolumeCurrentExt()

### Return Value

The current filled volume of the request created in the ECN for the filling of the client order. The value is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

# IMTECNHistoryFilling::VolumeCurrentExt

Set the current filled volume of the request created in the ECN for the filling of the client order.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::VolumeCurrentExt(
       const UINT64  volume     // volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.VolumeCurrentExt(
       ulong         volume     // volume
       )

### Parameters

**volume**  
[in] The current filled volume of the request created in the ECN for the filling of the client order. The value is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
