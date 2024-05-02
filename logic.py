def solucao():
    try:
        a = float(input("valor a11: "))
        b = float(input("valor a12: "))
        c = float(input("valor a21: "))
        d = float(input("valor a22: "))
        x = float(input("Resultado 1:"))
        y = float(input("Resultado 2:"))

        '''
        Matriz A  Matriz B  Matriz C
        | a  b |  | x  b |  | a  x |
        | c  d |  | y  d |  | c  y |
        '''

        det_a = (a*d)-(b*c)
        det_b = (x*d)-(b*y)
        det_c = (a*y)-(c*x)

        if det_a and det_b and det_c == 0:
            return("Sistema possível e indeterminado (SPI)")
        elif det_a and det_b and det_c != 0:
            print("Sistema possível e determinado (SPD)")
        else:
            print("Sistema Impossível (SI)")
    except ValueError:
        pass

def main():
    resultado = solucao()

main()