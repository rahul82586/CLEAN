[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Clear

[Previous](Assign.md) | [Next](Print.md)

# IMTDeal::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTDeal::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
