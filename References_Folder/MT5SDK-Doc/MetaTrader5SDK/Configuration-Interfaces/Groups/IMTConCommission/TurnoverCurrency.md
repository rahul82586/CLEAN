[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / TurnoverCurrency

[Previous](ReasonFlags.md) | [Next](TierAdd.md)

# IMTConCommission::TurnoverCurrency

Get the currency, in which the money turnover is calculated.

C++
    
    
    LPCWSTR  IMTConCommission::TurnoverCurrency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommission.TurnoverCurrency()

Python (Manager API)
    
    
    MTConCommission.TurnoverCurrency

### Return Value

If successful, it returns a pointer to a string with the currency name. Otherwise, it returns NULL.

### Note

This property is used when calculating turnover in money for commission levels ([IMTConCommission::COMM_RANGE_TURNOVER_MONEY (#encommrangemode)](Enumerations.md#encommrangemode)) and when calculating commission as percent of deal value ([IMTConCommTier::IMTConCommTier (#encommissionmode)](../IMTConCommTier/Enumerations.md#encommissionmode)). The group deposit currency is used by default (if no other currency is specified).

# IMTConCommission::TurnoverCurrency

Set the currency, in which the money turnover is calculated.

C++
    
    
    MTAPIRES  IMTConCommission::TurnoverCurrency(
       LPCWSTR  currency   // currency name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.TurnoverCurrency(
       string   currency   // currency name
       )

Python (Manager API)
    
    
    MTConCommission.TurnoverCurrency

### Parameters

**currency**  
[in] Three-letter abbreviation for the currency, for example, USD, EUR, etc.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This property is used when calculating turnover in money for commission levels ([IMTConCommission::COMM_RANGE_TURNOVER_MONEY (#encommrangemode)](Enumerations.md#encommrangemode)) and when calculating commission as percent of deal value ([IMTConCommTier::IMTConCommTier (#encommissionmode)](../IMTConCommTier/Enumerations.md#encommissionmode)). The group deposit currency is used by default (if no other currency is specified).
