[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Liabilities

[Previous](Assets.md) | [Next](../IMTAccountArray.md)

# IMTAccount::Liabilities

Get the current total amount of liabilities on a trading account.

C++
    
    
    double  IMTAccount::Liabilities()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Liabilities()

### Return Value

The current total amount of liabilities on a trading account.

### Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).

# IMTAccount::Assets

Set the current total amount of liabilities on a trading account.

C++
    
    
    MTAPIRES  IMTAccount::Liabilities(
       const double  liabilities      // Total liabilities
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Liabilities(
       double        liabilities      // Total liabilities
       )

### Parameters

**liabilities**  
[in] The current total amount of liabilities on a trading account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Used in the exchange risk management model ([IMTConGroup::MARGIN_MODE_EXCHANGE_DISCOUNT (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)).
