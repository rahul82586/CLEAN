[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDailyArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTDailyArray::Assign(
       const IMTDailyArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDailyArray.Assign(
       CIMTDailyArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
