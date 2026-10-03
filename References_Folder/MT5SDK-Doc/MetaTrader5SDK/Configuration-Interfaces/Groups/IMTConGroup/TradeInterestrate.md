[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / TradeInterestrate

[Previous](TradeTransferMode.md) | [Next](TradeVirtualCredit.md)

# IMTConGroup::TradeInterestrate

Get the annual interest rate on deposits of the group accounts.

C++
    
    
    double  IMTConGroup::TradeInterestrate()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroup.TradeInterestrate()

Python (Manager API)
    
    
    MTConGroup.TradeInterestrate

### Return Value

The annual interest rate on deposits of the group accounts.

# IMTConGroup::TradeInterestrate

Set the annual interest rate on deposits of the group accounts.

C++
    
    
    MTAPIRES  IMTConGroup::TradeInterestrate(
       const double  rate      // Annual interest rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.TradeInterestrate(
       double        rate      // Annual interest rate
       )

Python (Manager API)
    
    
    MTConGroup.TradeInterestrate

### Parameters

**rate**  
[in] The annual interest rate on deposits of the group accounts.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
