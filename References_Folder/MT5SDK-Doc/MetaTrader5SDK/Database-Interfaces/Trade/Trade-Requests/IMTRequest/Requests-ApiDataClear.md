[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ApiDataClear

[Previous](Requests-APIDataRawMax.md) | [Next](Requests-ApiDataClearAll.md)

# IMTRequest::ApiDataClear

Clear all custom parameters of requests set by an application.

C++
    
    
    MTAPIRES  IMTRequest::ApiDataClear(
       const USHORT  app_id      // Application identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.ApiDataClear(
       ushort        app_id      // Application identifier
       )

### Parameters

**app_id**  
[in] Application ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears all custom parameters of trade requests which were set by an application with the app_id.
