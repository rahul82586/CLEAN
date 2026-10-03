[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Clear

[Previous](Assign.md) | [Next](Login.md)

# IMTAccount::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTAccount::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
