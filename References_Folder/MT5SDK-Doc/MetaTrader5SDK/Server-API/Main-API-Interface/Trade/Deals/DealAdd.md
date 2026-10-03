[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealAdd

[Previous](DealUnsubscribe.md) | [Next](DealAddBatch.md)

# IMTServerAPI::DealAdd

Adds a deal to the server database.
    
    
    MTAPIRES  IMTServerAPI::DealAdd(
       IMTDeal*  deal      // An object of a deal
       )

### Parameters

**deal**  
[in] An object of a deal.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.

### Note

A deal can only be added to the database of the server, on which the plugin is running.

The ticket of the deal being added ([IMTDeal::DealSet](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DealSet.md)) must fall into the deals range of the trading server ([IMTConServerTrade::DealsRange*](../../../../Configuration-Interfaces/Network/IMTConServerTrade/DealsRangeAdd.md)), and must be greater than the last used ticket. 

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


