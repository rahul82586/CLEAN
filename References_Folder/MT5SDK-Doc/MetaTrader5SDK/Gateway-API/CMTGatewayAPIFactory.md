[🏠 Document Start](../README.md) / [Gateway API](README.md) / CMTGatewayAPIFactory

[Previous](Exported-Functions/MTGatewayCreateLocal.md) | [Next](CMTGatewayAPIFactory/Initialize.md)

# CMTGatewayAPIFactory

The interfaces factory is provided in the "MT5APIateway.h" file to ease the access to the IMTGatewayAPI interface. This factory automatically downloads a necessary GatewayAPI library (32/64-bit) and gives access to the [exported functions](Exported-Functions.md).

The factory contains the following methods:

Method | Description  
---|---  
[Initialize](CMTGatewayAPIFactory/Initialize.md) | Loading of Gateway API library and all functions exported by it.  
[Shutdown](CMTGatewayAPIFactory/Shutdown.md) | Gateway API library unloading.  
[Create](CMTGatewayAPIFactory/Create.md) | Create an instance of the [IMTGatewayAPI](Main-Interface.md) interface.  
[LicenseCheck](CMTGatewayAPIFactory/LicenseCheck.md) | Gateway/data feed module usage license verification.  
[Version](CMTGatewayAPIFactory/Version.md) | Get the version of the loaded Gateway API library.  
  
Using factories in application development is optional. You can use your own implementation of corresponding functions.
