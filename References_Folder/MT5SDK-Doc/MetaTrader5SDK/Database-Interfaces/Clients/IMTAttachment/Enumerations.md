[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachment](../IMTAttachment.md) / Enumerations

[Previous](../IMTAttachment.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTAttachment](../IMTAttachment.md) interface contains the following enumerations:

  * [IMTAttachment::EnFileType (#enfiletype)](Enumerations.md#enfiletype)
  * [IMTAttachment::EnFileFlags (#enfileflags)](Enumerations.md#enfileflags)



<a id="enfiletype"></a>
## IMTAttachment::EnFileType (#enfiletype)

File types are enumerated in IMTAttachment::EnFileType:

Identifier | Value | Description  
FILE_TYPE_OTHER | 0 | Other.  
FILE_TYPE_TXT | 1 | Plain text file (TXT).  
FILE_TYPE_DOC | 2 | Microsoft Word text file (DOC).  
FILE_TYPE_PDF | 3 | PDF file.  
FILE_TYPE_JPG | 4 | JPG image file.  
FILE_TYPE_PNG | 5 | PNG image file.  
FILE_TYPE_BMP | 6 | BMP image file.  
FILE_TYPE_ZIP | 7 | ZIP archive file.  
FILE_TYPE_FIRST |  | Enumeration beginning. Corresponds to FILE_TYPE_OTHER.  
DOCUMENT_TYPE_LAST |  | End of enumerationing. Corresponds to FILE_TYPE_ZIP.  
  
The enumeration is used in the [IMTAttachment::FileType](FileType.md) method.

<a id="enfileflags"></a>
## IMTAttachment::EnFileFlags (#enfileflags)

File flags are enumerated in IMTAttachment::EnFileFlags:

Identifier | Value | Description  
FILE_FLAG_EMBEDDED | 0x1 | Embedded image flag. Use it for image files which are inserted directly in the comment text. In this case, the file is displayed in the text but it does not appear as a separate attachment.  
FILE_FLAG_NONE | 0 | No flags.  
FILE_FLAG_ALL |  | All flags are set.  
  
The enumeration is used in the [IMTAttachment::FileFlags](FileFlags.md) method.
