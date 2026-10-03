[🏠 Document Start](../README.md) / [Manager API](README.md) / Python Implementation

[Previous](NET-Implementation.md) | [Next](Exported-Functions.md)

<a id="implementation-of-metatrader-5-manager-api-in-python"></a>
# Implementation of MetaTrader 5 Manager API in Python (#implementation-of-metatrader-5-manager-api-in-python)

MetaTrader 5 Manager API includes a ready-made implementation for the Python language. [MT5Manager package](https://pypi.org/project/MT5Manager/) combines the flexibility, power and speed of the Manager API library with the simplicity and ability to use the extensive library provided to Python developers. This combination enables transfer of data from servers to machine learning models and fast implementation of scripts for the platform management.

<a id="install"></a>
## Installation (#install)

To install the MT5Manager package, use the pip utility:
    
    
    E:\work\samples>pip install MT5Manager
    Collecting MT5Manager
      Obtaining dependency information for MT5Manager from https://files.pythonhosted.org/packages/31/ad/3d86480fb30221ebb6af58c37ea2a2edfa864f472f5744f412249f4b9d62/MT5Manager-5.0.3906-cp310-cp310-win_amd64.whl.metadata
      Downloading MT5Manager-5.0.3906-cp310-cp310-win_amd64.whl.metadata (2.1 kB)
    Collecting numpy>=1.7 (from MT5Manager)
      Obtaining dependency information for numpy>=1.7 from https://files.pythonhosted.org/packages/b7/db/4d37359e2c9cf8bf071c08b8a6f7374648a5ab2e76e2e22e3b808f81d507/numpy-1.25.2-cp310-cp310-win_amd64.whl.metadata
      Downloading numpy-1.25.2-cp310-cp310-win_amd64.whl.metadata (5.7 kB)
    Using cached MT5Manager-5.0.3906-cp310-cp310-win_amd64.whl (3.8 MB)
    Using cached numpy-1.25.2-cp310-cp310-win_amd64.whl (15.6 MB)
    Installing collected packages: numpy, MT5Manager
    Successfully installed MT5Manager-5.0.3906 numpy-1.25.2

Since this package provides the functionality of the native Manager API in its pure form, you need to perform the same [preparatory steps](Getting-Started.md).

<a id="example"></a>
## Sample usage (#example)

Let's look at a simple example of using MT5Manager. We are going to receive a list of managers and display their number:
    
    
    # include the library
    import MT5Manager
     
    # create manager interface
    manager = MT5Manager.ManagerAPI()
    # connect the server
    if manager.Connect("192.168.1.100:443", 1001, "1234Qwe!", 
                        MT5Manager.ManagerAPI.EnPumpModes.PUMP_MODE_USERS, 120000):
        # get the list of managers on the server
        managers = manager.UserGetByGroup("managers\*")
        # check the obtained list
        if managers is not False:
            print(f"There are {len(managers)} managers on server")
        else:
            # failed to get the list
            print(f"Failed to get manager list: {MT5Manager.LastError()}")
        # disconnect from the server
        manager.Disconnect()
    else:
        # failed to connect to the server
        print(f"Failed to connect to server: {MT5Manager.LastError()}")

Upon successful execution of the script, you should receive the following line:
    
    
    There are 5 managers on server

Let's look at the example in more detail. After connecting the library and creating the ManagerAPI interface, connect to the server at 192.168.1.100:443, with manager login 1001 and password 1234Qwe!:
    
    
    if manager.Connect("192.168.1.100:443", 1001, "1234Qwe!",
                        MT5Manager.ManagerAPI.EnPumpModes.PUMP_MODE_USERS, 120000):

ManagerAPI.Connect function parameters fully correspond to the [IManagerAPI::Connect](Manager-Interface/Connection-to-the-Server/Connect.md) function parameters of the native ManagerAPI: server address, manager login and password, pumping mode and timeout in milliseconds. If the connection to the server fails, the ManagerAPI.Connect function returns False. Error details can be obtained by calling the LastError function.

Next, we get a list of users by group mask:
    
    
    managers = manager.UserGetByGroup("managers\*")

If successful, the UserGetByGroup function returns the list of MT5Manager.MTUser objects. The object properties correspond to the methods of the native Manager API [IMTUser](../Database-Interfaces/Users/IMTUser.md) object.

By default, Manager API stores its data in the directory from which it is launched. There may be situations where the data directory must be overridden. For example, this may be needed to avoid access conflicts to local databases when using several scripts in parallel. To override the data directory for a specific copy of the script, specify the directory when creating the Manager API interface:
    
    
    # create manager interface
    manager = MT5Manager.ManagerAPI("C:\\API\\DataFolder1")

<a id="similarities"></a>
## Matches and differences from the native Manager API (#similarities)

To develop an application using the Python module, use the native Manager API documentation: the method signatures and format are identical except for Python-specific features.

The main classes — ManagerAPI and AdminAPI — correspond to the [IMTManagerAPI](Manager-Interface.md) and [IMTAdminAPI](Administrator-Interface.md) of the native API. For the interfaces of [configuration](../Configuration-Interfaces/README.md) and [data bases](../Database-Interfaces/README.md), there are also similar classes in MT5Manager, for example: [IMTUser](../Database-Interfaces/Users/IMTUser.md) and MTUser, [IMTPosition](../Database-Interfaces/Trade/Positions/IMTPosition.md) and MTPosition, [IMTOrder](../Database-Interfaces/Trade/Orders/IMTOrder.md) and MTOrder.

Enumerations in MT5Manager are created as descendants of the IntFlag class. This type allows comparisons and bit operations with int type variables. For example, the [IMTManagerAPI::EnPumpModes](Manager-Interface/Connection-to-the-Server/Pumping-Modes.md) enumeration in MT5Manager corresponds to ManagerAPI.EnPumpModes.

Unlike the native API, the Python version uses a value return instead of passing the value by reference or pointer. For example, in the native API, the [IMTManagerAPI::UserGet](Manager-Interface/Users/UserGet.md) method writes data using the passed pointer. The similar ManagerAPI.UserGet method in the Python module returns the MTUser object on success or False on failure.
    
    
    user = manager.UserGet(1400)
    if user is False:
        print(f"Failed to get user: {MT5Manager.LastError()}")
    else:
        print(user)

In case you need to pass multiple values from a function, the MT5Manager methods return a tuple of values.

MT5Manager module objects have properties that fully correspond to the methods of the native ManagerAPI interfaces. For example, the [IMTUser](../Database-Interfaces/Users/IMTUser.md) interface features the [IMTUser::Name](../Database-Interfaces/Users/IMTUser/Name.md) method to read the user name and the same-name overload for writing the name. In the MT5Manager module, the MTUser object has a corresponding Name property. The following code demonstrates how to read and write the object name:
    
    
    user = manager.UserGet(1400)
    print(user.Name)    # reading the Name field of the MTUser type 'user' variable
    user.Name = "Alisa" # writing the Name field of the MTUser type 'user' variable

In the native Manager API, objects are created through the Create methods of the IMTManagerAPI or IMTAdminAPI interface. In MT5Manager, objects are created in the classic Python format, but for correct creation, you should always specify an existing object of the ManagerAPI or AdminAPI classes in the parameters:
    
    
    manager = MT5Manager.ManagerAPI()
    user = MT5Manager.MTUser(manager) # creating the object
    user.Name = "Alisa"

An object created without a manager class cannot be used:
    
    
    user = MT5Manager.MTUser() # !!! error
    user.Name = "Alisa"

Functions that return arrays in the native ManagerAPI have counterparts in MT5Manager that return lists.

<a id="numpy-csv"></a>
## Receiving sample values from the databases into the NumPy array and CSV string (#numpy-csv)

The MT5Manager module allows us to query data in object, NumPy array and CSV string formats from trading and user databases. For NumPy arrays and CSV strings, it is possible to obtain sample record values.

Let's have a look at a user base:
    
    
    managers = manager.UserGetByGroup("managers\*")

In this case, the 'managers' object will be a list of objects of MT5Manager.MTUser type. When trying to display a list item:
    
    
    print(managers[0])

we receive:
    
    
    <MT5Manager.MTUser object at 0x00000295675F9530>

Reading and writing data for this object are available through properties similar to the native ManagerAPI [IMTUser](../Database-Interfaces/Users/IMTUser.md) methods.

The functions for obtaining data in NumPy array format have the NumPy postfix. For example, let's get the same list of managers in NumPy array format and display the first element:
    
    
    managers = manager.UserGetByGroupNumPy("managers\*")
        print(managers[0])

As a result we get:
    
    
    (1130, b'managers\\administrators', 0, 16385, 1675247009, 1693568566, b'192.168.1.100', b'Jasmine Robert Garrison', b'Test', b'', b'', 0,
     b'', b'', b'', b'', b'+35700000000',b'Jasmine.Garrison@test.manager.net', b'', b'', b'Changed', 0, b'', 1000, 0, 10986.19, 13.76, 0., 0.,
     0., 0., 0., 45.13, 45.13, 0.6, -35.3, 1688477602, b'0', b'', b'', 25191, b'Jasmine', b'Garrison', b'Robert', b'', 0, 0.)

The 'managers' object in this case is a NumPy array with the data from the user database. This object can be directly passed into both machine learning models and countless other data processing packages that work with NumPy.

Similarly, functions for obtaining data in CSV string format have the CSV postfix. Let's receive and display the same list in CSV format:
    
    
    managers = manager.UserGetByGroupCSV("managers\*")
        print(managers)

During the output, we get the following string:
    
    
    1130    managers\administrators 0       16385   1675247009      1693568566      192.168.1.100  Jasmine Robert Garrison Test             +35700000000...
    1131    managers\administrators 0       16385   1675247009      1693568566      192.168.1.100  Bryan Joshua Peterson   Test             +35700000000...

The resulting string has the following format: entry fields are separated by tabs, each entry is separated from the next by a string break.

In order to display in NumPy array and CSV string formats, it is possible to request only selected fields of an entry through the optional last string 'fields' parameter. For example, consider this code:
    
    
    managers = manager.UserGetByGroupNumPy("managers\*","Login,Name,Group")
    print(managers[0])

Here, a NumPy array with manager data is written to the 'managers' variable. Only the login, name and group of each manager is written. The execution result will look as follows:
    
    
    (1130, b'Jasmine Robert Garrison', b'managers\\administrators')

The names of the fields that can be queried fully corresponds to the names of the object properties. The order in which the fields are displayed corresponds to the order of the fields in the 'fields' parameter. The format of the 'fields' string should strictly correspond to the format in the example: extra spaces, commas and other characters are not allowed. Duplicate fields are not allowed, field names are case sensitive.

<a id="events"></a>
## Event notifications (#events)

To subscribe to events in the native ManagerAPI, we should implement a class that provides the appropriate subscriber interface. Thanks to [duck typing](https://en.wikipedia.org/wiki/Duck_typing) in Python, there is no need to inherit from the subscriber interface. It is sufficient to implement subscriber methods in the class that match in name and signature, and subscribe the object of the class via the corresponding Subscribe method.

Let's look at the example of subscribing to changes in the user database. Suppose that we need to monitor the removal of users from the database. The native ManagerAPI features the [IMTUserSink](../Database-Interfaces/Users/IMTUserSink.md) interface, whose descendant needs to be implemented in this situation. Since we only need to monitor deletion, we are only interested in one method in this interface:
    
    
    virtual void  IMTUserSink::OnUserDelete(
       const IMTUser*  user      // pointer to deleted entry
       )

Let's write a class in Python that implements this method:
    
    
    class UserSink:
        def OnUserDelete(self, user) -> None:
            print(f"User with login: {user.Login} was deleted")

Next, let's create an object and subscribe to changes:
    
    
    user_sink = UserSink()                          # create subscriber
    if not manager.UserSubscribe(user_sink):        # subscribe to changes
        print(f"Failed: {MT5Manager.LastError()}")

If the subscription is successful, a corresponding message is displayed when a user is removed from the database.

Please note the following when subscribing:

  * if the object does not have any implementations of subscriber methods at the time of subscription, the function returns an error
  * repeated subscriptions of the same objects to the same event are allowed - methods will be called as many times for each event as they were subscribed to



<a id="errors"></a>
## Error processing (#errors)

Functions and methods of MT5Manager module objects do not generate exceptions. Most functions return False instead of the expected value in case of an error. In case False may be in the list of expected values, None is returned in case of an error. To find out information about an error that occurred, call the LastError function. It returns a tuple with data about the error: internal MT5Manager error code, native Manager API error code from the [EnMTAPIRetcode](../Return-Codes/README.md) enumeration and a string with a brief error description. For example, if the connection to the server fails, LastError may return the following value:
    
    
    (-1, <EnMTAPIRetcode.MT_RET_ERR_NETWORK: 7>, 'Network error')

where:

  * -1 is the MT5Manager error code indicating an error when calling the native Manager API function
  * <EnMTAPIRetcode.MT_RET_ERR_NETWORK: 7> is the error code from the native Manager API
  * 'Network error' is the error string description



<a id="examples"></a>
## Real-case examples (#examples)

Scripts examples in this section will help you master the Manager API package for Python. Each example is provided with comments.

  * [Adding and updating a user on the server (#example-add-user)](Python-Implementation.md#example-add-user)
  * [Requesting user's deal history (#example-request-deals)](Python-Implementation.md#example-request-deals)
  * [Subscription to position additions and changes (#example-position-events)](Python-Implementation.md#example-position-events)
  * [Receiving ticks (#example-get-ticks)](Python-Implementation.md#example-get-ticks)



<a id="example-add-user"></a>
### Adding and updating a user on the server (#example-add-user)

Let's look at how to create a user, deposit a balance, update rights and change the password:
    
    
    # include the library
    import MT5Manager
    # create manager interface
    manager = MT5Manager.ManagerAPI()
    # connect the server
    if manager.Connect("192.168.1.100:443", 1002, "1Ar#pqkj", 0):
        # create a user
        user = MT5Manager.MTUser(manager)
        # fill in the required fields: group, leverage, first and last name
        user.Group = "demo\\example"
        user.Leverage = 100
        user.FirstName = "John"
        user.LastName = "Smith"
        # add a user to the server
        if not manager.UserAdd(user,"1Ar#pqkj","1Ar#pqkj"):
            # adding failed with an error
            error = MT5Manager.LastError()
            # no more logins
            if error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_USR_LOGIN_EXHAUSTED:
                print("No free logins on server")
            # add a user to another server
            elif error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_USR_LOGIN_PROHIBITED:
                print("Can't add user for non current server")
            # such a user already exists
            elif error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_USR_LOGIN_EXIST:
                print("User with same login already exists")
            # another error
            else:
                print(f"User was not added: {MT5Manager.LastError()}")
        else:
            # user added successfully
            print(f"User {user.Login} was added")
            # deposit balance
            deal_id = manager.DealerBalance(user.Login,100.,MT5Manager.MTDeal.EnDealAction.DEAL_BALANCE,"Start deposit")
            if deal_id is False:
                # depositing ended with error
                error = MT5Manager.LastError()
                # too much deposit amount
                if error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_TRADE_MAX_MONEY:
                    print("Money limit")
                # insufficient money on the account
                elif error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_REQUEST_NO_MONEY:
                    print("Not enough money")
                # another error
                else:
                    print(f"Balance operation failed {MT5Manager.LastError()}")
            else:
                # balance deposited successfully
                print(f"Balance operation succeeded")
                # make sure the balance deposited
                user = manager.UserRequest(user.Login)
                # user not found
                if user == False:
                    print(f"Failed to request user: {MT5Manager.LastError()}")
                else:
                    # display user balance
                    print(f"Found user {user.Login}, balance: {user.Balance}")
                # update user rights
                user.Rights = MT5Manager.MTUser.EnUsersRights.USER_RIGHT_ENABLED | \
                              MT5Manager.MTUser.EnUsersRights.USER_RIGHT_PASSWORD | \
                              MT5Manager.MTUser.EnUsersRights.USER_RIGHT_EXPERT
                # update user on server
                if not manager.UserUpdate(user):
                    print(f"Failed to update user: {MT5Manager.LastError()}")
                else:
                    # change user password
                    if not manager.UserPasswordChange(MT5Manager.MTUser.EnUsersPasswords.USER_PASS_MAIN,
                                                      user.Login, "2Ar#pqkj"):
                        print(f"Failed to update user password: {MT5Manager.LastError()}")
        # disconnect from the server
        manager.Disconnect()
    else:
        # failed to connect to the server
        print(f"Failed to connect to server: {MT5Manager.LastError()}")

Creating a manager and connecting to the server [have already been considered above (#example)](Python-Implementation.md#example). In this example, there is no need to synchronize data with the server, so the pumping mode is set to 0, that is, without synchronization, for connection speed.

Let's move on to creating a user. According to the documentation for the native Manager API, we are interested in the [ManagerAPI.UserAdd](Manager-Interface/Users/UserAdd.md) function. Create a user, while specifying the correct manager in the parameters:
    
    
    # create a user
        user = MT5Manager.MTUser(manager)

Let's enter the necessary fields according to the native API documentation:
    
    
    # fill in the required fields: group, leverage, first and last name
        user.Group = "demo\\example"
        user.Leverage = 100
        user.FirstName = "John"
        user.LastName = "Smith"

Now we can add a user to the server using the UserAdd method:
    
    
    # add a user to the server
        if not manager.UserAdd(user,"1Ar#pqkj","1Ar#pqkj"):
            # adding failed with an error
            error = MT5Manager.LastError()
            # no more logins
            if error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_USR_LOGIN_EXHAUSTED:
                print("No free logins on server")
            # add a user to another server
            elif error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_USR_LOGIN_PROHIBITED:
                print("Can't add user for non current server")
            # such a user already exists
            elif error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_USR_LOGIN_EXIST:
                print("User with same login already exists")
            # another error
            else:
                print(f"User was not added: {MT5Manager.LastError()}")

Make sure to add error checks: MT5Manager does not use exceptions and if the user has not been added to the server, the program will continue running.

When calling UserAdd, the fields of the added user in the user variable will be updated by the server. In particular, the Login of the added user will be set to be used for further operations.

Let's deposit the user balance using the [DealerBalance](Manager-Interface/Trade-Activity/Dealing/DealerBalance.md) function:
    
    
    deal_id = manager.DealerBalance(user.Login,100.,MT5Manager.MTDeal.EnDealAction.DEAL_BALANCE,"Start deposit")
            if deal_id is False:
                # depositing ended with error
                error = MT5Manager.LastError()
                # too much deposit amount
                if error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_TRADE_MAX_MONEY:
                    print("Money limit")
                # insufficient money on the account
                elif error[1] == MT5Manager.EnMTAPIRetcode.MT_RET_REQUEST_NO_MONEY:
                    print("Not enough money")
                # another error
                else:
                    print(f"Balance operation failed {MT5Manager.LastError()}")

The user has been created and the balance has been deposited. Let's check if everything went well by requesting user data from the server:
    
    
    # make sure the balance deposited
                user = manager.UserRequest(user.Login)
                # user not found
                if user == False:
                    print(f"Failed to request user: {MT5Manager.LastError()}")
                else:
                    # display user balance
                    print(f"Found user {user.Login}, balance: {user.Balance}")

Since we set the pumping mode to 0 during connection, user data will not be synchronized. In this case, the [UserGet](Manager-Interface/Users/UserGet.md) function is not suitable, we need to use [UserRequest](Manager-Interface/Users/UserRequest.md) instead.

If everything went well, assign the correct rights to the user:
    
    
    # update user rights
    user.Rights = MT5Manager.MTUser.EnUsersRights.USER_RIGHT_ENABLED | \
                  MT5Manager.MTUser.EnUsersRights.USER_RIGHT_PASSWORD | \
                  MT5Manager.MTUser.EnUsersRights.USER_RIGHT_EXPERT
    # update user on server
    if not manager.UserUpdate(user):
        print(f"Failed to update user: {MT5Manager.LastError()}")

To do this, write the rights to the user variable via the Rights property and send the update to the server via the [UserUpdate](Manager-Interface/Users/UserUpdate.md) function while checking the result for errors.

Next, change the user password using the [UserPasswordChange](https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userpasswordchange) function:
    
    
    # change user password
    if not manager.UserPasswordChange(MT5Manager.MTUser.EnUsersPasswords.USER_PASS_MAIN,
                                      user.Login, "2Ar#pqkj"):
        print(f"Failed to update user password: {MT5Manager.LastError()}")

As a result of executing the script, we get the following output:
    
    
    User 15770 was added
    Balance operation succeeded
    Found user 15770, balance: 100.0

<a id="example-request-deals"></a>
### Requesting user's deal history (#example-request-deals)

Let's look at how to receive user transactions from the server and handle their type.
    
    
    # include the library
    import MT5Manager
    # include library for handling dates
    import datetime
    # create manager interface
    manager = MT5Manager.ManagerAPI()
    # connect the server
    if manager.Connect("192.168.1.100:443", 1002, "1Ar#pqkj", 0):
        # request deal history up to the current moment
        date_to = datetime.datetime.now()
        # request deal history for last 100 days
        date_from = date_to - datetime.timedelta(days=400)
        # request deal history
        deals = manager.DealRequest(1065, date_from, date_to)
        if deals == False:
            # request failed with error
            print(f"Failed to request deals: {MT5Manager.LastError()}")
        else:
            # display total number of deals
            print(f"Get {len(deals)} deals")
            # display all balance deals
            for deal in deals:
                if deal.Action == MT5Manager.MTDeal.EnDealAction.DEAL_BALANCE:
                    print(deal.Print())
        # disconnect from the server
        manager.Disconnect()
    else:
        # failed to connect to the server
        print(f"Failed to connect to server: {MT5Manager.LastError()}")

This example uses the datetime module to specify a period of time to receive historical data:
    
    
    # include library for handling dates
    import datetime

Request data on transactions for the last 100 days. To do this, create two variables with time now and 100 days ago:
    
    
    # request deal history up to the current moment
        date_to = datetime.datetime.now()
        # request deal history for last 100 days
        date_from = date_to - datetime.timedelta(days=100)

Request deal history for last 100 days using the [DealRequest](Manager-Interface/Trade-Databases/Deals/DealRequest.md) method for a user with login 1065:
    
    
    # request deal history
        deals = manager.DealRequest(1065, date_from, date_to)
        if deals == False:
            # request failed with error
            print(f"Failed to request deals: {MT5Manager.LastError()}")

In case of a failure, DealRequest returns False. Use this to check whether the function completed successfully. If executed successfully, we receive a list with transactions in variables of the [MTDeal](https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_deal/imtdeal) type. The resulting list can be used like any other list in Python. For example, let's check all deals and display a short description for balance transactions:
    
    
    for deal in deals:
                if deal.Action == MT5Manager.MTDeal.EnDealAction.DEAL_BALANCE:
                    print(deal.Print())

As a result of executing the script, we receive the following output if the requested user has balance deals:
    
    
    Got 125 deals
    #86 balance 100.00 [Deposit]
    #92 balance -100.00 [Withdrawal]
    #111 balance 10.00 [Deposit]
    #115 balance -9.72 [Withdrawal]
    #116 balance 1.00 [Deposit]
    #119 balance 100.00 [Deposit]

<a id="example-position-events"></a>
### Subscription to position additions and changes (#example-position-events)

Let's look at how to receive notifications about changes in user's trading positions.
    
    
    # include the library
    import MT5Manager
    # include module to use delays
    import time
    # create class to track positions
    class PositionSink:
        # add position
        def OnPositionAdd(self, position):
            print(f"Position added: {position.Print()}")
        # update position
        def OnPositionUpdate(self, position):
            print(f"Position updated: {position.Print()}")
    # create manager interface
    manager = MT5Manager.ManagerAPI()
    # create class to track positions
    sink = PositionSink()
    # subscribe to position changes
    if not manager.PositionSubscribe(sink):
        print(f"Failed to subscribe: {MT5Manager.LastError()}")
    else:
        # connect the server
        if manager.Connect("192.168.1.100:443", 1002, "1Ar#pqkj",
                           MT5Manager.ManagerAPI.EnPumpModes.PUMP_MODE_POSITIONS,
                           300000):
            # connected to the server
            print("Connected to server")
            # watch position changes within 60 seconds
            for s in range(6):
                time.sleep(10)
                print(".")
            # disconnect from the server
            manager.Disconnect()
        else:
            # failed to connect to the server
            print(f"Failed to connect to server: {MT5Manager.LastError()}")
        # unsubscribe from position changes
        if not manager.PositionUnsubscribe(sink):
            print(f"Failed to unsubscribe: {MT5Manager.LastError()}")

Let's take a closer look. We need to set [MT5Manager.ManagerAPI.EnPumpModes.PUMP_MODE_POSITIONS](Manager-Interface/Connection-to-the-Server/Pumping-Modes.md) pumping mode to receive position data when connecting to the server.

Create the PositionSink class to track position changes:
    
    
    # create class to track positions
    class PositionSink:
        # add position
        def OnPositionAdd(self, position):
            print(f"Position added: {position.Print()}")
        # update position
        def OnPositionUpdate(self, position):
            print(f"Position updated: {position.Print()}")

Add the [OnPositionAdd](../Database-Interfaces/Trade/Positions/IMTPositionSink/OnPositionAdd.md) and [OnPositionUpdate](../Database-Interfaces/Trade/Positions/IMTPositionSink/OnPositionUpdate.md) functions. Signatures and names should strictly match the methods of the [IMTPositionSink](../Database-Interfaces/Trade/Positions/IMTPositionSink.md) class.

Let's create a variable of the PositionSink type and subscribe to manager changes using the [PositionSubscribe](Manager-Interface/Trade-Databases/Positions/PositionSubscribe.md) method:
    
    
    # create class to track positions
    sink = PositionSink()
    # subscribe to position changes
    if not manager.PositionSubscribe(sink):
        print(f"Failed to subscribe: {MT5Manager.LastError()}")

Next, connect to the server and wait for position changes within one minute. Position updates come from another thread, but there is no need to use thread synchronization primitives since all Python code runs under GIL (Global Interpreter Lock). To understand when tracking positions began, we will display a message about a successful connection to the server. Let's display "." once every 10 seconds to make sure the program runs:
    
    
    # connect the server
        if manager.Connect("192.168.1.100:443", 1002, "1Ar#pqkj",
                           MT5Manager.ManagerAPI.EnPumpModes.PUMP_MODE_POSITIONS,
                           300000):
            # connected to the server
            print("Connected to server")
            # watch position changes within 60 seconds
            for s in range(6):
                time.sleep(10)
                print(".")
            # disconnect from the server
            manager.Disconnect()

As a result of executing the script, we will get the following output if, while waiting, we add and change positions through the manager or client terminal:
    
    
    Connected to server
    Position added: #13111682 sell 0.0019 EURUSD 1.06567
    Position updated: #13111682 sell 0.0019 EURUSD 1.06567
    Position added: #13111684 buy 0.0019 EURUSD 1.06563
    Position updated: #13111684 buy 0.0019 EURUSD 1.06563
    Position updated: #13111684 buy 0.0038 EURUSD 1.065635
    Position added: #13111687 sell 0.0057 EURUSD 1.06562
    Position updated: #13111687 sell 0.0057 EURUSD 1.06562
    .
    Position added: #13111695 sell 0.0016 EURUSD 1.06563
    Position updated: #13111695 sell 0.0016 EURUSD 1.06563
    .
    Position added: #13111697 buy 0.0016 EURUSD 1.06563
    Position updated: #13111697 buy 0.0016 EURUSD 1.06563
    .
    .
    .
    .

Keep in mind that according to the documentation of the native ManagerAPI, all methods of the event processing interfaces (in this case OnPositionAdd and OnPositionUpdate) are called from the network thread. Therefore, any methods of the same manager or administrator interface, which send commands to the trade server (such as *Request, *Update, *Delete, *Send, etc.) are prohibited in these interfaces. Only methods working with local data (*Get, *Next, *Total, etc.) can be called from event handlers.

<a id="example-get-ticks"></a>
### Receiving ticks (#example-get-ticks)

Receiving ticks is completely similar to subscribing to position updates provided above.
    
    
    # include the library
    import MT5Manager
    # include module to use delays
    import time
    # include module for handling dates
    import datetime
    # create class to track quotes
    class TickSink:
        # new quote
        def OnTick(self, symbol, tick : MT5Manager.MTTickShort):
            print(f"tick: {symbol} \t {tick.bid:.5f} \t {tick.ask:.5f}")
        # update statistical data on prices
        def OnTickStat(self, stat : MT5Manager.MTTickStat):
            print(f"stat: {datetime.datetime.fromtimestamp(stat.datetime)} \t "
                  f"{stat.bid_high} \t {stat.bid_low} \t {stat.ask_high} \t {stat.ask_low}")
    # create manager interface
    manager = MT5Manager.ManagerAPI()
    # create class to track quotes
    sink = TickSink()
    # subscribe to quote changes
    if not manager.TickSubscribe(sink):
        print(f"Failed to subscribe: {MT5Manager.LastError()}")
    else:
        # connect the server
        # enable pumping of symbols, this will allow to add EURUSD to the list of selected symbols
        if manager.Connect("192.168.1.100:443", 1002, "1Ar#pqkj", MT5Manager.ManagerAPI.EnPumpModes.PUMP_MODE_SYMBOLS):
            # connected to the server
            print("Connected to server")
            # Add "EURUSD" to the list of selected symbols in order to receive the quotes
            if not manager.SelectedAdd("EURUSD"):
                print(f"Failed to select symbol: {MT5Manager.LastError()}")
            # expect data within a minute
            time.sleep(60)
            # disconnect from the server
            manager.Disconnect()
        else:
            # failed to connect to the server
            print(f"Failed to connect to server: {MT5Manager.LastError()}")
        # unsubscribe from changes
        if not manager.TickUnsubscribe(sink):
            print(f"Failed to unsubscribe: {MT5Manager.LastError()}")

There is no need to enable pumping mode here. Just like in the native Manager API, data is received only for the selected symbols.

As a result of executing the script, we get the following output:
    
    
    Connected to server
    stat: 2023-09-22 12:55:07        0.86648         0.86313         0.8666          0.86342
    tick: AUDCAD     0.86642         0.86653
    stat: 2023-09-22 12:55:06        1.0668          1.06149         1.0668          1.0615
    tick: EURUSD     1.06484         1.06484
    stat: 2023-09-22 12:55:07        1.22941         1.22509         1.22956         1.22511
    tick: GBPUSD     1.22677         1.22681
    stat: 2023-09-22 12:54:55        148.383         147.47          148.413         147.5
    tick: USDJPY     148.21400       148.244
    stat: 2023-09-22 02:59:50        0.64512         0.6387          0.64542         0.639
    tick: AUDUSD     0.64130         0.64160
    stat: 2023-09-22 12:55:07        1.34824         1.34584         1.34864         1.34623
    tick: USDCAD     1.34679         1.34719
    tick: USDCAD     1.34678         1.34718
    tick: USDCAD     1.34679         1.34719
    tick: AUDCAD     0.86641         0.86652
    tick: USDCAD     1.34678         1.34718
    tick: USDCAD     1.34679         1.34719
    tick: AUDCAD     0.86641         0.86653
    tick: USDCAD     1.34680         1.34720
    tick: GBPUSD     1.22676         1.22681
    tick: AUDCAD     0.86641         0.86654
    tick: AUDCAD     0.86641         0.86653
    tick: USDCAD     1.34679         1.34719
    tick: GBPUSD     1.22676         1.22680
    tick: EURUSD     1.06483         1.06483
    tick: AUDCAD     0.86642         0.86654
