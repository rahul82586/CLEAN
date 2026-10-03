[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealAddBatchArray

[Previous](DealAddBatch.md) | [Next](DealUpdate.md)

# IMTServerAPI::DealAddBatchArray

Adds a batch of deals to a server database.
    
    
    MTAPIRES  IMTServerAPI::DealAddBatchArray(
       IMTDeal**       deals,         // An array of deals
       const UINT      deals_total,   // The number of deals in the array
       MTAPIRES*       results        // An array of results
       )

### Parameters

**deals**  
[in] A pointer to the array of deals.

**deals_total**  
[in] The number of deals in the 'deals' array.

**results**  
[out] An array with the results of adding of deals. The size of the 'results' array must be not less than that of 'deals'.

### Return value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all deals have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of deals have been added. Analyze the 'results' array for a detailed information on execution results. The result of adding of each deal from the 'deals' array is added to 'results'. The index of a result corresponds to the index of a deal in the source array.

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


