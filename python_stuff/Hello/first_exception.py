#!/user/bin/python3
is_running = True
while is_running:
    uInput = input("Enter an integer: ")
    uInt = None
    try:
        uInt = int(uInput)

    except:
        print("Error: {0} is not an integer.".format(uInput))

    finally:
        if uInt != None:
            print("Integer detected. Exiting Program.")
            is_running = False