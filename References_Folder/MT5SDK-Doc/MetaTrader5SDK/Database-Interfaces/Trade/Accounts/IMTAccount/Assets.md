[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Assets

[Previous](BlockedProfit.md) | [Next](Liabilities.md)

# IMTAccount::Assets

Get the current total amount of assets on a trading account.

C++
    
    
    double  IMTAccount::Assets()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Assets()

### Return Value

The current total amount of assets on a trading account.

### Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).

# IMTAccount::Assets

Set the current total amount of assets on a trading account.

C++
    
    
    MTAPIRES  IMTAccount::Assets(
       const double  assets      // Total assets
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Assets(
       double        assets      // Total assets
       )

### Parameters

**assets**  
[in] The current total amount of assets on a trading account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).
