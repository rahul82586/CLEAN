[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealAddBatch

[Previous](DealAdd.md) | [Next](DealAddBatchArray.md)

# IMTServerAPI::DealAddBatch

Adds deals to a server database in bulk.
    
    
    MTAPIRES  IMTServerAPI::DealAddBatch(
       IMTDealArray*   deals,         // An array of deals
       MTAPIRES*       results        // An array of results
       )

### Parameters

**deals**  
[in] A pointer to the object of theIMTDealArrayarray of deals.

**results**  
[out] An array with the result of the addition of deals. The size of the 'results' array must be not less than that of 'deals'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) code means that all specified deals have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been added. For details, you should analyze the 'results' array. The result of addition of each deal from the 'deal' array is added to the 'results' array. The index of a result corresponds to the index of a deal in the source array.

### Note

Deals can only be added to the database of the server, on which the plugin is running.

The tickets of the deals being added ([IMTDeal::DealSet](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DealSet.md)) must fall into the deals range of the trading server ([IMTConServerTrade::DealsRange*](../../../../Configuration-Interfaces/Network/IMTConServerTrade/DealsRangeAdd.md)), and must be greater than the last used ticket. 

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)



# IMTServerAPI::DealAddBatch

Adds deals to a server database in bulk.
    
    
    MTAPIRES  IMTServerAPI::DealAddBatch(
       IMTDeal**       deals,         // An array of deals
       const UINT      deals_total,   // The number of deals in the array
       MTAPIRES*       results        // An array of results
       )

### Parameters

**deals**  
[in] A pointer to an array of deals.

**deals_total**  
[in] The number of deals in the 'deals' array.

**results**  
[out] An array with the result of the addition of deals. The size of the 'results' array must be not less than that of 'deals'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) code means that all specified deals have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been added. For details, you should analyze the 'results' array. The result of addition of each deal from the 'deal' array is added to the 'results' array. The index of a result corresponds to the index of a deal in the source array.

### Note

Deals can only be added to the database of the server, on which the plugin is running.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


