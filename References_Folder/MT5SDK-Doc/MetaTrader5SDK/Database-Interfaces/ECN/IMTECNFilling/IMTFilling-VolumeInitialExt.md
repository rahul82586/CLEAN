[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling VolumeInitialExt

[Previous](IMTFilling-TypeTime.md) | [Next](IMTFilling-VolumeCurrentExt.md)

# IMTECNFilling::VolumeInitialExt

Get the initial volume of the request created in the ECN for the filling of the client order.

C++
    
    
    UINT64  IMTECNFilling::VolumeInitialExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNFilling.VolumeInitialExt()

### Return Value

The initial volume of the request created in the ECN for the filling of the client order. The value is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

# IMTECNFilling::VolumeInitialExt

Set the initial volume of the request created in the ECN for the filling of the client order.

C++
    
    
    MTAPIRES  IMTECNFilling::VolumeInitialExt(
       const UINT64  volume     // volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.VolumeInitialExt(
       ulong         volume     // volume
       )

### Parameters

**volume**  
[in] The initial volume of the request created in the ECN for the filling of the client order. The value is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
