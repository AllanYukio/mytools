PI_INT=  '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
E_INT='7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'

def pi_real(numero):
    global PI_INT
    if 0<numero<=100:
        pi='3,'+PI_INT[0:numero]
    elif numero==0:
        pi=3
    return pi


def e_real(numero):
    global E_INT
    if 0<numero<=100:
        e='2,'+E_INT[0:numero]
    elif numero==0:
        e=2
    return e



