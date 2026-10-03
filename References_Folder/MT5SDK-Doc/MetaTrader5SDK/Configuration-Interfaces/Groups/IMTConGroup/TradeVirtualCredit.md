[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / TradeVirtualCredit

[Previous](TradeInterestrate.md) | [Next](MarginFreeMode.md)

# IMTConGroup::TradeVirtualCredit

Get the amount of additional funds that a brokerage company can provide to a client for opening a position with a volume larger than allowed by the client's current funds.

C++
    
    
    double  IMTConGroup::TradeVirtualCredit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroup.TradeVirtualCredit()

Python (Manager API)
    
    
    MTConGroup.TradeVirtualCredit

### Return Value

The amount of additional funds for opening a position with a volume larger than allowed by the client's current funds.

# IMTConGroup::TradeVirtualCredit

Set the amount of additional funds that a brokerage company can provide to a client for opening a position with a volume larger than allowed by the client's current funds.

C++
    
    
    MTAPIRES  IMTConGroup::TradeVirtualCredit(
       const double  credit      // A virtual credit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.TradeVirtualCredit(
       double        credit      // A virtual credit
       )

Python (Manager API)
    
    
    MTConGroup.TradeVirtualCredit

### Parameters

**credit**  
[in] The amount of additional funds for opening a position with a volume larger than allowed by the client's current funds.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
