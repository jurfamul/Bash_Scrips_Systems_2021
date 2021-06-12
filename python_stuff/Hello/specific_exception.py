#!/user/bin/python3
is_running = True
while is_running:
    uInput = input("Enter an integer: ")
    uInt = None
    try:
        uInt = int(uInput)

    except ValueError as err:
        print("Error: {0} is not an integer.".format(uInput))
        print(str(err))
    except Exception as err:
        print("Something else went wrong. Exception type: {0}, error message: {1}"
              .format(type(err), str(err)))

    finally:
        if uInt != None:
            print("Integer detected. Exiting Program.")
            is_running = False
