[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConFund::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConFund::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method deletes data from all fields ​​and removes all embedded objects.
