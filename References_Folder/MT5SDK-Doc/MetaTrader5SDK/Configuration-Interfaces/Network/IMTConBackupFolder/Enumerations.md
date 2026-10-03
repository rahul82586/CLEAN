[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConBackupFolder](../IMTConBackupFolder.md) / Enumerations

[Previous](../IMTConBackupFolder.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConBackupFolder](../IMTConBackupFolder.md) class contains the following enumerations:

  * [IMTConServerBackup::EnBackupFlags (#enbackupflags)](Enumerations.md#enbackupflags)



<a id="enbackupflags"></a>
## IMTConBackupFolder::EnBackupFlags (#enbackupflags)

IMTConBackupFolder::EnBackupFlags lists additional folder backup settings.

ID | Value | Description  
FOLDER_FLAG_NONE | 0x00000000 | No flags.  
FOLDER_FLAG_SUBFOLDERS | 0x00000001 | Enable backup of subdirectories in the specified folder.  
FOLDER_FLAG_ALL |  | All flags are enabled.  
  
The enumeration is used in the [IMTConBackupFolder::Flags](Flags.md) method.
