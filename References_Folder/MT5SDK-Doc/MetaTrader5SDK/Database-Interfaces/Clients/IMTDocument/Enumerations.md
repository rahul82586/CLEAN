[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / Enumerations

[Previous](../IMTDocument.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTDocument](../IMTDocument.md) interface contains the following enumerations:

  * [IMTDocument::EnDocumentTypes (#endocumenttypes)](Enumerations.md#endocumenttypes)
  * [IMTDocument::EnDocumentStatus (#endocumentstatus)](Enumerations.md#endocumentstatus)



<a id="endocumenttypes"></a>
## IMTDocument::EnDocumentTypes (#endocumenttypes)

Document types are enumerated in IMTDocument::EnDocumentTypes:

Identifier | Value | Description  
DOCUMENT_TYPE_OTHER | 0 | Another document.  
DOCUMENT_TYPE_PERSONAL_IDENITY | 1 | ID document.  
DOCUMENT_TYPE_PERSONAL_ADDRESS | 2 | Proof of address document.  
DOCUMENT_TYPE_REGISTERED_ADDRESS | 1000 | Document confirming legal address.  
DOCUMENT_TYPE_DIRECTORS_PASSPORT | 1001 | The company CEO's ID document.  
DOCUMENT_TYPE_CERTIFICATE_OF_INCORPORATION | 1002 | Certificate of incorporation.  
DOCUMENT_TYPE_CERTIFICATE_OF_DIRECTORS | 1003 | Certificate of directors.  
DOCUMENT_TYPE_CERTIFICATE_OF_GOOD_STANDING | 1004 | Certificate of good standing.  
DOCUMENT_TYPE_FIRST |  | Enumeration beginning. Corresponds to DOCUMENT_TYPE_OTHER.  
DOCUMENT_TYPE_LAST |  | End of enumerationing. Corresponds to DOCUMENT_TYPE_CERTIFICATE_OF_GOOD_STANDING.  
  
The enumeration is used in method [IMTDocument::Flags](DocumentType.md).

<a id="endocumentsubtype"></a>
## IMTDocument::EnDocumentSubtype (#endocumentsubtype)

Document subtypes are listed in IMTDocument::EnDocumentSubtype:

Identifier | Value | Description  
DOCUMENT_SUBTYPE_OTHER | 0 | Another document.  
DOCUMENT_SUBTYPE_ID_CARD | 1 | ID card.  
DOCUMENT_SUBTYPE_PASSPORT | 2 | Passport.  
DOCUMENT_SUBTYPE_DRIVERS | 3 | Driver's license.  
DOCUMENT_SUBTYPE_BANK_CARD | 4 | Bank card.  
DOCUMENT_SUBTYPE_UTILITY_BILL | 5 | Utility bill.  
DOCUMENT_SUBTYPE_BANK_STATEMENT | 6 | Bank statement.  
DOCUMENT_SUBTYPE_TAX_STATEMENT | 7 | Tax return statement.  
DOCUMENT_SUBTYPE_SELFIE | 8 | Selfie.  
DOCUMENT_SUBTYPE_PROFILE_IMAGE | 9 | Profile photo.  
DOCUMENT_SUBTYPE_ID_DOC_PHOTO | 10 | Photo from an identity document.  
DOCUMENT_SUBTYPE_AGREEMENT | 11 | Agreement.  
DOCUMENT_SUBTYPE_CONTRACT | 12 | Contract.  
DOCUMENT_SUBTYPE_RESIDENCE_PERMIT | 13 | Residence permit.  
DOCUMENT_SUBTYPE_EMPLOYMENT_CERTIFICATE | 14 | Employment agreement.  
DOCUMENT_SUBTYPE_DRIVERS_TRANSLATION | 15 | Translation of a drivers license.  
DOCUMENT_SUBTYPE_INVESTOR_DOC | 16 | Investor document.  
DOCUMENT_SUBTYPE_VEHICLE_REG_CERTIFICATE | 17 | Vehicle registration.  
DOCUMENT_SUBTYPE_INCOME_SOURCE | 18 | Proof of income.  
DOCUMENT_SUBTYPE_PAYMENT_METHOD | 19 | Proof of payment.  
DOCUMENT_TYPE_FIRST |  | Beginning of enumeration. Corresponds to DOCUMENT_TYPE_OTHER.  
DOCUMENT_TYPE_LAST |  | End of enumeration. Corresponds to DOCUMENT_SUBTYPE_PAYMENT_METHOD.  
  
The enumeration is used in the [IMTDocument::Subtype](DocumentSubtype.md) method.

<a id="endocumentstatus"></a>
## IMTDocument::EnDocumentStatus (#endocumentstatus)

Document statuses are enumerated in IMTDocument::EnDocumentStatus:

Identifier | Value | Description  
DOCUMENT_STATUS_NEW | 0 | New.  
DOCUMENT_STATUS_APPROVED | 100 | Approved.  
DOCUMENT_STATUS_REJECTED | 200 | Rejected.  
DOCUMENT_STATUS_ARCHIVED | 300 | Archived.  
DOCUMENT_STATUS_DELETED | 400 | Deleted.  
COMMENT_TYPE_FIRST |  | Enumeration beginning. Corresponds to DOCUMENT_STATUS_NEW.  
COMMENT_TYPE_LAST |  | End of enumerationing. Corresponds to DOCUMENT_STATUS_DELETED.  
  
The enumeration is used in the [IMTDocument::DocumentStatus](DocumentStatus.md) method.
