[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetColumn](../IMTDatasetColumn.md) / Enumerations

[Previous](../IMTDatasetColumn.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTDatasetColumn](../IMTDatasetColumn.md) interface contains the following enumerations:

  * [IMTDatasetColumn::EnType (#entype)](Enumerations.md#entype)
  * [IMTDatasetColumn::EnFlags (#enflags)](Enumerations.md#enflags)



<a id="entype"></a>
## IMTDatasetColumn::EnType (#entype)

Types of values that can be written in table columns are listed in IMTDatasetColumn::EnType.

ID | Value | Size (in bytes) | Description  
---|---|---|---  
Basic types  
TYPE_INT8 | 0 | 1 | Integer (8 bits).  
TYPE_UINT8 | 1 | 1 | Unsigned integer (8 bits).  
TYPE_INT16 | 2 | 2 | Ineger (16 bits).  
TYPE_UINT16 | 3 | 2 | Unsigned integer (16 bits).  
TYPE_INT32 | 4  | 4  | Integer (32 bits).  
TYPE_UINT32 | 5 | 4  | Unsigned integer (32 bits).  
TYPE_INT64 | 6 | 8 | Integer (64 bits).  
TYPE_UINT64 | 7 | 8 | Unsigned integer (64 bits).  
TYPE_DOUBLE | 8 | 8 | Floating-point number.  
TYPE_MONEY | 9 | 8 | Monetary unit.  
TYPE_STRING | 10 |  | A string in the Unicode format. The size is set by the [IMTDatasetColumn::Size](Size.md) method.  
TYPE_DATE | 11 | 8 | Date.  
TYPE_TIME | 12 | 8 | Time.  
TYPE_DATETIME | 13 | 8 | Date and time.  
TYPE_TIME_MSC | 14 | 8 | Time with millisecond precision.  
TYPE_DATETIME_MSC | 15 | 8 | Date and time with millisecond precision.  
Prices  
TYPE_PRICE | 100 | 8 | Price.  
TYPE_PRICES | 101 | 16 | Bid/Ask prices.  
TYPE_PRICE_POSITION | 102 | 8 | Position price.  
Volumes  
TYPE_VOLUME | 200 | 8 | Volume.  
TYPE_VOLUME_ORDER | 201 | 16 | Initial/current volume.  
TYPE_VOLUME_EXT | 202 | 8 | [Extended precision (#volume)](../../../Development-Features/README.md#volume) volume.  
TYPE_VOLUME_ORDER_EXT | 203 | 16 | Initial/current order volume with [extended precision (#volume)](../../../Development-Features/README.md#volume).  
TYPE_VOLUME_POSITION_EXT | 204 | 16 | Closed/initial position volume with [extended precision (#volume)](../../../Development-Features/README.md#volume).  
Positions  
TYPE_POSITION_TYPE | 300 | 4  | [Position type (#enpositionaction)](../../../Database-Interfaces/Trade/Positions/IMTPosition/Enumerations.md#enpositionaction).  
Orders  
TYPE_ORDER_TYPE | 400 | 4  | [Type of the order (#enordertype)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype).  
TYPE_ORDER_TYPE_TIME | 401 | 4  | [Order expiration type (#enordertime)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertime).  
TYPE_ORDER_TYPE_REASON | 402 | 4  | [Reason for placing the order (#enorderreason)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderreason).  
TYPE_ORDER_STATUS | 403 | 4  | [Order state. (#enorderstate)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate)  
TYPE_ORDER_FILLING | 404 | 4  | [Order filling mode (#enorderfilling)](../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderfilling).  
Deals  
TYPE_DEAL_ACTION | 500 | 4  | [Type of action (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) performed with a deal.  
TYPE_DEAL_ENTRY | 501 | 4  | [Deal direction (#endealentry)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealentry).  
Accounts  
TYPE_USER_LOGIN | 600 | 8 | Account number.  
TYPE_USER_LEVERAGE | 601 | 4  | Leverage size.  
  
This enumeration is used in the [IMTDatasetColumn::Type](Type.md) method.

<a id="enflags"></a>
## IMTDatasetColumn::EnFlags (#enflags)

Columns display flags are listed in IMTDatasetColumn::EnFlags:

ID | Value | Description  
FLAG_NONE | 0x00000000 | No flags.  
FLAG_PRIMARY | 0x00000001 | Key column. The field, according to which a table is sorted, can contain repeating values. Secondary feature is required for sorting such values and the key column is suitable for that role. The field must necessarily have the [integer type (#entype)](Enumerations.md#entype) (TYPE_INT8,TYPE_UINT8, ... TYPE_INT64, TYPE_UINT64).  
FLAG_HIDDEN_VIEW | 0x00000002 | The column is hidden in the manager terminal.  
FLAG_HIDDEN_SAVE | 0x00000004 | The column can be found in the exported report file.  
FLAG_HIDDEN |  | The column is hidden in the manager and the exported files.  
FLAG_LEFT | 0x00000008 | Forced levelling of the contents by the left margin.  
FLAG_RIGHT | 0x00000010 | Forced leveling of the contents by the right margin.  
FLAG_CENTER |  | Forced leveling of the contents centrally.  
FLAG_SORT_DEFAULT | 0x00000100 | The reported will be sorted by this column by default.  
FLAG_INVISIBLE_DEFAULT | 0x00000200 | The column is hidden when viewed in the Manager terminal but can be enabled via the context menu.  
  
In case leveling flags are not specified, contents of the columns is levelled automatically:

  * the first column is always levelled by the left margin;
  * columns with string values are levelled by the left margin;
  * columns with figures, monetary units, time, prices, volumes or logins are levelled by the right margin.



This enumeration is used in the [IMTDatasetColumn::Flags](Flags.md) method.
