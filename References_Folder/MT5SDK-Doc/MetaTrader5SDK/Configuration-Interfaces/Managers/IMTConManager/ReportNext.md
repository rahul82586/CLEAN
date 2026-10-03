[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / ReportNext

[Previous](ReportTotal.md) | [Next](../IMTConManagerAccess.md)

# IMTConManager::ReportNext

Get a manager's report access permission based on the permission position in the list.

C++
    
    
    MTAPIRES  IMTConManager::ReportNext(
       const UINT            pos,        // Position of the access permission
       IMTConManagerReport*  report      // Access permission object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.ReportNext(
       uint                  pos,        // Position of the access permission
       CIMTConManagerReport  report      // Access permission object
       )

Python (Manager API)
    
    
    MTConManager.ReportNext(
       pos                   # Position of the access permission
       )
    
    
    MTConManager.ReportGet()

### Parameters

**pos**  
[in] Position of the access permission in the list, starting from 0.

**report**  
[out] Access permission object. The 'access' object must be pre-created using theIMTAdminAPI::ManagerReportCreate,IMTManagerAPI::ManagerReportCreate,IMTServerAPI::ManagerReportCreateorIMTReportAPI::ManagerReportCreatemethod.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.
