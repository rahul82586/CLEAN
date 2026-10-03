[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / APIDataClear

[Previous](APIDataUpdate.md) | [Next](APIDataClearAll.md)

# IMTUser::ApiDataClear

Clear all user parameters set by an application.

C++
    
    
    MTAPIRES  IMTUser::ApiDataClear(
       const USHORT  app_id      // Application ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ApiDataClear(
       ushort        app_id      // Application ID
       )

### Parameters

**app_id**  
[in] Application ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all custom parameters of client records set by an application with the ID app_id.
