from msilib.schema import Error


def principal():
    print(f"The name of this module is : {__name__}")


if __name__ == '__main__':
    try:
        principal()
    except Error as e:
        print(e)
