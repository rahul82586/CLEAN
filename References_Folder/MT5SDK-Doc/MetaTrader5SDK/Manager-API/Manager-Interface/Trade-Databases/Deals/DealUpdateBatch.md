[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealUpdateBatch

[Previous](DealUpdate.md) | [Next](DealUpdateBatchArray.md)

# IMTManagerAPI::DealUpdateBatch

Update deals in a server database in bulk.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealUpdateBatch(
       IMTDealArray*   deals,         // Array of deals
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealUpdateBatch(
       CIMTDealArray   deals,         // Array of deals
       MTRetCode[]     res            // Array of results
       )

Python
    
    
    ManagerAPI.DealUpdateBatch(
       deals           # Array of deals
       )

### Parameters

**deals**  
[in] A pointer to the array of dealsIMTDealArray.

**results**  
[out] An array with deal update results. The size of the 'results' array must not be less than that of 'deals'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all deals have been updated. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been updated. Analyze the 'results' array for more details concerning the execution results. The update result of each deal from the 'deals' array is added to 'results'. The result index corresponds to the deal index in the source array.

### Note

A deal can only be updated from the applications connected to the trade server, on which the deals have been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


