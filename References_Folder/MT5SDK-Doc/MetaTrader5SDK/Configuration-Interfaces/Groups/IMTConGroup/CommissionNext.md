[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CommissionNext

[Previous](CommissionTotal.md) | [Next](CommissionGet.md)

# IMTConGroup::CommissionNext

Get a commission setting by the index.

C++
    
    
    MTAPIRES  IMTConGroup::CommissionNext(
       const UINT         pos,            // Position of the commission
       IMTConCommission*  commission      // An object of commission setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CommissionNext(
       uint               pos,            // Position of the commission
       CIMTConCommission  commission      // An object of commission setting
       )

Python (Manager API)
    
    
    MTConGroup.CommissionNext(
       pos                # позиция комиссии
       )

### Parameters

**pos**  
[in] Position of a commission in the list, starting with 0.

**commission**  
[out] An object of commission setting. The commission object must first be created using theIMTAdminAPI::GroupCommissionCreateorIMTManagerAPI::GroupCommissionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of a commission with a specified index to the commission object.
