[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Storage

[Previous](Profit.md) | [Next](Commission.md)

# IMTAccount::Storage

Get the current size of swaps charged for open positions on the account.

C++
    
    
    double  IMTAccount::Storage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Storage()

### Return Value

The current size of swaps charged for open positions on the account.

# IMTAccount::Storage

Set the current size of swaps charged for open positions on the account.

C++
    
    
    MTAPIRES  IMTAccount::Storage(
       const double  storage      // Swaps
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Storage(
       double        storage      // Swaps
       )

### Parameters

**storage**  
[in] The size of swaps charged for open positions on the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The swap of each open position is accumulated in the [IMTPosition::Storage](../../Positions/IMTPosition/Storage.md) field. The total amount of swaps of all positions on the account is stored in IMTAccount::Storage. The swap is reflected on the balance after position closure. In this case, the value of IMTPosition::Storage is reset, and the appropriate amount of fixed swap is deducted from the value of IMTAccount::Storage. If only a part of the position is closed, the proportionate share of the swap is reflected on the balance.
