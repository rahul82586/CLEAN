[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / ApiDataClear

[Previous](ApiDataGet.md) | [Next](ApiDataClearAll.md)

# IMTOrder::ApiDataClear

Clear all custom parameters of orders set by an application.

C++
    
    
    MTAPIRES  IMTOrder::ApiDataClear(
       const USHORT  app_id      // Application ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ApiDataClear(
       ushort        app_id      // Application ID
       )

### Parameters

**app_id**  
[in] Application ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all custom parameters of trade orders set by an application with the ID app_id.
