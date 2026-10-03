[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTThread](../CMTThread.md) / Start

[Previous](../CMTThread.md) | [Next](Shutdown.md)

# CMTThread::Start

Start the thread. After calling this method, the function thread_func starts.
    
    
    bool  CMTThread::Start(
       unsigned    (__stdcall *thread_func)(void*),     // Function for execution in the thread
       void        *thread_param,                       // Parameter for the function
       const UINT  stack_size                           // Stack size
       )

### Parameters

**(__stdcall *thread_func)(void*)**  
[in] A pointer to the function of the following form:

***thread_param**  
[in] A pointer to the value that will be passed to the MYThreadFunction function as the myparam parameter.

**stack_size**  
[in] The size of the thread stack in bytes.
    
    
    unsigned __stdcall MyThreadFunction(void *myparam)
       {
        return(0);
       }

### Return Value

If successful, returns true, otherwise returns false.
