#Libraries
from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import imutils
import mediapipe as mp
import math
import os
import face_recognition as fr
from tkinter import messagebox
import sys
import mysql.connector
from datetime import datetime, timedelta, time
import locale

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Usar las rutas adaptadas para PyInstaller
predictor_path = resource_path("face_recognition_models/models/shape_predictor_68_face_landmarks.dat")
face_detector_path = resource_path("face_recognition_models/models/mmod_human_face_detector.dat")

# Inicializar las variables con algún valor predeterminado
xi, yi, anc, alt = 0, 0, 0, 0

def reset_values():
    global step, UserName, conteo, facess, facescod  # Usa 'global' para modificar variables globales
    conteo = 0
    step = 0
    UserName = ""
    facess = []
    facescod = []

#FUNCION PARA ALERTAR PARA REPORTAR AL MOMENTO DE MARCAR ASISTENCIA
def empleado_ya_tiene_asistencia():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showerror("Error", "Ya tiene asistencia registrada para el dia de hoy.")

def mostrar_error_asistencia():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showerror("Error", "Inhabilitado, por favor acercarse a Administracion.")
    root.destroy()

def no_tiene_asistencia():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showerror("Error", "El empleado no tiene asistencia para el dia de hoy.")
    root.destroy()
#-------------------------------------------------------------------

# Añadimos una nueva función para mostrar mensaje de registro
def mostrar_mensaje_registro():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Empleado no registrado", "No se encuentra registrado en el sistema.\nPor favor, acérquese a Administración para registrarse.")
    root.destroy()

# Función para dibujar elementos (rectángulos y círculos):
def draw_elements_on_frame(frame, xi, yi, anc, alt, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, color=(255, 0, 0)):
    cv2.rectangle(frame, (xi, yi, anc, alt), (255, 255, 255), 2)
    cv2.circle(frame, (x1, y1), 2, color, cv2.FILLED)
    cv2.circle(frame, (x2, y2), 2, color, cv2.FILLED)
    cv2.circle(frame, (x3, y3), 2, color, cv2.FILLED)
    cv2.circle(frame, (x4, y4), 2, color, cv2.FILLED)
    cv2.circle(frame, (x5, y5), 2, color, cv2.FILLED)
    cv2.circle(frame, (x6, y6), 2, color, cv2.FILLED)
    cv2.circle(frame, (x7, y7), 2, color, cv2.FILLED)
    cv2.circle(frame, (x8, y8), 2, color, cv2.FILLED)

#Close window Funcions
def Close_Window2():
    global step, conteo
    #Reseteamos las variblaes
    conteo = 0
    step = 0
    pantalla3.destroy()

# Mostramos mensaje alerta de salida
def conectar_bd():  
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3307,  # Puerto personalizado
            user="root",
            password="",
            database="asistencia_dreamli"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def Salida():
    global UserName

    conexion = conectar_bd()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, apellidos FROM empleados WHERE documento = %s", (UserName,))
            resultado = cursor.fetchone()

            if resultado:
                nombre, apellidos = resultado
                messagebox.showinfo("👋 Hasta pronto", f"{nombre} {apellidos}, ¡has registrado tu salida correctamente!")
            else:
                messagebox.showwarning("❌ Usuario no encontrado", "No se pudo registrar la salida. El usuario no está en la base de datos.")

        except mysql.connector.Error as err:
            messagebox.showerror("🚫 Error de base de datos", f"No se pudo consultar la base de datos:\n{err}")
        finally:
            cursor.close()
            conexion.close()
    else:
        messagebox.showerror("🚫 Error de conexión", "No se pudo conectar a la base de datos.")

def Entrada():
    global UserName

    conexion = conectar_bd()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, apellidos FROM empleados WHERE documento = %s", (UserName,))
            resultado = cursor.fetchone()

            if resultado:
                nombre, apellidos = resultado
                messagebox.showinfo("✅ Acceso permitido", f"¡Bienvenido {nombre} {apellidos}!")
            else:
                messagebox.showwarning("❌ Usuario no encontrado", "El usuario no está registrado en la base de datos.")

        except mysql.connector.Error as err:
            messagebox.showerror("🚫 Error de base de datos", f"No se pudo consultar la base de datos:\n{err}")
        finally:
            cursor.close()
            conexion.close()
    else:
        messagebox.showerror("🚫 Error de conexión", "No se pudo conectar a la base de datos.")

#Profile: Es mostrar el perfil
def Profile():

    global step, conteo, UserName, NuevaCarpetaRostros, OutFolderPathUser
    # Reset Variable: Reseteamos las variables
    step = 0
    conteo = 0

    # Creamos nuestra nueva ventana : Window
    pantalla4 = Toplevel(ventana)
    pantalla4.title("PROFILE")
    pantalla4.geometry("1280x720")

    # Fondo
    bc = Label(pantalla4, image=imagenbc, text="Inicio")
    bc.place(x=0, y=0, relheight=1, relwidth=1)

    # Conexión a la base de datos
    conexion = conectar_bd()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            # Consulta para obtener los datos del documento desde la base de datos
            cursor.execute("SELECT nombre, apellidos, documento, foto FROM empleados WHERE documento = %s", (UserName,))
            resultado = cursor.fetchone()

            if resultado:
                # Extraemos los datos del documento
                Name, Apell, User, Foto = resultado

                # Mostramos el mensaje de bienvenida
                texto1 = Label(pantalla4, text=f"BIENVENIDO {Name} {Apell}", font=("Helvetica", 16, "bold"), bg="#f0f4f7")
                texto1.place(x=580, y=50)

                # Label para la imagen
                lblimage = Label(pantalla4)
                lblimage.place(x=490, y=80)

                # Cargamos la imagen del usuario desde la carpeta `Assets/img/`
                ruta_imagen = f"Assets/img/faces/{Foto}"
                if os.path.exists(ruta_imagen):  # Verificamos si la imagen existe
                    ImgUser = cv2.imread(ruta_imagen)
                    ImgUser = cv2.cvtColor(ImgUser, cv2.COLOR_BGR2RGB)
                    ImgUser = Image.fromarray(ImgUser)

                    IMG = ImageTk.PhotoImage(image=ImgUser)
                    # Configuramos el label para mostrar la imagen
                    lblimage.configure(image=IMG)
                    lblimage.image = IMG
                else:
                    # Si no se encuentra la imagen, mostramos un mensaje de error
                    texto_error = Label(pantalla4, text="Imagen no encontrada", font=("Helvetica", 12), fg="red", bg="#f0f4f7")
                    texto_error.place(x=490, y=300)
            else:
                # Si no se encuentra el usuario en la base de datos
                texto_error = Label(pantalla4, text="Usuario no encontrado en la base de datos", font=("Helvetica", 12), fg="red", bg="#f0f4f7")
                texto_error.place(x=490, y=300)

        except mysql.connector.Error as err:
            print(f"Error al consultar la base de datos: {err}")
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo conectar a la base de datos")

#Funcion para registrar una nueva asistencia de los empleadoes
def registrar_asistencia_mysql(username):
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # En lugar de 'es_ES.UTF-8'
    now = datetime.now()
    datenow = now.date()
    timenow = now.time()
    dia_semana = now.strftime('%A').capitalize()

    conexion = conectar_bd()

    if conexion is None:
        print("No se pudo conectar a la base de datos")
        return 1

    cursor = conexion.cursor(buffered=True)  # Añadido buffered=True para manejar resultados no leídos

    try:
        # Obtener ID del empleado
        cursor.execute("SELECT id FROM empleados WHERE documento=%s", (username,))
        empleado = cursor.fetchone()
        if not empleado:
            print(f"No se encontró al empleado con documento {username}")
            return 1

        empleado_id = empleado[0]

        # Verificar si el empleado está activo
        cursor.execute("SELECT estado FROM empleados WHERE id=%s AND estado=1", (empleado_id,))
        if not cursor.fetchone():
            print(f"{username} Inhabilitado a las {now}, por favor acercarse a Administración")
            return 1
        
        # Verificar si el empleado tiene horario asignado para el día de hoy
        cursor.execute("""
            SELECT h.hora_entrada 
            FROM empleado_horario eh 
            INNER JOIN horarios h ON eh.horario_id = h.id 
            WHERE eh.empleado_id = %s AND eh.dia_semana = %s
        """, (empleado_id, dia_semana))
        hora_entrada_snf = cursor.fetchone()

        if not hora_entrada_snf:
            print(f"{username} no tiene horario asignado para el día {dia_semana}. Consultar con Administración.")
            return 2  # Detenemos la ejecución si no tiene horario asignado

        # Verificar si ya marcó asistencia hoy
        cursor.execute("SELECT id, hora_salida FROM asistencia WHERE empleado_id=%s AND fecha=%s", (empleado_id, datenow))
        asistencia = cursor.fetchone()

        if asistencia and asistencia[1] is None:  # Si existe asistencia y no tiene hora de salida
            # Registrar salida
            cursor.execute("UPDATE asistencia SET hora_salida=%s WHERE empleado_id=%s AND fecha=%s",
                           (timenow, empleado_id, datenow))
            print(f"Salida registrada para {username} a las {timenow}")
            conexion.commit()
            return 4

        elif asistencia and asistencia[1] is not None:  # Si ya tiene hora de salida
            print(f"{username} ya marcó su salida hoy.")
            return 3 # Detenemos la ejecución si ya marcó su salida

        elif not asistencia:
            # Obtener hora de entrada del horario       
            cursor.execute("""
                SELECT h.hora_entrada 
                FROM empleado_horario eh 
                INNER JOIN horarios h ON eh.horario_id = h.id 
                WHERE eh.empleado_id = %s AND eh.dia_semana = %s
            """, (empleado_id, dia_semana))
            hora_entrada_snf = cursor.fetchone()

            if not hora_entrada_snf:
                print("No se encontró el horario del empleado para el día de hoy.")
                return 1

            hora_entrada_str = str(hora_entrada_snf[0])
            hora_entrada_horario = datetime.strptime(hora_entrada_str, "%H:%M:%S").time()

            # Calcular diferencia
            dt_hora_actual = datetime.combine(datenow, timenow)
            dt_hora_entrada = datetime.combine(datenow, hora_entrada_horario)

            # Valores por defecto
            minutos_tarde = "00:00:00"
            estado = "A tiempo"

            if dt_hora_actual > dt_hora_entrada:
                diferencia = dt_hora_actual - dt_hora_entrada
                horas, resto = divmod(diferencia.total_seconds(), 3600)
                minutos, segundos = divmod(resto, 60)
                minutos_tarde = f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}"
                estado = "Tarde"

            #Obtener el bloque de asistencia del empleado
            #En Python, para crear una tupla de un solo elemento, debes agregar una coma al final. De lo contrario,
            #  se pasa como un simple valor (no tupla), y eso puede lanzar errores o comportarse inesperadamente.
            cursor.execute("SELECT bloque FROM empleado_horario WHERE empleado_id = %s", (empleado_id,))
            bloque_result = cursor.fetchone()
        
            #bloque_result[0]: porque fetchone() devuelve una tupla como (bloque,).
            #if bloque_result else None: asegura que no explote si no hay resultados (buena práctica).
            bloque = bloque_result[0] if bloque_result else None

            # Insertar asistencia
            cursor.execute("""
                INSERT INTO asistencia (empleado_id, fecha, hora_entrada, minutos_tarde, estado, bloque) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (empleado_id, datenow, timenow, minutos_tarde, estado, bloque))

            print(f"{username} registrado a las {now.strftime('%H:%M:%S')} con {minutos_tarde} de tardanza. Estado: {estado}, en el bloque: {bloque}, con hora de entrada {hora_entrada_horario}")

        # ✔️ CONFIRMAR CAMBIOS
        conexion.commit()

    except Exception as e:
        print(f"Error al registrar asistencia: {e}")
        conexion.rollback()
        return 1

    finally:
        cursor.close()
        conexion.close()

    return 0

# Función para validar el login
def validar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Validamos que el usuario y la contraseña sean correctos
    if not usuario or not contrasena:
        messagebox.showerror("Error de login", "Por favor rellenar todos los campos")

    elif usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Login correcto", "¡Bienvenido!")
        Sign()
        
    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

#Code Faces  Functions
def Code_Face(images):
    #List
    listacod = []
    # Iteramos 
    for img in images:
        #Color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #COdificamos la imagen
        cod = fr.face_encodings(img)[0]
        #Guardamos en lista: Save List
        listacod.append(cod)
    return listacod

def Sign_Biometric():
    global NuevaCarpetaRostros, OutFolderPathFace, step, cap, lblVideo, pantalla3, FaceCode, clases, images, pantalla2, parpadeo, conteo, UserName

    # Verificamos si la captura de video existe
    if cap is not None:
        ret, frame = cap.read()

        if ret:
            frameSave = frame.copy()
            frame = imutils.resize(frame, width=1280)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Procesamos la malla facial
            res = FaceMesh.process(frameRGB)

            px, py, lista = [], [], []

            if res.multi_face_landmarks:
                for rostros in res.multi_face_landmarks:
                    mpDraw.draw_landmarks(frame, rostros, FacemeshObject.FACEMESH_TESSELATION, ConfigDraw, ConfigDraw)

                    for id, puntos in enumerate(rostros.landmark):
                        al, an, c = frame.shape
                        x, y = int(puntos.x * an), int(puntos.y * al)
                        px.append(x)
                        py.append(y)
                        lista.append([id, x, y])

                    # Solo si tenemos todos los puntos clave
                    if len(lista) == 468:
                        x1, y1 = lista[145][1:]
                        x2, y2 = lista[159][1:]
                        longitud1 = math.hypot(x2 - x1, y2 - y1)

                        x3, y3 = lista[374][1:]
                        x4, y4 = lista[386][1:]
                        longitud2 = math.hypot(x4 - x3, y4 - y3)

                        x5, y5 = lista[139][1:]
                        x6, y6 = lista[368][1:]
                        x7, y7 = lista[70][1:]
                        x8, y8 = lista[300][1:]

                        faces = detector.process(frameRGB)

                        # Si se detectan caras
                        if faces.detections is not None:  # Verifica si se detectaron rostros en el frame
                            for face in faces.detections:  # Itera sobre cada rostro detectado
                                score = face.score[0]  # Obtiene la puntuación de confianza de la detección
                                bbox = face.location_data.relative_bounding_box  # Obtiene las coordenadas del cuadro delimitador relativo

                                if score > confThreshold:  # Verifica si la confianza de la detección supera el umbral definido
                                    # Calcula las coordenadas del cuadro delimitador en píxeles
                                    xi = int(bbox.xmin * an)  # Coordenada X inicial (escalada al ancho del frame)
                                    yi = int(bbox.ymin * al)  # Coordenada Y inicial (escalada al alto del frame)
                                    anc = int(bbox.width * an)  # Ancho del cuadro delimitador (escalado al ancho del frame)
                                    alt = int(bbox.height * al)  # Alto del cuadro delimitador (escalado al alto del frame)

                                    # Aplica un offset horizontal al cuadro delimitador
                                    offsetan = (offsetx / 100) * anc  # Calcula el offset como un porcentaje del ancho del cuadro
                                    xi = int(xi - int(offsetan / 2))  # Ajusta la coordenada X inicial para centrar el offset
                                    anc = int(anc + offsetan)  # Ajusta el ancho del cuadro para incluir el offset

                                    # Aplica un offset vertical al cuadro delimitador
                                    offsetal = (offsety / 100) * alt  # Calcula el offset como un porcentaje del alto del cuadro
                                    yi = int(yi - offsetal)  # Ajusta la coordenada Y inicial para incluir el offset
                                    alt = int(alt + offsetal)  # Ajusta el alto del cuadro para incluir el offset

                                    # Asegura que las coordenadas y dimensiones no sean negativas
                                    if xi < 0: xi = 0  # Si la coordenada X inicial es negativa, la ajusta a 0
                                    if yi < 0: yi = 0  # Si la coordenada Y inicial es negativa, la ajusta a 0
                                    if anc < 0: anc = 0  # Si el ancho es negativo, lo ajusta a 0
                                    if alt < 0: alt = 0  # Si el alto es negativo, lo ajusta a 0

                                    # Validamos los pasos step 0 y step 1
                                    if step == 0:
                                        # Dibujar rectángulo y agregar imágenes de pasos
                                        cv2.rectangle(frame, (xi, yi, anc, alt), (255, 0, 255), 2)

                                        als0, ans0, c = img_step0.shape
                                        frame[50:50 + als0, 50:50 + ans0] = img_step0

                                        als1, ans1, c = img_step1.shape
                                        frame[50:50 + als1, 1030:1030 + ans1] = img_step1

                                        als2, ans2, c = img_step2.shape
                                        frame[270:270 + als2, 1030:1030 + ans2] = img_step2

                                        # Validar que la persona está mirando de frente
                                        if x7 > x5 and x8 < x6:
                                            alch, anch, c = img_check.shape
                                            frame[165:165 + alch, 1105:1105 + anch] = img_check

                                            # Detectar parpadeos
                                            if longitud1 <= 15 and longitud2 <= 15 and not parpadeo:
                                                conteo += 1
                                                parpadeo = True
                                            elif longitud1 > 15 and longitud2 > 15 and parpadeo:
                                                parpadeo = False
                                            
                                            cv2.putText(frame, f'Parpadeo: {int(conteo)}', (1070, 375), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                                            # Validar el conteo de parpadeos
                                            if conteo >= 3:
                                                #colocamos la imagen IMG CHECK
                                                alch, anch, c = img_check.shape
                                                #lo ubicamos en nuestro frame
                                                frame[385:385 + alch, 1105:1105 + anch] = img_check

                                                #CUando estan abierto los ojos tomamos la foto :OPen eyes
                                                #Esto tambien depende de la umbral de la camara
                                                if longitud1 > 26 and longitud2 > 26:
                                                    #Step 1
                                                    step = 1
                                        else:
                                            conteo = 0

                                    elif step == 1:
                                        # Dibujar rectángulo verde cuando ya se ha verificado
                                        cv2.rectangle(frame, (xi, yi, anc, alt), (0, 255, 0), 2)

                                        alli, anli, c = img_liche.shape #AQUI ESTA LA IMAGEN DE VALIDACIOn
                                        frame[50:50 + alli, 50:50 + anli] = img_liche #AQUI ESTA LA IMAGEN DE VALIDACIOn

                                        # fr.face_locations detecta las ubicaciones de los rostros en el frame.
                                        facess = fr.face_locations(frameRGB)
                                        #fr.face_encodings genera codificaciones (vectores de características) para los rostros detectados.
                                        facescod = fr.face_encodings(frameRGB, facess)

                                        # Comparar los rostros encontrados
                                        for facecod, facesloc in zip(facescod, facess):
                                            match = fr.compare_faces(FaceCode, facecod)  # Compara el rostro detectado con los registrados
                                            simi = fr.face_distance(FaceCode, facecod)  # Calcula la distancia de similitud entre los rostros
                                            min_idx = np.argmin(simi)  # Encuentra el índice del rostro más similar
                                            if match[min_idx]:
                                                UserName = clases[min_idx].upper()
                                                respuesta = registrar_asistencia_mysql(UserName)
                                                if respuesta == 1:
                                                    mostrar_error_asistencia()
                                                    reset_values()

                                                elif respuesta == 2:
                                                    no_tiene_asistencia()
                                                    reset_values()

                                                elif respuesta == 3:
                                                    empleado_ya_tiene_asistencia()
                                                    reset_values()

                                                elif respuesta == 4:
                                                    Salida()
                                                    reset_values()

                                                else:        
                                                    Entrada()    
                                                    reset_values()    
                                                                 
                #CON ESTO SALE EL ERROR CUANDO LOS PUNTOS SE PIERDEN EN UNA ESQUINA INFERIOR
                # draw_elements_on_frame(frame, xi, yi, anc, alt, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8)

        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, Sign_Biometric)

    else:
        cap.release()

#Creamos nuestra funcion Sign
def Sign():
    global LogUser, LogPass, NuevaCarpetaRostros, cap, lblVideo, pantalla3, FaceCode, clases, images, ventana
    #Primero extraemos los nombres: Extract: Name,  User, Password
    #LogUser, LogPass = InputUserLog.get(), InputPassLog.get()
    
    #DB Faces
    images = []
    clases = []
    lista = os.listdir(NuevaCarpetaRostros)

    # Read Images . Leemos las imagenes
    for lis in lista:
        #Read img
        imgdb = cv2.imread(f"{NuevaCarpetaRostros}/{lis}")
        #Save Img DB
        images.append(imgdb)
        # Name Img
        clases.append(os.path.splitext(lis)[0])
    
    # Face Code: Imagenes codificadas
    FaceCode = Code_Face(images)

    #Creamos nuestra nueva ventana : Window
    pantalla3 = Toplevel(ventana)
    pantalla3.title("BIOMETRIC SIGN UP")
    pantalla3.geometry("1280x720")

    # Label Video
    lblVideo = Label(pantalla3)
    lblVideo.place(x=0, y=0)

    # Creamos la video captura : Videocapture
    #Direccionamos a una nueva funcion
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 1280)
    cap.set(4, 720)
    Sign_Biometric()
    
############################################################################
# Crear la ventana principal
ventana = Tk()
ventana.title("Login")

# Establecer un tamaño inicial para la ventana
ventana.geometry("450x350")
ventana.configure(bg="#f0f4f7")  # Color de fondo claro

# Actualizar las tareas pendientes para obtener el tamaño real de la ventana
ventana.update_idletasks()

# Obtener el tamaño de la ventana
ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular la posición x, y para centrar la ventana
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# Establecer la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
############################################################################

#Leer las miamgenes: Estas imagenes obligatoriamente aparecen 
img_info = cv2.imread("C:/xampp/htdocs/python/SetUp/Info.png")
img_check = cv2.imread("C:/xampp/htdocs/python/SetUp/check.png")
img_step0 = cv2.imread("C:/xampp/htdocs/python/SetUp/Step0.png")
img_step1 = cv2.imread("C:/xampp/htdocs/python/SetUp/Step1.png")
img_step2 = cv2.imread("C:/xampp/htdocs/python/SetUp/Step2.png")
img_liche = cv2.imread("C:/xampp/htdocs/python/SetUp/LivenessCheck.png")

# Variables
parpadeo = False
conteo = 0
muestra = 0
step = 0

#OffSet
offsety = 40
offsetx = 20


# Threshold : Umbral de presision
confThreshold = 0.5

# Object Face Detect -> Detector de Rostros
FaceObject = mp.solutions.face_detection
detector = FaceObject.FaceDetection(min_detection_confidence=0.5, model_selection=1)

# Tool Drow : Herramienta de dibujo de la malla facial
mpDraw = mp.solutions.drawing_utils
ConfigDraw = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)

#Object Face Mesh
FacemeshObject = mp.solutions.face_mesh
FaceMesh = FacemeshObject.FaceMesh(max_num_faces = 1)


# Object Face Detect -> Detector de Rostros
FaceObject = mp.solutions.face_detection
detector = FaceObject.FaceDetection(min_detection_confidence=0.5, model_selection=1)

#Profile. Fondo para perfil
imagenbc = PhotoImage(file="C:/xampp/htdocs/python/SetUp/Back3.png")

# Path
# Carpeta de lo usuarios
OutFolderPathUser = 'C:/xampp/htdocs/python/Database/Users'
#Esto es para verificar los usuarios
PathUserCheck = 'C:/xampp/htdocs/python/Database/Users/'
# carpeta de los rostros
NuevaCarpetaRostros = 'C:/xampp/htdocs/python/Assets/img/faces'
OutFolderPathFace = 'C:/xampp/htdocs/python/Database/Faces'


# Fuente y color general
fuente_label = ("Helvetica", 12)
fuente_entry = ("Helvetica", 11)
color_label = "#333333"
color_entry_bg = "#ffffff"
color_boton_bg = "#4a90e2"
color_boton_fg = "#ffffff"


# Contenedor central
frame_central = Frame(ventana, bg="#f0f4f7")
frame_central.place(relx=0.5, rely=0.5, anchor=CENTER)

# Etiqueta y campo de usuario
label_usuario = Label(frame_central, text="Usuario:", font=fuente_label, bg="#f0f4f7", fg=color_label)
label_usuario.pack(pady=(0, 5), anchor="w")
entry_usuario = Entry(frame_central, font=fuente_entry, bg=color_entry_bg, width=30, bd=1, relief="solid")
entry_usuario.pack(pady=(0, 15))

# Etiqueta y campo de contraseña
label_contrasena = Label(frame_central, text="Contraseña:", font=fuente_label, bg="#f0f4f7", fg=color_label)
label_contrasena.pack(pady=(0, 5), anchor="w")
entry_contrasena = Entry(frame_central, font=fuente_entry, show="*", bg=color_entry_bg, width=30, bd=1, relief="solid")
entry_contrasena.pack(pady=(0, 20))

# Botón de login
boton_login = Button(frame_central, text="Iniciar Sesión", font=("Helvetica", 11, "bold"),
                     bg=color_boton_bg, fg=color_boton_fg, activebackground="#357ABD",
                     activeforeground="#ffffff", width=20, bd=0, cursor="hand2", command=validar_login)
boton_login.pack()

ventana.mainloop()