[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTDealArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTDealArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
