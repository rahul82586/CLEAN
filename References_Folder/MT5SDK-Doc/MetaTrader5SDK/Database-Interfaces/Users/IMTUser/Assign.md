[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTUser::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTUser::Assign(
       const IMTUser*  user      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Assign(
       CIMTUser        user      // Source object
       )

### Parameters

**user**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
