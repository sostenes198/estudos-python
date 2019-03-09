from builtins import TypeError


def error(x):
    try:
        eval(x)
    except (TypeError, NameError) as e:
        print("Type Error")
        print("Name Error")
    except ValueError as e:
        print("Value Error")
    except ZeroDivisionError as e:
        print("Zero Division Error")
    else:
        print("Nenhuma exceção ocorreu")
    finally:
        print("Foi executado mesmooo")

#Type error
error("int + int")

#NameError
error("a")

#Value Error
error("int('a')")

#ZeroDivisionError
error("5/0")

error("10+10")