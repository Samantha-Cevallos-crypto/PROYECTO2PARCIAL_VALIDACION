from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
import re

from GUI.vtn_principal import Ui_vtn_principal


class PersonaServicio(QMainWindow):
    '''
    Clase que genera la lógica de los objetos persona con validaciones estrictas
    '''

    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)

        # Conexión de botones
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

        # --- VALIDACIONES INTERACTIVAS ---

        # 1. Validación para Nombre y Apellido (Solo letras y espacios en tiempo real)
        regex_letras = QRegularExpression(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
        validador_letras = QRegularExpressionValidator(regex_letras, self)

        self.ui.txt_nombre.setValidator(validador_letras)
        self.ui.txt_apellido.setValidator(validador_letras)

        # Limitar la longitud máxima directamente en la interfaz
        self.ui.txt_nombre.setMaxLength(100)
        self.ui.txt_apellido.setMaxLength(100)

        # 2. Validación para Descripción (Máximo 250 caracteres en tiempo real)
        self.ui.txt_descrip.setMaxLength(250)

        # 3. Validación para Precio (Solo números y un punto decimal en tiempo real)
        regex_precio = QRegularExpression(r'^-?\d*\.?\d*$')
        validador_precio = QRegularExpressionValidator(regex_precio, self)
        self.ui.txt_precio.setValidator(validador_precio)
        # 4.Validacion para email (Formato basico en tiempo real)
        regex_email = QRegularExpression(r"^[a-zA-Z0-9._%+-]*@?[a-zA-Z0-9.-]*\.?[a-zA-Z]{0,}$")
        validador_email = QRegularExpressionValidator(regex_email, self)
        self.ui.txt_email.setValidator(validador_email)
        self.ui.txt_email.setMaxLength(100)

    def guardar(self):
        print("Se hizo clic en el botón de guardar")

        nombre = self.ui.txt_nombre.text().strip()
        apellido = self.ui.txt_apellido.text().strip()
        descripcion = self.ui.txt_descrip.text().strip()
        precio = self.ui.txt_precio.text().strip()
        email = self.ui.txt_email.text().strip()

        print("--- Datos ingresados ---")
        print(
            f"Nombre: {nombre} | Apellido: {apellido} | Descripción: {descripcion} | Precio: {precio} | Email: {email}")

        # 1. Validar que ningún campo esté vacío
        if not nombre or not apellido or not descripcion or not precio or not email:
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los datos.")
            return

        # 2. Validación secundaria de Descripción
        # (Para asegurar que no se hayan pegado caracteres extraños permitiendo letras, números y signos básicos)
        if not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ .,\n-]+$", descripcion):
            QMessageBox.warning(self, "Error de Validación", "La descripción contiene caracteres no permitidos.")
            return

        # 3. Validación secundaria de Precio
        try:
            float(precio)
        except ValueError:
            QMessageBox.warning(self, "Error de Validación", "El precio debe ser un número entero o decimal válido.")
            return
        # 4. Validacion secundaria de Email
        regex_email_completo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(regex_email_completo, email):
            QMessageBox.warning(self, "Error de Validación", "El email ingresado no tiene un formato válido.")
            return


        # --- GUARDAR DATOS ---
        try:
            with open('persona.txt', 'a', encoding='utf-8') as archivo:
                archivo.write(nombre + '\n')
                archivo.write(apellido + '\n')
                archivo.write(descripcion + '\n')
                archivo.write(precio + '\n')
                archivo.write(email + '\n')
                archivo.write('******************\n')
            print("Datos guardados correctamente")

            QMessageBox.information(self, "Éxito", "Los datos se guardaron correctamente.")
            self.limpiar()

        except Exception as e:
            print(f"Error al guardar: {e}")
            QMessageBox.critical(self, "Error", f"Ocurrió un error al guardar el archivo: {e}")

    def limpiar(self):
        print("Se hizo clic en el botón de limpiar")
        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.txt_descrip.setText('')
        self.ui.txt_precio.setText('')
        self.ui.txt_email.setText('')



