[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / ModificationFlags

[Previous](MarketLast.md) | [Next](../IMTDealArray.md)

# IMTDeal::ModificationFlags

Gets deal modification flags. The flags allow you to keep track of whether a deal has been modified manually by the administrator, manager or API.

C++
    
    
    UINT  IMTDeal::ModificationFlags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDeal.ModificationFlags()

### Return Value

A value of the [IMTDeal::EnTradeModifyFlags (#entrademodifyflags)](Enumerations.md#entrademodifyflags) enumeration.

### Note

Deals that close a position or part of it inherit its modification flags. After closing, no separate entry about the position remains in the database. To prevent the information about modification from being lost, flags are copied to the deal that closes his position. At the same time, the additional EnTradeModifyFlags::MODIFY_FLAGS_POSITION modification flag is set for the deal 
