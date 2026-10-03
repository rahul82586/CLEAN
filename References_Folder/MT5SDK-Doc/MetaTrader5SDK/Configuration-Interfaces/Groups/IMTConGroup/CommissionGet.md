[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CommissionGet

[Previous](CommissionNext.md) | [Next](SymbolAdd.md)

# IMTConGroup::CommissionGet

Gets a commission setting with the specified name.

C++
    
    
    MTAPIRES  IMTConGroup::CommissionGet(
       LPCWSTR            name,           // Commission name
       IMTConCommission*  commission      // An object of commission setting
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CommissionGet(
       string             name,           // Commission name
       CIMTConCommission  commission      // An object of commission setting
       )

Python (Manager API)
    
    
    MTConGroup.CommissionGet(
       name               # Commission name
       )
    
    
    MTConGroup.CommissionGet()

### Parameters

**name**  
[in] The name of a commission configuration.

**commission**  
[out] An object of commission setting. The commission object must first be created using theIMTAdminAPI::GroupCommissionCreateorIMTManagerAPI::GroupCommissionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of a commission with a specified name to the commission object.
