[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Equity

[Previous](Floating.md) | [Next](SOActivation.md)

# IMTAccount::Equity

Get the account equity.

C++
    
    
    double  IMTAccount::Equity()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Equity()

### Return Value

The account equity calculated as a sum of [IMTAccount::Balance](Balance.md), [IMTAccount::Credit](Credit.md) and [IMTAccount::Floating](Floating.md).

# IMTAccount::Equity

Set the account equity.

C++
    
    
    MTAPIRES  IMTAccount::Equity(
       const double  equity      // Equity
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Equity(
       double        equity      // Equity
       )

### Parameters

**equity**  
[in] The account equity.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
