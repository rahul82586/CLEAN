[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / ReportUpdate

[Previous](ReportAdd.md) | [Next](ReportDelete.md)

# IMTConManager::ReportUpdate

Update a report access permission for a manager.

C++
    
    
    MTAPIRES  IMTConManager::ReportUpdate(
       const UINT                  pos,        // Position of the access permission
       const IMTConManagerReport*  report      // Access permission object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.ReportUpdate(
       uint                        pos,        // Position of the access permission
       CIMTConManagerReport        report      // Access permission object
       )

Python (Manager API)
    
    
    MTConManager.ReportUpdate(
       pos,                        # Position of the access permission
       report                      # Access permission object
       )
    
    
    MTConManager.ReportSet(
       report_list                 # A list of permissions
       )

### Parameters

**pos**  
[in] Position of a permission in the list, starting with 0.

**access**  
[in] An object of the access permission.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.
