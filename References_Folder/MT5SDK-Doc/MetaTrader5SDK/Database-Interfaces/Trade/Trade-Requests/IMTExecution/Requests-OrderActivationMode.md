[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderActivationMode

[Previous](Requests-OrderActivationFlags.md) | [Next](Requests-OrderTypeFill.md)

# IMTExecution::OrderActivationMode

Gets the activation type of the order placed in an external system.

C++
    
    
    UINT  IMTExecution::OrderActivationMode()

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.OrderActivationMode()

### Return Value

A value of the [IMTOrder::EnOrderActivation (#enorderactivation)](../../Orders/IMTOrder/Enumerations.md#enorderactivation) enumeration.

### Note

IMTExecution::OrderActivationMode changes the value of the appropriate order field [IMTOrder::ActivationMode](../../Orders/IMTOrder/ActivationMode.md).

# IMTExecution::OrderActivationMode

Sets the activation type of the order placed in an external system.

C++
    
    
    MTAPIRES  IMTExecution::OrderActivationMode(
       const UINT  activation      // Activation type
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderActivationMode(
       uint        activation      // Activation type
       )

### Parameters

**activation**  
[in] Order activation type. TheIMTOrder::EnOrderActivationenumeration is used to pass the type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

IMTExecution::OrderActivationMode changes the value of the appropriate order field [IMTOrder::ActivationMode](../../Orders/IMTOrder/ActivationMode.md).
