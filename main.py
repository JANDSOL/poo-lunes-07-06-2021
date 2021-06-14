# number = 45
# if type(number) == int:
#     print("~ Resultado:", number * 2)
# else:
#     print("~ Este dato NO es numérico.")

# def message(men):
#     print(men)


# message(" ! Primer Programa.")
# message(" ! Segundo Programa.")


class Sintax:
    def __init__(self, data = "~ Iniciando..."):
        self.word = data

    def useVariables(self):
        age, _weight = 19, 50
        name = "Juan Andrade"
        type_sex = "Masculino"
        single = True
        print(" ! Nombre: {}".format(name))
        print(" ! Edad: {}".format(age))
        print(" ! Tipo de Sexo: {}".format(type_sex))
        print(" ! Soltero: {}".format(single))
        print(" ! Peso: {}kg".format(_weight))


# exercise2 = Sintax()
# print(exercise2.word)
# exercise2.useVariables()


class Sintax:
    def __init__(self, data = "~ Iniciando..."):
        self.word = data

    def useVariables(self):
        # age, _weight = 19, 50
        # name = "Juan Andrade"
        # type_sex = "Masculino"
        # single = True
        # print(" ! Nombre: {}".format(name))
        # print(" ! Edad: {}".format(age))
        # print(" ! Tipo de Sexo: {}".format(type_sex))
        # print(" ! Soltero: {}".format(single))
        # print(" ! Peso: {}kg".format(_weight))
        
        # () -> Data type Tuple.
        user = ()
        user = ("jpas23", 2001, "jpas.juan23@gmail.com", True)

        # [] -> Data type List.
        subjects = []
        subjects = ["Programacion Web", "PHP", "Cobol"]
        subjects[1] = "Python"
        subjects.append("Go")

        # {} -> Data type Dictionary.
        teacher = {}
        teacher = {"Nombre": "Luis", "Edad": 20, "Fac.": "FACI"}
        teacher["Carrera"] = "CS"

        # Print with .format().
        # print("""Me llamo {}, y tengo {}
        #          años""".format(nombre, edad))

        # Structures Slices.
        print(user, subjects, teacher)
        print(user, user[0], user[0:2], user[-1])
        print(subjects, subjects[2:], subjects[:1], subjects[::], subjects[-2:])
        print(teacher, teacher["Nombre"])


exercise3 = Sintax()
exercise3.useVariables()
