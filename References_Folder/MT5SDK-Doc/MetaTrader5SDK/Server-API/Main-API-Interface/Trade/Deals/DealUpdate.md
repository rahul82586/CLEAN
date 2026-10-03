[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealUpdate

[Previous](DealAddBatchArray.md) | [Next](DealUpdateBatch.md)

# IMTServerAPI::DealUpdate

Update a deal in the server data base.
    
    
    MTAPIRES  IMTServerAPI::DealUpdate(
       IMTDeal*  deal      // Deal object
       )

### Parameters

**deal**  
[in] An object of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A deal can be updated only from the plugins that run on the same trade server where the deal was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md) (an account with this login must exist on the server)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::TimeMsc](../../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md)


  * [IMTDeal::Digits](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md)
  * [IMTDeal::DigitsCurrency](../../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md)
  * [IMTDeal::ContractSize](../../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md)


