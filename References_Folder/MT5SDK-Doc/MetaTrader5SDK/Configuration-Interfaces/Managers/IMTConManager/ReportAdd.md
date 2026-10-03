[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / ReportAdd

[Previous](AccessNext.md) | [Next](ReportUpdate.md)

# IMTConManager::ReportAdd

Create a report access permission for a manager.

C++
    
    
    MTAPIRES  IMTConManager::ReportAdd(
       IMTConManagerReport*  report      // Access permission object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.ReportAdd(
       CIMTConManagerReport  report      // Access permission object
       )

Python (Manager API)
    
    
    MTConManager.ReportAdd(
       report                # Access permission object
       )

### Parameters

**report**  
[in] An object of a report access permissionIMTConManagerReport.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.
