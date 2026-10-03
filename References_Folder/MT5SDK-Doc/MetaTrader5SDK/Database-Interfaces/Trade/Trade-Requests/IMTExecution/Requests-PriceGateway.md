[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests PriceGateway

[Previous](Requests-ApiDataClearAll.md) | [Next](Requests-GatewayID.md)

# IMTExecution::PriceGateway

Gets the price that was actually used for performing a deal through a gateway in an external trading system without taking in consideration its [price transformation settings of the gateway](../../../../Configuration-Interfaces/Gateways/IMTConGateway/TranslateAdd.md).

C++
    
    
    double  IMTExecution::PriceGateway()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTExecution.PriceGateway()

### Return Value

The price at which the deal was executed.

# IMTExecution::PriceGateway

Sets the price that was actually used for performing a deal through a gateway in an external trading system without taking in consideration its [price transformation settings of the gateway](../../../../Configuration-Interfaces/Gateways/IMTConGateway/TranslateAdd.md).

C++
    
    
    MTAPIRES  IMTExecution::PriceGateway(
       const double  price      // Deal execution price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.PriceGateway(
       double        price      // Deal execution price
       )

### Parameters

**price**  
[in] The price at which the deal is executed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The corresponding deal field IMTDeal::PriceGateway is filled in accordance with the IMTExecution::PriceGateway value.
