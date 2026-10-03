[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / IESlipLosing

[Previous](IESlipProfitDefault.md) | [Next](IESlipLosingDefault.md)

# IMTConGroupSymbol::IESlipLosing

Get the maximum allowed slippage in the loss direction during instant execution.

C++
    
    
    UINT  IMTConGroupSymbol::IESlipLosing()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroupSymbol.IESlipLosing()

Python (Manager API)
    
    
    MTConGroupSymbol.IESlipLosing

### Return Value

The maximum allowed slippage in the direction of a loss for a client during instant execution. If this limit is exceeded, the client is returned a requote.

### Note

This method operates with individual symbol settings for groups.

# IMTConGroupSymbol::IESlipLosing

Set the maximum allowed slippage in the loss direction during instant execution.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::IESlipLosing(
       const UINT  slippage      // Amount of slippage
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.IESlipLosing(
       uint        slippage      // Amount of slippage
       )

Python (Manager API)
    
    
    MTConGroupSymbol.IESlipLosing

### Parameters

**slippage**  
[in] The maximum allowed slippage in the direction of a loss for a client during instant execution. If this limit is exceeded, the client is returned a requote.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method operates with individual symbol settings for groups.
