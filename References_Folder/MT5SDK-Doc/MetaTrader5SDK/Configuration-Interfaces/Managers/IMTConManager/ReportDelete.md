[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / ReportDelete

[Previous](ReportUpdate.md) | [Next](ReportShift.md)

# IMTConManager::ReportDelete

Delete a report access permission for a manager.

C++
    
    
    MTAPIRES  IMTConManager::ReportDelete(
       const UINT  pos      // Position of the access permission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.ReportDelete(
       uint        pos      // Position of the access permission
       )

Python (Manager API)
    
    
    MTConManager.ReportDelete(
       pos         # Position of the access permission
       )

### Parameters

**pos**  
[in] Permission position in the list, starting from 0.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.
