[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealAddBatchArray

[Previous](DealAddBatch.md) | [Next](DealUpdate.md)

# IMTManagerAPI::DealAddBatchArray

Add a batch of deals to the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealAddBatchArray(
       IMTDeal**       deals,         // Array of deals
       const UINT      deals_total,   // Number of deals in the array
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealAddBatchArray(
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

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all deals have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been added. Analyze the 'results' array for more details on the execution results. The result of addition of each deal from the 'deals' array is added to 'results'. The result index corresponds to the deal index in the source array.

### Note

Deals can only be added to the database of the server, to which the application is connected.

Use this method very carefully. Deals are added directly to clients' trading histories. The addition of deals does not affect clients' balances and positions. Therefore, [IMTAdminAPI::PositionCheck](../../../Administrator-Interface/Trade-Databases/Positions/PositionCheck.md) will show that the clients' positions do not match their history of deals. Note that further correction of balances ([IMTAdminAPI::UserBalanbceCheck](../../../Administrator-Interface/Users/UserBalanceCheck.md)) and positions ([IMTAdminAPI::PositionFix](../../../Administrator-Interface/Trade-Databases/Positions/PositionFix.md)) will require a lot of resources and time, since these methods analyze clients' entire trading histories.

The tickets of the deals you are adding ([IMTDeal::DealSet](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DealSet.md)) must fall within the deals range on the trading server ([IMTConServerTrade::DealsRange*](../../../../Configuration-Interfaces/Network/IMTConServerTrade/DealsRangeAdd.md)), and they must be greater than the last used ticket. 

Note that the server allocates new tickets starting from the last used ticket in the range. For example, if you create a deal with a ticket of 5000, the server will allocate tickets 5001, 5002, etc. for further deals (even if tickets before 5000 are not busy).

If deals are added with zero tickets, the server will assign the tickets automatically.

Deals being added are checked for integrity. The following fields must be filled:

To improve performance, it is recommended to create arrays and perform group operations separately for each trading account.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


