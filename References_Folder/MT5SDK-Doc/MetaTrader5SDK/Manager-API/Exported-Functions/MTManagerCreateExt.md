[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Exported Functions](../Exported-Functions.md) / MTManagerCreateExt

[Previous](MTManagerCreate.md) | [Next](MTAdminCreate.md)

# MTManagerCreateExt

The MTManagerCreateExt exported function creates a new [IMTManagerAPI](../Manager-Interface.md) interface instance and returns a pointer to it. The directory where Manager API is to store its data is additionally specified.
    
    
    MTAPIRES  MTManagerCreateExt(
       UINT             api_version    // API version
       LPCWSTR          datapath,      // data folder
       IMTManagerAPI**  manager        // pointer to the pointer to the interface
       )

### Parameters

**api_version**  
[out] The current version of Manager API supported by the server is passed in this parameter.

**datapath**  
[in] The absolute path to the directory where Manager API is to store its data (local cache, journals, etc.) is additionally specified. If NULL, the application stores data in the directory it is launched from.

**manager**  
[out] A pointer to the pointer to the createdIMTManagerAPIinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

By default, Manager API stores its data in the directory it is launched from. In some cases, the need arises to re-define the data folder, for example, if the application is installed to Program Files of MS Windows Vista or higher. By default, applications installed to Program Files are not allowed to write their data to the installation folder in these systems. In this case, use a special directory in [system disk letter]:\Users\\[account name in OS]\AppData\Roaming\\[application data folder], for example, C:\Users\JohnSmith\AppData\Roaming\ManagerAPIApp.
