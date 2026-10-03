[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Categories

[Previous](Keywords.md) | [Next](Timeout.md)

# IMTConFeeder::Categories

Get the category of news received from a data feed.

C++
    
    
    LPCWSTR  IMTConFeeder::Categories()

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.Categories()

Python (Manager API)
    
    
    MTConFeeder.Categories

### Return Value

If successful, it returns a pointer to a string with the categories of news received from the data feed. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFeeder](../IMTConFeeder.md) object.

# IMTConFeeder::Categories

Set a category, to which all news received from the data feed will be assigned.

C++
    
    
    MTAPIRES  IMTConFeeder::Categories(
       LPCWSTR  categories      //Name of the news category
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.Categories(
       string   categories      // Name of the news category
       )

Python (Manager API)
    
    
    MTConFeeder.Categories

### Parameters

**categories**  
[in] The name of the news catego;ry.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the category name is limited to 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
