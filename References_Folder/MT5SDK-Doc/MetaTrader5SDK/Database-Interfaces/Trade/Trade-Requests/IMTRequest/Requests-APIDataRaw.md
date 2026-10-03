[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests APIDataRaw

[Previous](Requests-APIDataNext.md) | [Next](Requests-APIDataRawMax.md)

# IMTRequest::APIDataRaw

Get custom parameters of a trade request as raw data (memory fragment).

C++
    
    
    LPVOID  IMTRequest::APIDataRaw()  const

.NET (Gateway/Manager API)
    
    
    byte[]  CIMTRequest.APIDataRaw()

### Return Value

A pointer to the value.

### Note

Use the standard memcpy function to record raw data. The amount of recorded data must not exceed the [IMTRequest::APIDataRawMax](Requests-APIDataRawMax.md) value.
