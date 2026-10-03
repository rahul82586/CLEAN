[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / InterestRate

[Previous](Credit.md) | [Next](CommissionDaily.md)

# IMTDaily::InterestRate

Get the amount of accumulated annual interest.

C++
    
    
    double  IMTDaily::InterestRate()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.InterestRate()

### Return Value

The amount of accumulated annual interest.

### Note

Annual interest is calculated every day in accordance with the group settings ([IMTConGroup::TradeInterestrate](../../../../Configuration-Interfaces/Groups/IMTConGroup/TradeInterestrate.md)) and is accumulated in a separate account field. At the end of each month, the accumulated amount is credited to the account balance using an [IMTDeal::DEAL_INTERESTRATE (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction) operation, and the InterestRate value is reset to zero.

# IMTDaily::InterestRate

Set the amount of accumulated annual interest.

C++
    
    
    MTAPIRES  IMTDaily::InterestRate(
       const double  credit      // Amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.InterestRate(
       double        credit      // Amount
       )

### Parameters

**credit**  
[in] The amount of accumulated annual interest.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
