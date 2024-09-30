import string
import secrets

alphabet = string.ascii_letters + string.digits

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    
    # Verificar requisitos de la contraseña
    if (any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        sum(c.isdigit() for c in password) >= 3):
        break

print("Contraseña generada:", password)


with open('contraseñas.txt', 'a') as f:
    f.write(password + '\n')

with open('contraseñas.txt', 'r') as f:
    mensaje = f.read()
    print("Contraseñas guardadas en el archivo:")
    print(mensaje)
