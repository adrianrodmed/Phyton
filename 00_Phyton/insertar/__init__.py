import MySQLdb

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'tienda' 
comando = "INSERT INTO `clientes` (`IdCliente`, `Nombre`, `Ciudad`, `Telefono`, `Mail`) VALUES (NULL, 'Santiago', 'Gerona', '123456789', 'santiago@gmail.com')"
#def run_query(query=''): 
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
cursor = conn.cursor()         # Crear un cursor 
cursor.execute(comando)          # Ejecutar una consulta 

#if query.upper().startswith('SELECT'): 
#data = cursor.fetchall()   # Traer los resultados de un select 
#else: 
conn.commit()              # Hacer efectiva la escritura de datos 
#data = None 
 
cursor.close()                 # Cerrar el cursor 
conn.close()                   # Cerrar la conexion 

#print(data)
print('Registro guardado')