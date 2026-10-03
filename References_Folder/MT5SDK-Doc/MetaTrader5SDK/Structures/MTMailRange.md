[🏠 Document Start](../README.md) / [Structures](README.md) / MTMailRange

[Previous](MTTickStat.md) | [Next](MTLogRecord.md)

# MTMailRange

This structure is used to describe the range of recipients of the mailing list. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTMailRange
      {
       UINT64            first_login;                           // The first login in the range
       UINT64            last_login;                            // The last login in the range
       UINT              reserved[4];                           // A reserved field
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTMail::ToRangesAdd](../Database-Interfaces/Mail-Database/IMTMail/ToRangesAdd.md)
  * [IMTMail::ToRangesNext](../Database-Interfaces/Mail-Database/IMTMail/ToRangesNext.md)



The structure contains the following parameters:

Field | Type | Description  
first_login | UINT64 | A login with which the range of the mailing list begins.  
last_login | UINT64 | A login with which the range of the mailing list ends.  
reserved | UINT | A reserved field for future use.
