[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / TradeTransferMode

[Previous](TradeFlags.md) | [Next](TradeInterestrate.md)

# IMTConGroup::TradeTransferMode

Gets the mode of funds transfer between accounts.

C++
    
    
    UINT  IMTConGroup::TradeTransferMode()  const

.NET (Gateway/Manager API)
    
    
    EnTransferMode  CIMTConGroup.TradeTransferMode()

Python (Manager API)
    
    
    MTConGroup.TradeTransferMode

### Return Value

A value from the [IMTConGroup::EnTransferMode (#entransfermode)](Enumerations.md#entransfermode) enumeration.

# IMTConGroup::TradeTransferMode

Gets the mode of funds transfer between accounts.

C++
    
    
    MTAPIRES  IMTConGroup::TradeTransferMode(
       const UINT      mode  // Funds transfer mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.TradeTransferMode(
       EnTransferMode  mode  // Funds transfer mode
       )

Python (Manager API)
    
    
    MTConGroup.TradeTransferMode

### Parameters

**mode**  
[in] The funds transfer mode can be set using theIMTConGroup::EnTransferModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Notes

The following limitations apply to money transfer between accounts:

  * Funds can be transferred only within the same trading server and only between the accounts of the same type. From a real account funds can be transferred only to another real account, from a demo one - only to demo.
  * The accounts, between which funds are transferred, should use the same deposit currency.
  * The transfer amount should not exceed the current balance and free margin on the account from which money is transferred.


