[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupUpdate

[Previous](GroupUnsubscribe.md) | [Next](GroupUpdateBatch.md)

# IMTManagerAPI::GroupUpdate

Update group configuration.

C++
    
    
    MTAPIRES  IMTManagerAPI::GroupUpdate(
       IMTConGroup*  group      // Group configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.GroupUpdate(
       CIMTConGroup  group      // Group configuration object
       )

Python
    
    
    ManagerAPI.GroupUpdate(
       group         # Group configuration object
       )

### Parameters

**group**  
[in] An object of group configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

A configuration can only be added or updated from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.

  * [IMTConGroup::MarginCall](../../../../Configuration-Interfaces/Groups/IMTConGroup/MarginCall.md)
  * [IMTConGroup::MarginStopOut](../../../../Configuration-Interfaces/Groups/IMTConGroup/MarginStopOut.md)
  * [IMTConGroup::MarginSOMode](../../../../Configuration-Interfaces/Groups/IMTConGroup/MarginSOMode.md)
  * [IMTConGroup::EnTradeFlags::TRADEFLAGS_SO_COMPENSATION (#entradeflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#entradeflags)
  * [IMTConGroup::Commission*](../../../../Configuration-Interfaces/Groups/IMTConGroup/CommissionAdd.md):
  * [IMTConGroup::Symbol*](../../../../Configuration-Interfaces/Groups/IMTConGroup/SymbolAdd.md):


  * [IMTConGroupSymbol::Path](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/Path.md)
  * [IMTConGroupSymbol::SpreadDiff](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SpreadDiff.md)
  * [IMTConGroupSymbol::SpreadDiffBalance](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SpreadDiffBalance.md)
  * [IMTConGroupSymbol::MarginInitial](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginInitial.md)
  * [IMTConGroupSymbol::MaringMaintenance](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginMaintenance.md)
  * [IMTConGroupSymbol::MarginHedged](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginHedged.md)
  * [IMTConGroupSymbol::MarginHedged](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginHedged.md)
  * [IMTConGroupSymbol::MarginFlags](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginFlags.md)
  * [IMTConGroupSymbol::MarginRateInitial](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginRateInitial.md)
  * [IMTConGroupSymbol::MarginRateMaintenance](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginRateMaintenance.md)
  * [IMTConGroupSymbol::MarginRateLiquidity](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginRateLiquidity.md)
  * [IMTConGroupSymbol::MarginRateCurrency](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/MarginRateCurrency.md)
  * [IMTConGroupSymbol::SwapMode](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SwapMode.md)
  * [IMTConGroupSymbol::SwapLong](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SwapLong.md)
  * [IMTConGroupSymbol::SwapShort](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SwapShort.md)
  * [IMTConGroupSymbol::Swap3Day](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/Swap3Day.md)


