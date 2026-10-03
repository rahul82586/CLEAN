[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolAddPreliminary

[Previous](SymbolUnsubscribe.md) | [Next](SymbolUpdate.md)

# IMTGatewayAPI::SymbolAddPreliminary

Add or update a preliminary configuration of a symbol.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SymbolAddPreliminary(
       IMTConSymbol*  symbol      // An object of the symbol configuration
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SymbolAddPreliminary(
       CIMTConSymbol  symbol      // An object of the symbol configuration
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

## Symbol Adding Features

Process of the importing the symbols into the trading platform using this method has several peculiarities:

  * When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated (the list of parameters that can be updated is given below), otherwise a new entry is added. A key field for comparison is the name of the symbol [IMTConSymbol::Symbol()](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConSymbolSink::OnSymbolUpdate](../../../../Configuration-Interfaces/Symbols/IMTConSymbolSink/OnSymbolUpdate.md) notification method is not called.
  * All symbols are added to the \Preliminary\ symbols subgroup. For example, if the path 'Metals\Gold' ([IMTConSymol::Path](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Path.md)) is indicated in the added symbol parameter, the symbol will be added to the \Preliminary\Metals\Gold group.
  * All symbols are imported with the trading possibility ([IMTConSymbol::TradeMode](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TradeMode.md)) turned off.



Therefore, an administrator has to manually place a symbol into an appropriate group after the import and allow trading for it.

> For full control over symbols, use [IMTGatewayAPI::SymbolUpdate](SymbolUpdate.md) method. It allows adding symbols to any group and changing any symbol parameters.

The below list includes all the symbol parameters that can be changed using this method. Other parameters cannot be modified.

  * [ISIN](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ISIN.md)
  * [Description](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Description.md)
  * [International](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/International.md)
  * [Basis](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Basis.md)
  * [Source](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Source.md)
  * [Page](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Page.md)
  * [CurrencyBase](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyBase.md)
  * [CurrencyProfit](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyProfit.md)
  * [CurrencyMargin](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyMargin.md)
  * [Color](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Color.md)
  * [ColorBackground](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ColorBackground.md)
  * [TickFlags](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TickFlags.md)
  * [TickBookDepth](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TickBookDepth.md)
  * [FilterDiscard](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FilterDiscard.md)
  * [FilterSoft](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FilterSoft.md)
  * [FilterSoftTicks](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FilterSoftTicks.md)
  * [FilterHard](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FilterHard.md)
  * [FilterHardTicks](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FilterHardTicks.md)
  * [TradeFlags](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TradeFlags.md)
  * [Spread](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Spread.md)
  * [SpreadBalance](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadBalance.md)
  * [TickValue](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TickValue.md)
  * [TickSize](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TickSize.md)
  * [ContractSize](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ContractSize.md)
  * [GTCMode](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/GTCMode.md)
  * [CalcMode](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CalcMode.md)
  * [QuotesTimeout](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/QuotesTimeout.md)
  * [PriceSettle](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/PriceSettle.md)
  * [PriceLimitMax](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/PriceLimitMax.md)
  * [PriceLimitMin](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/PriceLimitMin.md)
  * [TimeStart](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TimeStart.md)
  * [TimeExpiration ](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/TimeExpiration.md)
  * [FillFlags](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/FillFlags.md)
  * [ExpirFlags](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExpirFlags.md)
  * [VolumeMin](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/VolumeMin.md)
  * [VolumeMax](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/VolumeMax.md)
  * [VolumeStep](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/VolumeStep.md)
  * [VolumeLimit ](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/VolumeLimit.md)
  * [MarginCheckMode](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginFlags.md)
  * [MarginInitial](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginInitial.md)
  * [MarginMaintenance](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginMaintenance.md)
  * [MarginLong](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginLong.md)
  * [MarginShort](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginShort.md)
  * [MarginLimit](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginLimit.md)
  * [MarginStop](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginStop.md)
  * [MarginStopLimit](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/MarginStopLimit.md)


