[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CommissionAdd

[Previous](LimitPositions.md) | [Next](CommissionUpdate.md)

# IMTConGroup::CommissionAdd

Add a commission setting.

C++
    
    
    MTAPIRES  IMTConGroup::CommissionAdd(
       IMTConCommission*  commission      // An object of commission setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CommissionAdd(
       CIMTConCommission  commission      // An object of commission setting
       )

Python (Manager API)
    
    
    MTConGroup.CommissionAdd(
       commission         # An object of commission setting
       )

### Parameters

**commission**  
[in] An object of commission setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
