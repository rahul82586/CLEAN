[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Controlling Positions in External System](../Controlling-Positions-in-External-System.md) / GatewayParamArrayCreate

[Previous](../Controlling-Positions-in-External-System.md) | [Next](GatewayPositionArrayCreate.md)

# IMTGatewayAPI::GatewayParamArrayCreate

Create an object of the array of parameters.

C++
    
    
    IMTConParamArray*  IMTGatewayAPI::GatewayParamArrayCreate()

.NET
    
    
    CIMTConParamArray  CIMTGatewayAPI.GatewayParamArrayCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParamArray](../../../Configuration-Interfaces/Additional-Parameters/IMTConParamArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParamArray::Release](../../../Configuration-Interfaces/Additional-Parameters/IMTConParamArray/Release.md) method of this object.
