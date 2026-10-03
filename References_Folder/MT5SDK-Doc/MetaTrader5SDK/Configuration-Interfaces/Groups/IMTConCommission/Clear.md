[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConCommission::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConCommission::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.Clear()

Python (Manager API)
    
    
    bool  MTConCommission.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
