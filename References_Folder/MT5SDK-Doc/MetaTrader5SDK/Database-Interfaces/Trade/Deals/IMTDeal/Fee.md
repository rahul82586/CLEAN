[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Fee

[Previous](Commission.md) | [Next](RateProfit.md)

# IMTDeal::Fee

Get the fee amount charged for a deal.

C++
    
    
    double  IMTDeal::Fee()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.Fee()

### Return Value

The fee amount charged for a deal. A negative value means funds are deducted from the account. A positive value means funds are added to the account.

### Note

The field is used for the [IMTConCommission::COMM_FEE (#encommmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode) commission type.

# IMTDeal::Fee

Set the fee amount for a deal.

C++
    
    
    MTAPIRES  IMTDeal::Fee(
       const double  fee       // Fee
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Fee(
       double        fee       // Fee
       )

### Parameters

**comm**  
[in] Fee for a deal. A negative value means funds are deducted from the account. A positive value means funds are added to the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The field is used for the [IMTConCommission::COMM_FEE (#encommmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode) commission type.
