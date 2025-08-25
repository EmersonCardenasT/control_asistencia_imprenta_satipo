j

# Función para obtener los cargos
# Cargar cargos y configurar Combobox
def configurar_combobox_cargo(combobox):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM cargo")
        resultados = cursor.fetchall()
        conexion.close()

        # Guardar en variable global o asociada
        combobox.cargos = {nombre: id for id, nombre in resultados}
        combobox['values'] = list(combobox.cargos.keys())  # Mostrar solo nombres

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

def registrar_empleado_mysql(nombre, apellido, usuario, telefono, genero, fecha_nacimiento, direccion, email, cargo):
    conexion = conectar_bd()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            # Consulta SQL para registrar datos en la base de datos
            consulta = """INSERT INTO empleados (nombre, apellidos, telefono, documento, genero, fecha_nacimiento, direccion, email, id_cargo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            valores = (nombre, apellido, telefono, usuario, genero, fecha_nacimiento, direccion, email, cargo)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Empleado registrado exitosamente")
            return True  # Registro exitoso
        except mysql.connector.Error as err:
            print(f"Error al conectar a la BD: {err}")
            return False  # Error en el registro
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo conectar a la BD")
        return False  # Error en la conexión

#Conexion a la BD
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

# Función para actualizar el último registro con el nombre de la imagen
def actualizar_foto_en_bd(nombre_usuario, nombre_imagen):
    conexion = conectar_bd()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            # Actualizar el campo `foto` del registro correspondiente
            sql_update = """
                UPDATE empleados 
                SET foto = %s 
                WHERE documento = %s
            """
            cursor.execute(sql_update, (nombre_imagen, nombre_usuario))
            conexion.commit()  # Guardar los cambios
            print("Campo de foto actualizado en la base de datos")
        except mysql.connector.Error as err:
            print(f"Error al actualizar la base de datos: {err}")
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo conectar a la base de datos")

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

#Close window Funcions
def Close_Window():
    global step, conteo
    #Reseteamos las variblaes
    conteo = 0
    step = 0
    pantalla2.destroy()
 
#Log Biometric Function
def Log_Biometric():
    #Declaramos funciones Globales
    global pantalla2, conteo, parpadeo, img_info, step, cap, lblVideo, RegUser
    
    #Verificamos si video Captura
    if cap is not None: #not None Hacemos una doble negacion
        ret, frame = cap.read()

        frameSave = frame.copy()

        # Redimensionamos los frame
        frame = imutils.resize(frame, width=1280)

        #Frame RGB
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Frame Show : Esto es para mostrar el frame en color RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if ret == True:
            # Inferencia de la malla facial Face Mesh
            res = FaceMesh.process(frameRGB)

            # Lista de Resultados
            px = []
            py = []
            lista = []
            if res.multi_face_landmarks:
                #Si tiene detecciones entonces la extraemos
                for rostros in res.multi_face_landmarks:
                    #Dibujamos la malla facial: Draw
                    mpDraw.draw_landmarks(frame, rostros, FacemeshObject.FACEMESH_TESSELATION , ConfigDraw, ConfigDraw)

                    #Extrameos loskeypoint
                    for id, puntos in enumerate(rostros.landmark):
                        #Info img
                        al, an, c = frame.shape
                        x,y =int(puntos.x * an), int(puntos.y * al)
                        px.append(x)
                        py.append(y)
                        lista.append([id, x , y])

                        #Primero preguntamos si tenemos todos los puntos: 468 keypoints
                        if len(lista) == 468:
                            #priermo Ojo derecho
                            x1, y1 = lista[145][1:]
                            x2, y2 = lista[159][1:]
                            longitud1 = math.hypot(x2-x1, y2-y1)

                            #Parpadeo del ojo izquierdo ahora
                            x3, y3 = lista[374][1:]
                            x4, y4 = lista[386][1:]
                            longitud2 = math.hypot(x4-x3, y4-y3)

                            #Parietal Derecho
                            x5, y5 = lista[139][1:]
                            #Parietal Izquierdo
                            x6, y6 = lista[368][1:]
                            
                            #Ceja Derecho
                            x7, y7 = lista[70][1:]
                            #Ceja Izquierdo
                            x8, y8 = lista[300][1:]

                            #Realizamos la detteccion de rostros
                            faces = detector.process(frameRGB)

                            if faces.detections is not None:
                                for faces in faces.detections:
                                    #Recuadro del rostro : Bbox: "ID, BBOX,SCORE"
                                    score = faces.score
                                    score = score[0]
                                    bbox = faces.location_data.relative_bounding_box

                                    #Threshold
                                    if score > confThreshold:
                                        # Pixeles
                                        xi, yi, anc, alt = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                                        xi, yi, anc, alt = int(xi * an), int(yi * al), int(anc * an), int(alt * al)

                                        # offset X
                                        offsetan = (offsetx / 100) * anc
                                        xi = int(xi - int(offsetan/2))
                                        anc = int(anc + offsetan)
                                        xf = xi + anc

                                        # offset Y
                                        offsetal = (offsety / 100) * alt
                                        yi = int(yi - offsetal)
                                        alt = int(alt + offsetal)
                                        yf = yi + alt

                                        # Si sale error : Error
                                        if xi < 0: xi = 0
                                        if yi < 0: yi = 0
                                        if anc < 0: anc = 0
                                        if alt < 0: alt = 0

                                        #Pasos de verificacion: Steps
                                        if step == 0:
                                            #Draw
                                            cv2.rectangle(frame, (xi, yi, anc, alt), (255, 0, 255), 2)
                                            
                                            #IMG Step0
                                            als0, ans0, c = img_step0.shape
                                            #lo ubicamos en nuestro frame
                                            frame[50:50 + als0, 50:50 + ans0] = img_step0

                                            #IMG Step1
                                            als1, ans1, c = img_step1.shape
                                            #lo ubicamos en nuestro frame
                                            frame[50:50 + als1, 1030:1030 + ans1] = img_step1

                                            #IMG Step2
                                            als2, ans2, c = img_step2.shape
                                            #lo ubicamos en nuestro frame
                                            frame[270:270 + als2, 1030:1030 + ans2] = img_step2

                                            #Face center: Validamos que este mirando de frente a la camara
                                            if x7 > x5 and x8 < x6:
                                                #colocamos la imagen IMG CHECK
                                                alch, anch, c = img_check.shape
                                                #lo ubicamos en nuestro frame
                                                frame[165:165 + alch, 1105:1105 + anch] = img_check

                                                #Conteo de parpadeos
                                                #La condicional que trabajamos aqui es depende la ubral de la camara
                                                #se puede realizar a prueba y error hasta encontrar el umbral correcto de la camara
                                                if longitud1 <= 15 and longitud2 <= 15 and parpadeo == False:
                                                    conteo = conteo + 1
                                                    parpadeo = True
                                                
                                                elif longitud1 > 15 and longitud2 > 15 and parpadeo == True:
                                                    parpadeo = False
                                                
                                                cv2.putText(frame, f'Parpadeo: {int(conteo)}', (1070, 375), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                                                #Condicion para validar el conteo
                                                if conteo >= 3:
                                                    #colocamos la imagen IMG CHECK
                                                    alch, anch, c = img_check.shape
                                                    #lo ubicamos en nuestro frame
                                                    frame[385:385 + alch, 1105:1105 + anch] = img_check

                                                    #CUando estan abierto los ojos tomamos la foto :OPen eyes
                                                    #Esto tambien depende de la umbral de la camara
                                                    if longitud1 > 26 and longitud2 > 26:
                                                        # Recortar el rostro detectado
                                                        cut = frameSave[yi:yf, xi:xf]
                                                        # Nombre de la imagen
                                                        nombre_imagen = f"{RegUser}.png"
                                                        # Ruta donde se guardará la imagen
                                                        ruta_imagen = f"Assets/img/faces/{nombre_imagen}"
                                                        # Guardar la imagen en la carpeta
                                                        cv2.imwrite(ruta_imagen, cut)
                                                        # Llamar a la función para actualizar el campo `foto` en la base de datos
                                                        actualizar_foto_en_bd(RegUser, nombre_imagen)  # Actualizar el campo `foto` en la tabla empleados
                                                        # Step 1
                                                        step = 1
                                                                                                    
                                            else:
                                                conteo = 0

                                        if step == 1:
                                            #Draw
                                            cv2.rectangle(frame, (xi, yi, anc, alt), (0, 255, 0), 2)
                                            #IMG Check Live
                                            alli, anli, c = img_liche.shape
                                            #lo ubicamos en nuestro frame
                                            frame[50:50 + alli, 50:50 + anli] = img_liche
                                #Close
                                close = pantalla2.protocol("WM_DELETE_WINDOW", Close_Window) 
                                draw_elements_on_frame(frame, xi, yi, anc, alt, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8)

        #Convertimos el video: Conv Video
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        #Mostramos el video: Show video
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, Log_Biometric) #Que se ejecute cada 10 milisegundo con la funcion Log_Biometric
    else:
        cap.release()
    
#Creamos nuestra funcion Log
def Log():
    global RegName, RegApellido, RegUser, RegTelefono, RegGenero, RegFechaNacimiento, RegDireccion, RegEmail, RegCargo, InputNameReg, InputApellidoReg, InputUserReg, InputTelefonoReg, InputGeneroReg, InputFechaNacimientoReg, InputDireccionReg, InputEmailReg, InputCargo, cap, lblVideo, pantalla2

    # Extraemos los datos del formulario
    RegName = InputNameReg.get()
    RegApellido = InputApellidoReg.get()
    RegUser = InputUserReg.get()
    RegTelefono = InputTelefonoReg.get()
    RegGenero = InputGeneroReg.get()
    RegFechaNacimiento = InputFechaNacimientoReg.get()
    RegDireccion = InputDireccionReg.get()
    RegEmail = InputEmailReg.get()
    nombreCargo = InputCargo.get()
    RegCargo = InputCargo.cargos.get(nombreCargo)

    # Validamos si el formulario está completo
    if not all([RegName, RegApellido, RegUser, RegTelefono, RegGenero, RegFechaNacimiento, RegDireccion, RegEmail, RegCargo]):
        print("FORMULARIO INCOMPLETO, TODOS LOS CAMPOS SON OBLIGATORIOS")
        messagebox.showwarning("Validación", "Formulario incompleto. Todos los campos son obligatorios.")

    else:
        # Conexión a la base de datos
        conexion = conectar_bd()
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                # Verificamos si el usuario ya está registrado en la base de datos
                consulta = "SELECT COUNT(*) FROM empleados WHERE documento = %s"
                cursor.execute(consulta, (RegUser,))
                resultado = cursor.fetchone()
                if resultado[0] > 0:
                    print("Usuario Registrado Anteriormente en la base de datos")
                else:
                    # Guardamos la información en la base de datos
                    registro_exitoso = registrar_empleado_mysql(RegName, RegApellido, RegUser, RegTelefono, RegGenero, RegFechaNacimiento, RegDireccion, RegEmail, RegCargo)
                    if registro_exitoso:  # Si el registro fue exitoso
                        # Limpiamos los campos del formulario
                        InputNameReg.delete(0, END)
                        InputApellidoReg.delete(0, END)
                        InputUserReg.delete(0, END)
                        InputTelefonoReg.delete(0, END)
                        InputGeneroReg.set("")
                        InputFechaNacimientoReg.delete(0, END)
                        InputDireccionReg.delete(0, END)
                        InputEmailReg.delete(0, END)
                        InputCargo.set("")

                        # Creamos una nueva pantalla para el login biométrico
                        pantalla2 = Toplevel(pantalla)
                        pantalla2.title("LOGIN BIOMETRICO")
                        pantalla2.geometry("1280x720")

                        # Label para el video
                        lblVideo = Label(pantalla2)
                        lblVideo.place(x=0, y=0)

                        # Creamos la captura de video
                        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                        cap.set(3, 1280)
                        cap.set(4, 720)
                        Log_Biometric()
                    else:
                        print("Error al registrar al empleado. Por favor, intente nuevamente.")
            except mysql.connector.Error as err:
                print(f"Error al consultar la base de datos: {err}")
            finally:
                cursor.close()
                conexion.close()
        else:
            print("No se pudo conectar a la base de datos")

#Leer las miamgenes
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

# Tool Drow : Herramienta de dibujo de la malla facial
mpDraw = mp.solutions.drawing_utils
ConfigDraw = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)

#Object Face Mesh
FacemeshObject = mp.solutions.face_mesh
FaceMesh = FacemeshObject.FaceMesh(max_num_faces = 1)

# Object Face Detect -> Detector de Rostros
FaceObject = mp.solutions.face_detection
detector = FaceObject.FaceDetection(min_detection_confidence=0.5, model_selection=1)

#Creamos una lista de informacion: Info List
info = []

#Asignar un margen para la deteccion de rostros

# INTERFAZ -> Ventana principal ----INTERFAZZZZZZZ-----------
# INTERFAZ -> Ventana principal ----
pantalla = Tk()  # Creamos la pantalla
pantalla.title("FACE RECOGNITION SYSTEM")  # Título
pantalla.geometry("1280x720")  # Tamaño de la pantalla

# Fondo
imagenF = PhotoImage(file="C:/xampp/htdocs/python/SetUp/back3.png")
background = Label(pantalla, image=imagenF)
background.place(x=0, y=0, relwidth=1, relheight=1)  # Asegurar que cubra toda la pantalla

#Profile. Fondo para perfil
# imagenbc = PhotoImage(file="C:/xampp/htdocs/Python/asistencia_dream_li_sac/SetUp/Back2.png")
# Fuente personalizada
fuente_personalizada = font.Font(family="Helvetica", size=16)

# Función de validación para permitir solo letras y espacios
def validar_entrada(texto):
    return texto.isalpha() or texto.isspace()

# Registrar la función de validación
validacion = pantalla.register(validar_entrada)

# Función de validación para números
def validar_numeros(char):
    return char.isdigit()

# Registrar la función de validación para números
validacion_numeros = pantalla.register(validar_numeros)

# Limitar el número de caracteres
def limitar_caracteres(entry, limite, event):
    if len(entry.get()) > limite:
        entry.delete(limite, END)

# Primera columna: Datos personales
Label(pantalla, text="Datos Personales", font=("Helvetica", 18, "bold"), bg="#f0f0f0").place(x=100, y=50)

# Nombre
Label(pantalla, text="Nombre:", font=fuente_personalizada).place(x=100, y=100)
InputNameReg = Entry(pantalla, font=fuente_personalizada, bg="white", fg="black", width=25, validate="key", validatecommand=(validacion, "%S"))
InputNameReg.place(x=250, y=100)

# Apellido
Label(pantalla, text="Apellido:", font=fuente_personalizada).place(x=100, y=150)
InputApellidoReg = Entry(pantalla, font=fuente_personalizada, bg="white", fg="black", width=25, validate="key", validatecommand=(validacion, "%S"))
InputApellidoReg.place(x=250, y=150)

# Documento que viene a  ser USUARIO
Label(pantalla, text="Documento:", font=fuente_personalizada).place(x=100, y=200)
InputUserReg = Entry(pantalla, font=fuente_personalizada, bg="white", fg="black", width=25, validate="key", validatecommand=(validacion_numeros, "%S"))
InputUserReg.place(x=250, y=200)
InputUserReg.bind("<KeyRelease>", lambda event: limitar_caracteres(InputUserReg, 8, event))

# Teléfono
Label(pantalla, text="Teléfono:", font=fuente_personalizada).place(x=100, y=250)
InputTelefonoReg = Entry(pantalla, font=fuente_personalizada, bg="white", fg="black", width=25, validate="key", validatecommand=(validacion_numeros, "%S"))
InputTelefonoReg.place(x=250, y=250)
InputTelefonoReg.bind("<KeyRelease>", lambda event: limitar_caracteres(InputTelefonoReg, 9, event))

# Género
Label(pantalla, text="Género:", font=fuente_personalizada).place(x=100, y=300)
InputGeneroReg = ttk.Combobox(pantalla, font=fuente_personalizada, width=23, state="readonly")
InputGeneroReg['values'] = ("Masculino", "Femenino")
InputGeneroReg.place(x=250, y=300)

# Fecha de nacimiento
Label(pantalla, text="Fecha de Nacimiento:", font=fuente_personalizada).place(x=100, y=350)
InputFechaNacimientoReg = Entry(pantalla, font=fuente_personalizada, bg="white", fg="black", width=25)
InputFechaNacimientoReg.place(x=250, y=350)

# Dirección
Label(pantalla, text="Dirección:", font=fuente_personalizada).place(x=100, y=400)
InputDireccionReg = Entry(pantalla, font=fuente_personalizada, bg="white", fg="black", width=25)
InputDireccionReg.place(x=250, y=400)

# Email
Label(pantalla, text="Email:", font=fuente_personalizada).place(x=100, y=450)
InputEmailReg = Entry(pantalla, font=fuente_personalizada, bg="white", fg="black", width=25)
InputEmailReg.place(x=250, y=450)

# Segunda columna: Datos laborales
Label(pantalla, text="Datos Laborales", font=("Helvetica", 18, "bold"), bg="#f0f0f0").place(x=600, y=50)

# Cargo
Label(pantalla, text="Cargo:", font=fuente_personalizada).place(x=600, y=100)
InputCargo = ttk.Combobox(pantalla, font=fuente_personalizada, width=23, state="readonly")
InputCargo.place(x=750, y=100)
configurar_combobox_cargo(InputCargo)

# Botón de registro
imagenBR = PhotoImage(file="C:/xampp/htdocs/python/SetUp/BtLogin.png")
BtReg = Button(pantalla, text="Registro", image=imagenBR, height="40", width="200", command=Log)
BtReg.place(x=750, y=200)

pantalla.mainloop()