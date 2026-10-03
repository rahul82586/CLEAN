[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CommissionUpdate

[Previous](CommissionAdd.md) | [Next](CommissionDelete.md)

# IMTConGroup::CommissionUpdate

Change a commission setting at the specified position.

C++
    
    
    MTAPIRES  IMTConGroup::CommissionUpdate(
       const UINT               pos,            // Position of the commission
       const IMTConCommission*  commission      // An object of commission setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CommissionUpdate(
       uint                     pos,            // Position of the commission
       CIMTConCommission        commission      // An object of commission setting
       )

Python (Manager API)
    
    
    MTConGroup.CommissionUpdate(
       pos,                     # Position of the commission
       commission               # An object of commission setting
       )
    
    
    MTConGroup.CommissionSet(
       comm_list                # A list of objects
       )

### Parameters

**pos**  
[in] Position of a commission in the list, starting with 0.

**commission**  
[in] An object of commission setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
