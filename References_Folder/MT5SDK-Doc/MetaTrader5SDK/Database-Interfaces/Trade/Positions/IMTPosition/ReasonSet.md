[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ReasonSet

[Previous](Reason.md) | [Next](../IMTPositionArray.md)

# IMTPosition::ReasonSet

Set the reason for opening a position.

C++
    
    
    MTAPIRES  IMTPosition::ReasonSet(
       const UINT  reason    // reason
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ReasonSet(
       uint        reason    // reason
       )

### Parameters

**reason**  
[in] Reason for opening a position. TheIMTPosition::EnPositionReasonenumeration is used to pass it.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Do not change a reason for opening a position without a serious cause to keep the data integrity intact.
