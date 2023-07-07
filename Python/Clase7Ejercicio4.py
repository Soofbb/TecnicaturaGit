#Etapas de la vida
edad = int(input('Digite su edad: '))
mensaje = None

if 0 <= edad < 10: 
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Empieza la mejor etapa'
elif 40 <= edad < 50:
    mensaje = 'Llegando a los 50, no son nada'
else:
    mensaje = 'Error, etapa de vida no reconocida'
print(f'Tu edad es: {edad}, {mensaje}')    
