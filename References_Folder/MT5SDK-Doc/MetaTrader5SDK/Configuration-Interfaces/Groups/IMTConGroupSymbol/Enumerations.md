[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / Enumerations

[Previous](../IMTConGroupSymbol.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConGroupSymol](../IMTConCommission.md) class contains the following enumerations:

<a id="enreflags"></a>
## IMTConGroupSymbol::EnREFlags (#enreflags)

Request execution settings are enumerated in IMTConGroupSymbol::EnREFlags.

ID | Value | Description  
RE_FLAGS_NONE | 0 | No flags.  
RE_FLAGS_ORDER | 1 | Additional confirmation mode.  
RE_FLAGS_ALL |  | End of enumeration. Corresponds to RE_FLAGS_ORDER.  
  
This enumeration is used in the [IMTConGroupSymbol::REFlags](REFlags.md) enumeration.

<a id="enpermissionsflags"></a>
## IMTConGroupSymbol::EnPermissionsFlags (#enpermissionsflags)

Flags of permissions by the group symbols are enumerated in IMTConGroupSymbol::EnPermissionsFlags.

ID | Value | Description  
PERMISSION_NONE | 0 | No flags.  
PERMISSION_BOOK | 1 | Allow the depth of market by symbols for the group.  
PERMISSION_DEFAULT |  | Default flags. Corresponds to allowing the depth of market by symbols for the group.  
PERMISSION_ALL |  | End of enumeration. Corresponds to enabling all the flags.  
  
This enumeration is used in the [IMTConGroupSymbol::PermissionFlags](PermissionsFlags.md) method.
