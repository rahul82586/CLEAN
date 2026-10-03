[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Search

[Previous](IMTProviderArray-Sort.md) | [Next](IMTProviderArray-SearchGreatOrEq.md)

# IMTECNProviderArray::Search

Search in an array for the array element matching the search key.
    
    
    int  IMTECNProviderArray::Search(
       const void*        key,               // sorting key
       MTSortFunctionPtr  sort_function      // a pointer to the search array
       )  const

### Parameters

**key**  
[in] A pointer to the sorting key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of the order object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must first be sorted by calling the [IMTECNProviderArray::Sort](IMTProviderArray-Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| The function compares providers for sorting                      |
    //+------------------------------------------------------------------+
    int SortProviders(const void* left,const void* right)
      {
       IMTECNProvider* lft=*(IMTECNProvider**)left;
       IMTECNProvider* rgh=*(IMTECNProvider**)right;
    //--- compare by provider ID
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| The function compares providers for search                       |
    //+------------------------------------------------------------------+
    int SearchProvider(const void* left,const void* right)
      {
       UINT64          lft=(UINT64)left;
       IMTECNProvider* rgh=*(IMTECNProvider**)right;
    //--- compare by provider ID
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTECNProviderArray* array;
       UINT64               recordid;
       int                  index;
       ...
    //--- initializing and filling the array of providers 'array'
       ...
    //--- sort
       array->Sort(SortProviders);
    //--- search
       index=array->Search(12345,SearchProvider);
    //---
       return(0);
      }
