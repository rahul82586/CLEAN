[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Exported Functions](../Exported-Functions.md) / MTAdminCreateExt

[Previous](MTAdminCreate.md) | [Next](../CMTManagerAPIFactory.md)

# MTAdminCreateExt

The MTAdminCreateExt exported function creates a new [IMTAdminAPI](../Administrator-Interface.md) interface instance and returns a pointer to it. The directory where Manager API is to store its data is additionally specified.
    
    
    MTAPIRES  MTAdminCreateExt(
       UINT           api_version    // API version
       LPCWSTR        datapath,      // data folder
       IMTAdminAPI**  admin          // pointer to the pointer to the API interface
       )

### Parameters

**api_version**  
[out] The current version of Manager API supported by the server is passed in this parameter.

**datapath**  
[in] The absolute path to the directory where Manager API is to store its data (local cache, journals, etc.) is additionally specified. If NULL, the application stores data in the directory it is launched from.

**admin**  
[out] A pointer to the pointer to the createdIMTAdminAPIinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

By default, Manager API stores its data in the directory it is launched from. In some cases, the need arises to re-define the data folder, for example, if the application is installed to Program Files of MS Windows Vista or higher. By default, applications installed to Program Files are not allowed to write their data to the installation folder in these systems. In this case, use a special directory in [system disk letter]:\Users\\[account name in OS]\AppData\Roaming\\[application data folder], for example, C:\Users\JohnSmith\AppData\Roaming\ManagerAPIApp.
