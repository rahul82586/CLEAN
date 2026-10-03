[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTAccountArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTAccountArray::Assign(
       const IMTAccountArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.Assign(
       CIMTAccountArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
