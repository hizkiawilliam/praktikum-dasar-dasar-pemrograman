a_str = '1a2b'
for x_str in a_str:
    try:
        x_int = int(x_str)
        print(x_int)
    except ValueError:
        print("Error: " + x_str)
