[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests PriceGateway

[Previous](Requests-PositionExternalID.md) | [Next](Requests-ExternalRetcode.md)

# IMTConfirm::PriceGateway

Gets the price that was actually used for performing a deal through a gateway in an external trading system without taking in consideration its [price transformation settings of the gateway](../../../../Configuration-Interfaces/Gateways/IMTConGateway/TranslateAdd.md).

C++
    
    
    double  IMTConfirm::PriceGateway()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConfirm.PriceGateway()

### Return Value

The price at which the deal was executed.

# IMTConfirm::PriceGateway

Sets the price that was actually used for performing a deal through a gateway in an external trading system without taking in consideration its [price transformation settings of the gateway](../../../../Configuration-Interfaces/Gateways/IMTConGateway/TranslateAdd.md).

C++
    
    
    MTAPIRES  IMTConfirm::PriceGateway(
       const double  price      // Deal execution price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.PriceGateway(
       double        price      // Deal execution price
       )

### Parameters

**price**  
[in] The price at which the deal is executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

According to the IMTConfirm::PriceGateway value, the corresponding field of deal [IMTDeal::PriceGateway](../../Deals/IMTDeal/PriceGateway.md) is filled.
