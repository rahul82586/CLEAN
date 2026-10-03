[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Storage

[Previous](Profit.md) | [Next](RateProfit.md)

# IMTPosition::Storage

Get the swap size for a position.

C++
    
    
    double  IMTPosition::Storage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.Storage()

### Return Value

The swap value of a position in the account deposit currency.

# IMTPosition::Storage

Set the swap size for a position.

C++
    
    
    MTAPIRES  IMTPosition::Storage(
       const double  storage      // Swap
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Storage(
       double        storage      // Swap
       )

### Parameters

**storage**  
[in] The swap value of a position in the account deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The swap of each open position is accumulated in the IMTPosition::Storage field. The total amount of swaps of all positions on the account is stored in [IMTAccount:Storage](../../Accounts/IMTAccount/Storage.md). The swap is reflected on the balance after position closure. In this case, the value of IMTPosition::Storage is reset, and the appropriate amount of fixed swap is deducted from the value of IMTAccount::Storage. If only a part of the position is closed, the proportionate share of the swap is reflected on the balance.
