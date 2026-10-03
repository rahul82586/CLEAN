[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / ProfitRaw

[Previous](ApiDataClearAll.md) | [Next](PricePosition.md)

# IMTDeal::ProfitRaw

Gets the value of profit/loss resulting from the deal execution. The profit/loss is expressed in the [profit currency of the symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyProfit.md), for which a deal is executed.

C++
    
    
    double  IMTDeal::ProfitRaw()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.ProfitRaw()

### Return Value

The profit/loss value in the symbol profit currency.

### Note

The profit value can only be obtained for deals of type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)

# IMTDeal::ProfitRaw

Sets the value of profit/loss resulting from the deal execution. The profit/loss is expressed in the [profit currency of the symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyProfit.md), for which a deal is executed.

C++
    
    
    MTAPIRES  IMTDeal::ProfitRaw(
       const double  profit      // The profit/loss value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.ProfitRaw(
       double        profit      // The profit/loss value
       )

### Parameters

**profit**  
[in] The profit/loss value in the profit currency of the symbol, for which a deal is executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The profit value can only be set for deals of type [IMTDeal::ENTRY_OUT (#endealentry)](Enumerations.md#endealentry)[IMTDeal::ENTRY_INOUT (#endealentry)](Enumerations.md#endealentry)
