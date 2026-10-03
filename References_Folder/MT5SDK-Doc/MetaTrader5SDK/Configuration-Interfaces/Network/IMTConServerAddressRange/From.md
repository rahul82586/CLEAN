[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAddressRange](../IMTConServerAddressRange.md) / From

[Previous](Clear.md) | [Next](To.md)

# IMTConServerAddressRange::From

Get the beginning of the range of IP addresses.

C++
    
    
    LPCWSTR  IMTConServerAddressRange::From()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServerAddressRange.From()

### Return Value

The beginning of the range of IP addresses.

# IMTConServerAddressRange::From

Set the beginning of the range of IP addresses.

C++
    
    
    MTAPIRES  IMTConServerAddressRange::From(
       LPCWSTR       from      // The beginning of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAddressRange.From(
       string        from      // The beginning of the range
       )

### Parameters

**from**  
[in] The beginning of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
