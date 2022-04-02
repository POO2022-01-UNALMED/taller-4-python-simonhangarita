from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo perdeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
          if self._asignaturas is None:
            self._asignaturas=[]
            self._asignaturas.append(Asignatura(x))
          else:
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            lista=[]
            lista.append(alumno)
            self.listadoAlumnos = lista
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    def __str__(self):
      cadena= "Grupo de estudiantes: "+ self._grupo
      return cadena