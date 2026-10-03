[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon Enumerations

[Previous](../IMTCon.md) | [Next](IMTCon-Release.md)

# Enumerations

The [IMTConCommon](../IMTCon.md) class contains one enumeration.

## IMTConCommon::EnUpdateMode

The modes of receiving the platform components updates are listed in IMTConCommon::EnUpdateMode.

ID | Value | Description  
UPDATE_DISABLE | 0 | Update disabled.  
UPDATE_ENABLE | 1 | Update enabled.  
UPDATE_ENABLE_BETA | 2 | Update, including intermediate versions.  
UPDATE_FIRST |  | Beginning of enumeration. It corresponds to UPDATE_DISABLE.  
UPDATE_LAST |  | End of enumeration. It corresponds to UPDATE_ENABLE_BETA.  
  
This enumeration is used in method [IMTConCommon::LiveUpdateMode](IMTCon-LiveUpdateMode.md).
