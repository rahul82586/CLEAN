[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Settings Files](../Settings-Files.md) / SettingSet

[Previous](SettingGet.md) | [Next](SettingDelete.md)

# IMTAdminAPI::SettingSet

Sends the settings file to the trade server.

C++
    
    
    MTAPIRES  IMTAdminAPI::SettingSet(
       LPCWSTR        section,        // directory name
       LPCWSTR        key,            // file name
       const LPVOID&  indata,         // passed data
       const UINT&    indata_len      // size of passed data
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SettingSet(
       string         section,        // directory name
       string         key,            // file name
       byte[]         indata          // passed data
       )

Python
    
    
    AdminAPI.SettingSet(
       section,       # directory name
       key,           # file name
       indata         # passed data
       )

### Parameters

**section**  
[in] The name of the subfolder in the manager account directory, to which you want to write the settings file.

**key**  
[in] The name of the settings file. Only files with the following extensions are allowed: ini, cfg, dat, json, config, sqlite, xml, conf, settings, key, db, txt and log, as well as files without extensions.

**indata**  
[out] A reference to data to be sent.

**indata_len**  
[out] A reference to the size of passed data in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code. For example:

  * [MT_RET_ERR_PARAMS](../../../Return-Codes/Common-errors.md) — invalid parameters, for example the name of the folder or file.
  * [MT_RET_CFG_LIMIT_REACHED](../../../Return-Codes/Configuration-Management.md) — the [maximum number of files or folders (#limit)](SettingSet.md#limit) has been reached.
  * [MT_RET_ERR_DISK](../../../Return-Codes/Common-errors.md) — writing the file to the disk failed.



### Note

The path to the settings file is formed as follows: [trade server directory]\settings\\[manager login]\\. section and key — the first and the second parameters of the IMTAdminAPI::SettingSet method, manager login is the manager's account, using which the application is [connected to the trade server](../Connection-to-the-Server/Connect.md).

The format of the settings file and its parsing methods are determined by the file creator. IMTAdminAPI::Setting* methods work with arbitrary data.

The IMTAdminAPI::SettingSet method works with files, not with individual settings. Therefore, a whole settings file needs to be formed to send changes to the server.
