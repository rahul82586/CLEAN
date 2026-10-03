[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ExpertID

[Previous](RateMargin.md) | [Next](ExpertPositionID.md)

# IMTPosition::ExpertID

Get the ID of the Expert Advisor that has opened the position.

C++
    
    
    UINT64  IMTPosition::ExpertID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTPosition.ExpertID()

### Return Value

The ID of the Expert Advisor that has opened the position. If a position has been opened manually, 0 is returned.

### Note

This identifier is set by the Expert Advisor.

# IMTPosition::ExpertID

Set the ID of the Expert Advisor that has opened the position.

C++
    
    
    MTAPIRES  IMTPosition::ExpertID(
       const UINT64  id      // Expert Advisor ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ExpertID(
       ulong         id      // Expert Advisor ID
       )

### Parameters

**id**  
[in] The ID of the Expert Advisor that has opened the position. The 0 value means that the deal was executed manually.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
