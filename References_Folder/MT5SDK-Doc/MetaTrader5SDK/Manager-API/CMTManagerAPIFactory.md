[🏠 Document Start](../README.md) / [Manager API](README.md) / CMTManagerAPIFactory

[Previous](Exported-Functions/MTAdminCreateExt.md) | [Next](CMTManagerAPIFactory/Initialize.md)

# CMTManagerAPIFactory

For easy access to the IMTManagerAPI interface, a [factory of interfaces](CMTManagerAPIFactory.md) is implemented in the MT5Manager.h file. The factory automatically loads the appropriate library (32/64-bit) Manager API and provides access to exported functions.

The Manager API factory performs the basic functions of applications — initialization and deinitialization, as well as creation of interfaces of the Manager API. It contains the following methods:

Method | Purpose  
---|---  
[Initialize](CMTManagerAPIFactory/Initialize.md) | Initialize the Manager API.  
[Shutdown](CMTManagerAPIFactory/Shutdown.md) | Unload DLL from the Manager API.  
[CreateManager](CMTManagerAPIFactory/CreateManager.md) | Create the manager interface.  
[CreateAdmin](CMTManagerAPIFactory/CreateAdmin.md) | Create the administrator interface.  
[Version](CMTManagerAPIFactory/Version.md) | Get the version of the Manager Manager API.  
[LicenseCheckAdmin](CMTManagerAPIFactory/LicenseCheckAdmin.md) | Check whether the Manager API application use is authorized.  
[LicenseCheckManager](CMTManagerAPIFactory/LicenseCheckManager.md) | Check whether the Manager API application use is authorized.  
  
Using factories in application development is optional. You can use your own implementation of corresponding functions.
