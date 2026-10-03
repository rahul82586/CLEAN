[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / ApiDataClear

[Previous](ApiDataGet.md) | [Next](ApiDataClearAll.md)

# IMTDeal::ApiDataClear

Clears all custom parameters of deals set by an application.

C++
    
    
    MTAPIRES  IMTDeal::ApiDataClear(
       const USHORT  app_id      // Application ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.ApiDataClear(
       ushort        app_id      // Application ID
       )

### Parameters

**app_id**  
[in] Application ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all custom parameters of deals set by an application with the app_id ID.
