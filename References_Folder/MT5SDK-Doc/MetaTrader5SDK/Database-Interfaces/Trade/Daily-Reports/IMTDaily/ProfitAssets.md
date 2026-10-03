[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / ProfitAssets

[Previous](ProfitEquity.md) | [Next](ProfitLiabilities.md)

# IMTDaily::ProfitAssets

Get the current amount of client assets in a daily report.

C++
    
    
    double  IMTDaily::ProfitAssets()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDaily.ProfitAssets()

### Return Value

The current amount of client assets in a daily report.

### Further Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).

# IMTDaily::ProfitAssets

Set the current total amount of assets on a trading account.

C++
    
    
    MTAPIRES  IMTDaily::ProfitAssets(
       const double  assets      // Amount of assets
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.ProfitAssets(
       double        assets      // Amount of assets
       )

### Program Parameters

**assets**  
[in] The current amount of client assets in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Further Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).
