[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatTimeMsc

[Previous](FormatTime.md) | [Next](FormatIP.md)

# SMTFormat::FormatTimeMsc

Format time into a string with an indication of milliseconds.
    
    
    static LPCWSTR  SMTFormat::FormatTimeMsc(
       CMTStr  &str,             // Reference to a string object
       INT64   ctm,              // Time
       bool    useSec=false      // Flag of seconds
       )

### Program Parameters

**& str**  
[out] Reference to theCMTStrstring object, into which information is placed.

**ctm**  
[in] Time in milliseconds since 01.01.1970.

**useSec=false**  
[in] The flag of seconds. If true, seconds are shown in the summary line.

### Return Value

Returns a constant pointer to a string in the str object.
