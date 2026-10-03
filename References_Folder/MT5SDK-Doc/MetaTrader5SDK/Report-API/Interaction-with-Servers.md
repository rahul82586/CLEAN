[🏠 Document Start](../README.md) / [Report API](README.md) / Interaction with Servers

[Previous](Purpose-of-the.md) | [Next](Configuration-of-Reports.md)

# Interaction with Servers

The information provided in this section will help the developer to clearly understand how the server and the report module.

  * The server can only work with the modules, whose bit is the same as that of the server. The server can only work with the modules, whose bit is the same as that of the server. 64-bit servers only work with 64-bit modules, 32-bit servers — only with 32-bit report modules.  
In connection with this feature, you should always develop report modules in two versions — the 32- and 64-bit.  
It is recommended to give the module versions the appropriate names depending on the versions: ModuleName.dll and ModuleName64.dll. Our company is used the same naming standard.
  * The modules can run only on trade servers.

  
---  
  
## Initialization of modules

The first stage of interaction is the initialization of modules:

  1. When starting the server scans its directory /reports, including all subdirectories, and finds all files with the extension DLL.
  2. The server tries to load all found dll-files and call the [MTReportAbout](Entry-Points/MTReportAbout.md), function in them, which returns the [MTReportInfo](../Structures/MTReportInfo.md) structure containing basic information about the module. If such a function cannot be called, then the dll-file is not a report module.
  3. One DLL module may contain several reports (up to 1024). While downloading a module, a server inquires all reports by the index (index parameter of the [MTReportAbout](Entry-Points/MTReportAbout.md) function). Inquiry continues until [MT_RET_ERR_NOTFOUND](../Return-Codes/Common-errors.md) or [MT_RET_ERROR_NOTIMPLEMENTED](../Return-Codes/API.md) return codes are received.
  4. [MTReportInfo](../Structures/MTReportInfo.md) informs the server about the version of the API, using which a report module was compiled. The module version must be supported by the server.  
If the module version is not supported, then it will not be downloaded, and the appropriate entry will appear in the server log. In this case, you should update MetaTrader 5 Report API and recompile the reports module.



## Reading Configuration Files

After viewing the directory and identifying the reports modules, the server goes through all created [reports configurations](Configuration-of-Reports.md). Further the found modules are loaded only in accordance with the configurations created previously by the system administrator (via the administrator terminal).

> As compared with MetaTrader 4, in the fifth version of the platform, for each reports module you can create multiple configurations with different parameters. In such a case, the server will run several instances of the module.

## Waiting for a report request

Reports are generated at a trade server according to the request from the manager terminal. When a request comes, the [MTReportCreate](Entry-Points/MTReportCreate.md) function of an appropriate report module is called to create a report generation context (object of the class that realizes the [IMTReportContext](Report-Plugin-Interface.md) interface).

## IMTReportContext interface operation

The [IMTReportContext](Report-Plugin-Interface.md) interface contains two methods:

Method | Description  
---|---  
Release | This method removes the created object. In general, the API objects do not count references (AddRef). Thus, when calling the IMTReportContext::Release method, the object is unconditionally removed, and not just the access counter is decreased.  
Generate | The IMTReportContext::Generate method is called by a server for a report generation. It passes to the plugin the IMTReportAPI* api — the interface that implements the Report API (the interface used for interaction with the server).
