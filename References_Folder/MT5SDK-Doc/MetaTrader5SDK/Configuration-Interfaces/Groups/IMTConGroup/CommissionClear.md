[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CommissionClear

[Previous](CommissionDelete.md) | [Next](CommissionShift.md)

# IMTConGroup::CommissionClear

Clear the list of commission settings.

C++
    
    
    MTAPIRES  IMTConGroup::CommissionClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CommissionClear()

Python (Manager API)
    
    
    MTConGroup.CommissionClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears the entire list of group commission settings.
