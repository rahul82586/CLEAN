[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests APIDataRawSet

[Previous](Requests-APIDataNext.md) | [Next](Requests-APIDataRawGet.md)

# IMTExecution::APIDataRawSet

Set custom parameters for a trade execution as raw data (memory fragment).

C++
    
    
    MTAPIREST  IMTExecution::APIDataRawSet(
       const void*    data,       // Data
       const UINT     datalen     // Data size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.APIDataRawSet(
       byte[]         data        // Data
       )

### Parameters

**data**  
[in] A pointer to the data.

**datalen**  
[in] Data size.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The amount of recorded data must not exceed the [IMTExecution::APIDataRawMax](Requests-APIDataRawMax.md) value.
