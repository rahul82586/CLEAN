[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Settings Files](../Settings-Files.md) / SettingGet

[Previous](../Settings-Files.md) | [Next](SettingSet.md)

# IMTAdminAPI::SettingGet

Receives the settings file from the trade server.

C++
    
    
    MTAPIRES  IMTAdminAPI::SettingGet(
       LPCWSTR        section,        // directory name
       LPCWSTR        key,            // file name
       LPVOID&        outdata,        // return data
       UINT&          outdata_len     // the size of the return data
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SettingGet(
       string         section,        // directory name
       string         key,            // file name
       byte[]         outdata         // return data
       )

Python
    
    
    AdminAPI.SettingGet(
       section,       # directory name
       key            # file name
       )

### Parameters

**section**  
[in] The name of the subfolder in the manager account directory, from which you want to receive the settings file.

**key**  
[in] The name of the settings file.

**outdata**  
[out] A reference to the data returned in response to the request.

**outdata_len**  
[out] A reference to the size of data returned in response to the request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code. For example:

  * [MT_RET_ERR_PARAMS](../../../Return-Codes/Common-errors.md) — invalid parameters, for example the name of the folder or file.
  * [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) — the requested file is not found.
  * [MT_RET_ERR_MEM](../../../Return-Codes/Common-errors.md) — not enough memory to receive the file.



### Note

The path to the settings file is formed as follows: [trade server directory]\settings\\[manager login]\\. section and key — the first and the second parameters of the IMTAdminAPI::SettingGet method, manager login is the manager's account, using which the application is [connected to the trade server](../Connection-to-the-Server/Connect.md).

The format of the settings file and its parsing methods are determined by the file creator. IMTAdminAPI::Setting* methods work with arbitrary data.
