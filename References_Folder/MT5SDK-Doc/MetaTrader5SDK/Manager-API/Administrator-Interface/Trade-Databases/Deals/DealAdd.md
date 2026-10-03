[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealAdd

[Previous](DealRequestPage.md) | [Next](DealAddBatch.md)

# IMTAdminAPI::DealAdd

Add a deal to the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealAdd(
       IMTDeal*  deal      // deal object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealAdd(
       CIMTDeal  deal      // deal object
       )

Python
    
    
    AdminAPI.DealAdd(
       deal      # deal object
       )

### Parameters

**deal**  
[in] An object of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

A deal can only be added to the database of the server, to which the application is connected.

The ticket of the deal you are adding ([IMTDeal::DealSet](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DealSet.md)) must fall within the deals range on the trading server ([IMTConServerTrade::DealsRange*](../../../../Configuration-Interfaces/Network/IMTConServerTrade/DealsRangeAdd.md)), and it must be greater than the last used ticket. 

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)
  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


