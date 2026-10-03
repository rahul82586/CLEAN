[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / TierClear

[Previous](TierDelete.md) | [Next](TierShift.md)

# IMTConCommission::TierClear

Clear the list of commission ranges.

C++
    
    
    MTAPIRES  IMTConCommission::TierClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.TierClear()

Python (Manager API)
    
    
    MTConCommission.TierClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of commission configuration ranges.
