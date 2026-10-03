[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / ProfitLiabilities

[Previous](ProfitAssets.md) | [Next](DailyProfit.md)

# IMTDaily::ProfitLiabilities

Get the current amount of client liabilities in a daily report.

C++
    
    
    double  IMTDaily::ProfitLiabilities()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.ProfitLiabilities()

### Return Value

The current amount of client liabilities in a daily report.

### Further Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).

# IMTDaily::ProfitLiabilities

Set the current amount of client liabilities in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::ProfitLiabilities(
       const double  liabilities      // Amount of liabilities
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.ProfitLiabilities(
       double        liabilities      // Amount of liabilities
       )

### Program Parameters

**liabilities**  
[in] The current amount of client liabilities in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Further Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).
