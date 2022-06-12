from database.db import get_connection
from .entities.Client import Client

class ClientModel:
    @classmethod
    def get_client(self):
        try:
            connection = get_connection()
            clients = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id , titulo, descripcion, prioridad, estado, creado, usuario, fecha_creacion, fecha_actualizacion FROM data ORDER BY update_at DESC")
                resultset = cursor.fetchall()
                
                for row in resultset:
                    client=Client(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    clients.append(client.to_JSON())
                    
            connection.close()
            return clients  
        except Exception as ex:
            raise Exception(ex)