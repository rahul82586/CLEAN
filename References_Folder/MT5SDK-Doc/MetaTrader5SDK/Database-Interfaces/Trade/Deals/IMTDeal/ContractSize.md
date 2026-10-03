[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / ContractSize

[Previous](DigitsCurrency.md) | [Next](Time.md)

# IMTDeal::ContractSize

Get the contract size of the symbol, for which a deal was executed.

C++
    
    
    double  IMTDeal::ContractSize()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.ContractSize()

### Return Value

The contract size of the symbol, for which a deal was executed.

# IMTDeal::ContractSize

Set the contract size of the symbol, for which a deal is executed.

C++
    
    
    MTAPIRES  IMTDeal::ContractSize(
       const double  contract_size      // Contract size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.ContractSize(
       double        contract_size      // Contract size
       )

### Parameters

**contract_size**  
[in] The contract size of the symbol, for which a deal was executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
