[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealAddBatch

[Previous](DealAdd.md) | [Next](DealAddBatchArray.md)

# IMTManagerAPI::DealAddBatch

Add a batch of deals to the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealAddBatch(
       IMTDealArray*   deals,         // Array of deals
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealAddBatch(
       CIMTDealArray   deals,         // Array of deals
       MTRetCode[]     res            // Array of results
       )

Python
    
    
    ManagerAPI.DealAddBatch(
       deals           # Array of deals
       )

### Parameters

**deals**  
[in] A pointer to the array of dealsIMTDealArray.

**results**  
[out] An array with the deal addition results. The size of the 'results' array must not be less than the size of the 'deals' array.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all deals have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been added. Analyze the 'results' array for more details on the execution results. This array features the results of adding of each individual deal from the 'deals' array. The result index corresponds to the deal index in the source array.

### Note

Deals can only be added to the database of the server, to which the application is connected.

The manager account requires the [RIGHT_TRADE_MANAGER (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission in order to use the function.

Use this method very carefully.

The tickets of the deals you are adding ([IMTDeal::DealSet](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DealSet.md)) must fall within the deals range on the trading server ([IMTConServerTrade::DealsRange*](../../../../Configuration-Interfaces/Network/IMTConServerTrade/DealsRangeAdd.md)), and they must be greater than the last used ticket. 

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


