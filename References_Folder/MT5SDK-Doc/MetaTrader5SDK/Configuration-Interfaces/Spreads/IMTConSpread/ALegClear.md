[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / ALegClear

[Previous](ALegDelete.md) | [Next](ALegShift.md)

# IMTConSpread::ALegClear

Clear the list of all spread A legs.

C++
    
    
    MTAPIRES  IMTConSpread::ALegClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.ALegClear()

Python (Manager API)
    
    
    MTConSpread.ALegClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
