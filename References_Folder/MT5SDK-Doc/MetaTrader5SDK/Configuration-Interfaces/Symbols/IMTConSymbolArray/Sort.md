[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTConSymbolArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTConSymbolArray::Sort(
       MTSortFunctionPtr  sort_function      // Sort function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Positioning of elements after sorting is determined by sort_function.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function comparing elements for sorting                          |
    //+------------------------------------------------------------------+
    int SortParams(const void* left,const void* right)
      {
       IMTConSymbol* lft=*(IMTConSymol**)left;
       IMTConSymbol* rgh=*(IMTConSymbol**)right;
    //--- compare by value
       return CMTStr::Compare(lft->Symbol(), rgh->Symbol());
      }
    //+------------------------------------------------------------------+
    //| Parameter comparing function for search                          |
    //+------------------------------------------------------------------+
    int SearchParams(const void* left,const void* right)
      {
       LPCWSTR          lft=(LPCWSTR)left;
       IMTConSymbol*    rgh=*(IMTConSymbol**)right;
    //--- compare by value
       return (CMTStr::Compare(lft, rgh->Symbol());
      }
    //+------------------------------------------------------------------+
    //| Sort and search method example                                   |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTConSymbolArray*  array;
       LPCWSTR             symbol;
       int                 index;
       ...
    //--- initialize and fill the the 'array' array of parameters
       ...
    //--- sort
       array->Sort(SortParams);
    //--- search
       index=array->Search(L"EURUSD",SearchParams);
    //---
       return(0);
      }
