[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealStorage

[Previous](Requests-DealReason.md) | [Next](Requests-DealCommission.md)

# IMTExecution::DealStorage

Getting the swap size of a deal conducted out as a result of trade execution.

C++
    
    
    double  IMTExecution::DealStorage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.DealStorage()

### Return Value

The swap size for a deal.

# IMTExecution::DealStorage

Setting the swap size of a deal conducted out as a result of trade execution.

C++
    
    
    MTAPIRES  IMTExecution::DealStorage(
       const double  storage      // Swap
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealStorage(
       double        storage      // Swap
       )

### Parameters

**storage**  
[in] The swap size for a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If a trade execution results in a deal which opens or increases a position, the current swap in field [IMTPosition::Storage](../../Positions/IMTPosition/Storage.md) will be increased by the swap size passed in the trade execution. 

  * If no swap is specified in the trade execution (IMTExecution::DealStorage was not called), then position swap decreases in proportion to the closed volume. For example, if a deal closes 0.5 lots of a one-lot position, only half of the lot is left.
  * If the swap is specified in the trade execution (method IMTExecution::DealStorage was called), the position swap is decreased by the value passed in Storage. The proportions to be closed relative on the total volume are not taken into account.


