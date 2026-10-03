[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealAddBatchArray

[Previous](DealAddBatch.md) | [Next](DealUpdate.md)

# IMTAdminAPI::DealAddBatchArray

Add a batch of deals to the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealAddBatchArray(
       IMTDeal**       deals,         // Array of deals
       const UINT      deals_total,   // Number of deals in the array
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealAddBatchArray(
       CIMTDeal[]      deals,         // Array of deals
       MTRetCode[]     retcodes       // Array of results
       )

### Parameters

**deals**  
[in] A pointer to the array of deals.

**deals_total**  
[in] The number of deals in the 'deals' array.

**results**  
[out] An array with deal addition results. The size of the 'results' array must not be less than the size of the 'deals' array.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all deals have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been added. Analyze the 'results' array for more details on the execution results. This array features the results of adding of each individual deal from the 'deals' array. The result index corresponds to the deal index in the source array.

### Note

Deals can only be added to the database of the server, to which the application is connected.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


