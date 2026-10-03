[🏠 Document Start](../README.md) / [Structures](README.md) / MTReportInfo

[Previous](MTEconomicEvent.md) | [Next](MTReportParam.md)

<a id="mtreportinfo"></a>
# MTReportInfo (#mtreportinfo)

The MTReportInfo structure is used for transmitting the primary data of a reports module to a server. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTReportInfo
      {
       //--- databases snapshots flags
       enum EnSnapshots
         {
          SNAPSHOT_NONE          =0x0,                          // Without a snapshot
          SNAPSHOT_USERS         =0x1,                          // Requested users database snapshot
          SNAPSHOT_USERS_FULL    =0x2,                          // A snapshot of the entire database of users
          SNAPSHOT_ACCOUNTS      =0x4,                          // Requested accounts state snapshot
          SNAPSHOT_ACCOUNTS_FULL =0x8,                          // A snapshot of the entire database of trading accounts
          SNAPSHOT_ORDERS        =0x10,                         // Requested orders database snapshot
          SNAPSHOT_ORDERS_FULL   =0x20,                         // A snapshot of the entire database of orders
          SNAPSHOT_POSITIONS     =0x40,                         // Requested positions database snapshot
          SNAPSHOT_POSITIONS_FULL=0x80,                         // A snapshot of the entire database of positions
          SNAPSHOT_NO_GROUPS_LOGINS=0x100,                      // Do not form a list of logins by groups
          //---
          SNAPSHOT_ALL =SNAPSHOT_USERS|SNAPSHOT_ACCOUNTS|SNAPSHOT_ORDERS|SNAPSHOT_POSITIONS,
          SNAPSHOT_ALL_FULL =SNAPSHOT_USERS_FULL|SNAPSHOT_ACCOUNTS_FULL|SNAPSHOT_ORDERS_FULL|SNAPSHOT_POSITIONS_FULL, 
         };
       //--- Types of reports
       enum EnTypes
         {
          TYPE_NONE              =0x0,                          // Reports are not supported
          TYPE_HTML              =0x1,                          // HTML report
          TYPE_TABLE             =0x2,                          // Binary table
          //---
          TYPE_ALL               =TYPE_HTML|TYPE_TABLE
         };
       //--- Internet Explorer minimum version
       enum EnIEVersion
         {
          IE_VERSION_ANY         =0x0000,                       // Any version of IE
          IE_VERSION_9           =0x0900,                       // not older than IE 9
          //---
          IE_VERSION_FIRST       =IE_VERSION_ANY,
          IE_VERSION_LAST        =IE_VERSION_9,
         };
       //--- Information about the module
       UINT              version;                               // Module version
       UINT              version_api;                           // Report API version
       UINT              version_ie;                            // IE minimum version
       wchar_t           name[64];                              // Module name
       wchar_t           copyright[128];                        // Copyright
       wchar_t           description[256];                      // Description
       UINT              snapshots;                             // Snapshots modes
       UINT              types;                                 // Types of reports
       wchar_t           category[64];                          // Report category
       MTReportParam     params[64];                            // Parameters of request
       UINT              params_total;                          // Number of request parameters
       MTReportParam     config[64];                            // Module parameters
       UINT              config_total;                          // Number of module parameters
       UINT              reserved[64];                          // A reserved field
      };
    #pragma pack(pop)

The structure is passed to the server via the [MTReportAbout](../Report-API/Entry-Points/MTReportAbout.md) entry point.

<a id="enumerations"></a>
## Enumerations (#enumerations)

The structure contains the following enumerations:

  * EnSnapshots
  * EnTypes
  * EnIEVersion



<a id="ensnapshots"></a>
### EnSnapshots (#ensnapshots)

Possible modes for creating snapshots of databases when generating reports are enumerated in EnSnapshots. Database snapshots allow you to quickly save a particular database, which helps to avoid the discrepancy between the beginning and end of the report that may occur due to changes in the market environment during the report generation time.

ID | Value | Description  
SNAPSHOT_NONE | 0x0 | No snapshots.  
SNAPSHOT_USERS | 0x1 | A snapshot of the database of users [requested by a manager](../Report-API/Request-for-Reports.md) during report generation. To request a report by groups/users, the report module must have the [MTReportParam::TYPE_GROUPS (#enparamtype)](MTReportParam.md#enparamtype) parameter turned on.  
SNAPSHOT_USERS_FULL | 0x2 | A snapshot of the entire database of users.  
SNAPSHOT_ACCOUNTS | 0x4 | A snapshot of the database of trading accounts requested by a manager during report generation. To request a report by groups/users, the report module must have the [MTReportParam::TYPE_GROUPS (#enparamtype)](MTReportParam.md#enparamtype) parameter enabled.  
SNAPSHOT_ACCOUNTS_FULL | 0x8 | A snapshot of the entire database of trading accounts.  
SNAPSHOT_ORDERS | 0x10 | A snapshot of the database of orders of clients requested by a manager during report generation. To request a report by groups/users, the report module must have the [MTReportParam::TYPE_GROUPS (#enparamtype)](MTReportParam.md#enparamtype) parameter enabled.  
SNAPSHOT_ORDERS_FULL | 0x20 | A snapshot of the entire database of orders.  
SNAPSHOT_POSITIONS | 0x40 | A snapshot of the database of positions of clients requested by a manager during report generation. To request a report by groups/users, the report module must have the [MTReportParam::TYPE_GROUPS (#enparamtype)](MTReportParam.md#enparamtype) parameter enabled.  
SNAPSHOT_POSITIONS_FULL | 0x80 | A snapshot of the entire database of positions.  
SNAPSHOT_NO_GROUPS_LOGINS | 0x100 | Disable automatic generation of a list of logins if a list of groups is passed in a report request. Many reports available in the platform package use the standard "Groups" parameter, indicating the list of groups for which a report should be generated. Every time when a report is generated with this parameter, the API generates the appropriate list of logins (it can be obtained via the [IMTReportAPI::ParamLogins](../Report-API/Main-Interface-of-Reports/Report-Parameters/ParamLogins.md) and [IMTReportAPI::KeySetParamLogins](../Report-API/Main-Interface-of-Reports/Data-cache/KeySetParamLogins.md) methods). This is a time consuming operation. If your report can handle the "Groups" parameter directly, disabled the generation of the list of logins using the SNAPSHOT_NO_GROUPS_LOGINS flag and save computing resources.  
SNAPSHOT_ALL |  | Enabling all eased snapshots of databases (only the data requested by a manager).  
SNAPSHOT_ALL_FULL |  | Enabling all full snapshots of databases (*_FULL).  
  
<a id="entypes"></a>
### EnTypes (#entypes)

Types of reports that can be supported by the module are enumerated in EnTypes:

ID | Value | Description  
TYPE_NONE | 0x0 | None of the types is supported.  
TYPE_HTML | 0x1 | Generation of HTML reports.  
TYPE_TABLE | 0x2 | Generation of reports as binary tables.  
TYPE_ALL |  | All types of reports are supported.  
  
This enumeration is used in the [IMTReportContext::Generate](../Report-API/Report-Plugin-Interface/Generate.md) method.

<a id="enieversion"></a>
### EnIEVersion (#enieversion)

Internet Explorer minimum version is indicated using EnIEVersion for correct display of HTML reports.

ID | Value | Description  
IE_VERSION_ANY | 0x0000 | Any Internet Explorer version is supported.  
IE_VERSION_9 | 0x0900 | Internet Explorer version should be no older than 9.  
IE_VERSION_FIRST |  | Beginning of enumeration. Corresponds to IE_VERSION_ANY.  
IE_VERSION_LAST |  | End of enumeration. Corresponds to IE_VERSION_9.  
  
<a id="parameters"></a>
## Parameters (#parameters)

The structure contains the following parameters:

Field | Type | Description  
version | UINT | In this parameter, information about the reports module version is passed to the server.  
version_api | UINT | This field is used to pass the version of the Report API, in which the module has been compiled.  
version_ie | UINT | The Internet Explorer minimum version is passed in this field for the correct display of reports. To pass the version, the EnIEVersion enumeration is used.  
name | wchar_t | This parameter is used to pass the name of the module.  
copyright | wchar_t | This parameter is used to pass the copyright.  
description | wchar_t | This parameter is used to pass the module description.  
snapshots | UINT | Databases snapshots flags are passed in this parameter. To pass the options, the EnSnapshots enumeration is used.  
types | UINT | Reports types supported by the module are passed in this parameter. EnTypes enumeration is used for passing.  
category | wchar_t | Report category. It is used for grouping reports in a tree view in the Manager and Administrator terminals.  
params | MTReportParam | The array of the reports request parameters from this module. The parameters are described by the [MTReportParam](MTReportParam.md) structure.  
params_total | UINT | The total number of request parameters.  
config | MTReportParam | The array of external module parameters that can be changed during the configuration in MetaTrader 5 Administrator. The parameters are described by the [MTReportParam](MTReportParam.md) structure.  
config_total | UINT | The total number of external parameters.  
reserved | UINT | A reserved field for future use.
