[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTDailyArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTDailyArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
