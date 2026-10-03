[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTPosition::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTPosition::Assign(
       const IMTPosition*  position      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Assign(
       CIMTPosition        position      // Source object
       )

### Parameters

**position**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
