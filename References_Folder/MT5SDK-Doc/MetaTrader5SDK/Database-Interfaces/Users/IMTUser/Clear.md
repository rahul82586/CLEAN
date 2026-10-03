[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Clear

[Previous](Assign.md) | [Next](Login.md)

# IMTUser::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTUser::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
