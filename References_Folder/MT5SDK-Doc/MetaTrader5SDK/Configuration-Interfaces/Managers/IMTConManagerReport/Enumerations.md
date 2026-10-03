[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerReport](../IMTConManagerReport.md) / Enumerations

[Previous](../IMTConManagerReport.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConManagerReport](../IMTConManagerReport.md) class contains the following enumerations:

  * [IMTConManagerReport::EnPermissionsFlags (#enpermissionsflags)](Enumerations.md#enpermissionsflags)



<a id="enpermissionsflags"></a>
## IMTConManagerReport::EnPermissionsFlags (#enpermissionsflags)

The states of manager permissions are listed in IMTConManager::EnPermissionsFlags.

ID | Value | Description  
PERMISSION_NONE | 0x00000000 | Access is denied.  
PERMISSION_VIEW | 0x00000001 | Permission to view the report.  
PERMISSION_EXPORT | 0x00000002 | Permission to export report data to a file.  
PERMISSION_ALL |  | Enumeration end. Corresponds to PERMISSION_EXPORT.  
  
The enumeration is used in the [IMTConManagerReport::Permissions](Permissions.md) method.
