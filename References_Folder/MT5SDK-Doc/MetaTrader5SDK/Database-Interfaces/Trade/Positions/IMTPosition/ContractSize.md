[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ContractSize

[Previous](DigitsCurrency.md) | [Next](Position.md)

# IMTPosition::ContractSize

Get the contract size of the symbol, for which a position is opened.

C++
    
    
    double  IMTPosition::ContractSize()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.ContractSize()

### Return Value

The contract size of the symbol, for which a position is opened.

# IMTPosition::ContractSize

Set the contract size of the symbol, for which a position is opened.

C++
    
    
    MTAPIRES  IMTPosition::ContractSize(
       const double  contract_size      // Contract size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ContractSize(
       double        contract_size      // Contract size
       )

### Parameters

**contract_size**  
[in] The contract size of the symbol, for which a position is opened.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
