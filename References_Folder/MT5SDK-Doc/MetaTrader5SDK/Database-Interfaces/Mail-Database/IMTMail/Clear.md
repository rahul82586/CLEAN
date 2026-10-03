[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / Clear

[Previous](Assign.md) | [Next](ID.md)

# IMTMail::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTMail::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
