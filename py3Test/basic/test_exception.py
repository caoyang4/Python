def x():
    try:
        i = 2
    except (IOError, IndentationError) as e:
        print(e)