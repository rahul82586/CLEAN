[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Clear

[Previous](Assign.md) | [Next](ID.md)

# IMTNews::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTNews::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
