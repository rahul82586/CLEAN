[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / BlockedProfit

[Previous](BlockedCommission.md) | [Next](Assets.md)

# IMTAccount::BlockedProfit

Get the amount of intraday profit locked on the account.

C++
    
    
    double  IMTAccount::BlockedProfit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.BlockedProfit()

### Return Value

The amount of intraday profit locked on the account.

### Note

For each group of clients, you can choose one of two modes of calculation of the intraday returns in the free margin. In the [IMTConGroup::FREE_MARGIN_PROFIT_LOSS (#enmarginfreeprofitflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginfreeprofitflags)

# IMTAccount::BlockedProfit

Set the margin amount on an account at the time of reaching the Stop Out level.

C++
    
    
    MTAPIRES  IMTAccount::BlockedProfit(
       const double  profit      // The amount of locked profit
       )

.NET (Gateway/Manager API)
    
    
    MTAPIRES  CIMTAccount.BlockedProfit(
       double        profit      // The amount of locked profit
       )

### Parameters

**profit**  
[in] The amount of intraday profit locked on the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

For each group of clients, you can choose one of two modes of calculation of the intraday returns in the free margin. In the [IMTConGroup::FREE_MARGIN_PROFIT_LOSS (#enmarginfreeprofitflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginfreeprofitflags)
