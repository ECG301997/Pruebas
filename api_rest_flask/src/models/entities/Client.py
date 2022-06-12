class Client():
    # id , titulo, descripcion, prioridad, estado, creado, usuario, fecha_creacion, fecha_actualizacion
    def __init__(self,id,titulo=None,descripcion=None,prioridad=None, estado=None,
                 creado=None,usuario=None,fecha_creacion=None,fecha_actualizacion=None)-> None:
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.creado = creado
        self.usuario = usuario
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
    
    def to_JSON(self):
        return {
            'id' : self.id,
            'titulo' : self.titulo,
            'descripcion' : self.descripcion,
            'prioridad' : self.prioridad,
            'estado' : self.estado,
            'creado' : self.creado,
            'usuario' : self.usuario,
            'fecha_creacion' : self.fecha_creacion,
            'fecha_actualizacion' : self.fecha_actualizacion
        }