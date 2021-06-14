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


exercise2 = Sintax()
print(exercise2.word)
exercise2.useVariables()
