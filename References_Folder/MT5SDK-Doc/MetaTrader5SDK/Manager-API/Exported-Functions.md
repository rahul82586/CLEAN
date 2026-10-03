[🏠 Document Start](../README.md) / [Manager API](README.md) / Exported Functions

[Previous](Python-Implementation.md) | [Next](Exported-Functions/MTManagerVersion.md)

# Exported Functions

The MT5APIManager.dll library (as well as its 64-bit version), which is used for implementing interaction between the application and the MetaTrader 5 trading platform, exports several functions:

Function | Purpose  
---|---  
[MTManagerVersion](Exported-Functions/MTManagerVersion.md) | Returns the version of the Manager API library.  
[MTManagerCreate](Exported-Functions/MTManagerCreate.md) | Creates a new object of the [IMTManagerAPI](Manager-Interface.md) interface and returns a pointer to it.  
[MTManagerCreateExt](Exported-Functions/MTManagerCreateExt.md) | Creates a new object of the [IMTManagerAPI](Manager-Interface.md) interface and returns a pointer to it. The directory where Manager API is to store its data is additionally specified.  
[MTAdminCreate](Exported-Functions/MTAdminCreate.md) | Creates a new object of the [IMTAdminAPI](Administrator-Interface.md) interface and returns a pointer to it.  
[MTAdminCreateExt](Exported-Functions/MTAdminCreateExt.md) | Creates a new object of the [IMTAdminAPI](Administrator-Interface.md) interface and returns a pointer to it. The directory where Manager API is to store its data is additionally specified.
