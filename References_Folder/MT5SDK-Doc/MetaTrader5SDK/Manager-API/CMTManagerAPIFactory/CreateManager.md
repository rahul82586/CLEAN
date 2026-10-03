[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [CMTManagerAPIFactory](../CMTManagerAPIFactory.md) / CreateManager

[Previous](Shutdown.md) | [Next](CreateAdmin.md)

# CMTManagerAPIFactory::CreateManager

Create the manager interface [IMTManagerAPI](../Manager-Interface.md).

C++
    
    
    MTAPIRES  CMTManagerAPIFactory::CreateManager(
       UINT             version,       // Version
       IMTManagerAPI**  manager        // A pointer to the manager interface
       )

.NET
    
    
    CIMTManagerAPI  SMTManagerAPIFactory.CreateManager(
       uint             version,       // Version
       out MTRetCode    res            // Response code
       )

### Parameters

**version**  
[in] Version of the MT5APIManager.h header file

**manager**  
[out] A pointer to the manager interfaceIMTManagerAPI.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The Manager API application can use separate data directories for each manager and administrator interface (to store the local data cache). However, the application log is always written to only one data directory, which is specified during creation of the first interface (no matter whether it is a manager or an administrator interface).

# CMTManagerAPIFactory::CreateManager

Creating the [IMTManagerAPI](../Manager-Interface.md) manager interface specifying the directory where Manager API application data are to be stored.

C++
    
    
    MTAPIRES  CMTManagerAPIFactory::CreateManager(
       UINT             version,       // version
       LPCWSTR          datapath,      // data folder
       IMTManagerAPI**  manager        // pointer to the manager interface
       )

.NET
    
    
    CIMTManagerAPI  SMTManagerAPIFactory.CreateManager(
       uint             version,       // version
       string           datapath,      // data folder
       out MTRetCode    res            // response code
       )

### Parameters

**version**  
[in] Version of the MT5APIManager.h header file.

**datapath**  
[in] The absolute path to the directory where Manager API is to store its data (local cache, journals, etc.) is additionally specified. If NULL, the application stores data in the directory it is launched from.

**manager**  
[out] A pointer to the manager interfaceIMTManagerAPI.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

By default, Manager API stores its data in the directory it is launched from. In some cases, the need arises to re-define the data folder, for example, if the application is installed to Program Files of MS Windows Vista or higher. By default, applications installed to Program Files are not allowed to write their data to the installation folder in these systems. In this case, use a special directory in [system disk letter]:\Users\\[account name in OS]\AppData\Roaming\\[application data folder], for example, C:\Users\JohnSmith\AppData\Roaming\ManagerAPIApp.
