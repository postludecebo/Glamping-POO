# 🏕️ Sistema de Gestión de Glamping

### 📌 Descripción
Este proyecto es un **Sistema de Gestión de Glamping** desarrollado en **Python**, aplicando principios de **Programación Orientada a Objetos (POO)**. Permite la gestión de alojamientos, huéspedes, reservas y servicios adicionales.  

---

## ✨ **Características Principales**
✅ Registro y gestión de alojamientos (cabañas, domos, tiendas de lujo).  
✅ Manejo de información de huéspedes y empleados.  
✅ Creación y control de reservas con cálculo de precios según temporada.  
✅ Oferta de servicios adicionales como spa, tours y comidas.  
✅ Generación de reportes de ingresos mensuales.  

---

## 🏗️ **Estructura del Código**
El sistema está compuesto por las siguientes clases:

- **`Person`**: Superclase que define atributos básicos como nombre, teléfono y email.  
- **`Guest`**: Hereda de `Person`, agregando fecha de nacimiento y país de origen.  
- **`Employee`**: Hereda de `Person`, incluyendo cargo, salario y fecha de ingreso.  
- **`Hosting`**: Gestiona alojamientos, disponibilidad y cálculo de precios por temporada.  
- **`AdditionalService`**: Representa servicios adicionales disponibles en el glamping.  
- **`Reservation`**: Maneja reservas, cálculo de precios y estados como "confirmada" o "cancelada".  
- **`Glamping`**: Clase principal que gestiona huéspedes, alojamientos, empleados y reservas.  

📌 **El código implementa encapsulación, herencia y polimorfismo** para optimizar la estructura del sistema.  

---

## 🚀 **Instalación y Uso**
Para ejecutar el sistema en tu máquina:

1️⃣ **Clonar el repositorio**:  
   ```sh
   git clone https://github.com/postludecebo/Glamping-POO.git

2️⃣ Navegar al directorio del proyecto:
   cd Sistema-Glamping

3️⃣ Ejecutar el script principal:
   glampingversionfinal.py

🎯 Ejemplo de Uso
Aquí hay un ejemplo de cómo utilizar el sistema:
glamping = Glamping("EcoGlamp", "Montañas Verdes")
guest = Guest("Sergio", "3001234567", "sergio@email.com", "12345678", "1998-05-21", "Colombia", ["Vegetariano"])
glamping.registerGuests(guest)
print(guest.show_info())

Autores:
Sergio Esteban León Valencia - Github: https://github.com/postludecebo
Hanna Isabela Cardona Echavarria - Github: https://github.com/hannacardona
Laura Manuela Muñoz Hernandez - Github: https://github.com/lauramanuelamunoz
Santiago Molina Muñoz - Github: https://github.com/SantiagoMM7
