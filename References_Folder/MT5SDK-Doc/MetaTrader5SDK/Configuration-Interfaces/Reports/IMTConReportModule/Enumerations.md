[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReportModule](../IMTConReportModule.md) / Enumerations

[Previous](../IMTConReportModule.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConReportModule](../IMTConReportModule.md) interface contains the following enumerations:

  * [IMTConReportModule::EnSnapshots (#ensnapshots)](Enumerations.md#ensnapshots)
  * [IMTConReportModule::EnTypes (#entypes)](Enumerations.md#entypes)



<a id="ensnapshots"></a>
## IMTConReportModule::EnSnapshots (#ensnapshots)

Possible modes for creating snapshots of databases when generating reports are enumerated in IMTConReportModule::EnSnapshots. Database snapshots allow you to quickly save a particular database, which helps to avoid the discrepancy between the beginning and end of the report that may occur due to changes in the market environment during the report generation time.

ID | Value | Description  
SNAPSHOT_NONE | 0x0 | No snapshots.  
SNAPSHOT_USERS | 0x1 | A snapshot of the database of users requested by a manager during report generation.  
SNAPSHOT_USERS_FULL | 0x2 | A snapshot of the entire database of users.  
SNAPSHOT_ACCOUNTS | 0x4 | A snapshot of the database of trading accounts requested by a manager during report generation.  
SNAPSHOT_ACCOUNTS_FULL | 0x8 | A snapshot of the entire database of trading accounts.  
SNAPSHOT_ORDERS | 0x10 | A snapshot of the database of orders requested by a manager during report generation.  
SNAPSHOT_ORDERS_FULL | 0x20 | A snapshot of the entire database of orders.  
SNAPSHOT_POSITIONS | 0x40 | A snapshot of the database of positions requested by a manager during report generation.  
SNAPSHOT_POSITIONS_FULL | 0x80 | A snapshot of the entire database of positions.  
SNAPSHOT_FIRST |  | Beginning of enumeration. It corresponds to SNAPSHOT_NONE.  
SNAPSHOT_LAST |  | End of enumeration. It corresponds to SNAPSHOT_POSITIONS_FULL.  
  
This enumeration is used in the [IMTConReportModule::Snapshots](Snapshots.md) method.

<a id="entypes"></a>
## IMTConReportModule::EnTypes (#entypes)

Types of reports that can be supported by the report module are enumerated in IMTConReportModule::EnTypes:

ID | Value | Description  
TYPE_NONE | 0x0 | None of the types is supported.  
TYPE_HTML | 0x1 | Generation of HTML reports.  
TYPE_TABLE | 0x2 | Generation of reports as binary tables.  
TYPE_FIRST |  | Beginning of enumeration. Corresponds to TYPE_NONE.  
TYPE_LAST |  | Beginning of enumeration. It corresponds to TYPE_TABLE.  
TYPE_ALL |  | All types of reports are supported.  
  
This enumeration is used in the [IMTConReportModule::Types](Types.md) method.
