import math

n="si"
s="si"
t="si"
m="si"

class Planeta():
    habitantes=[]
    museos=0
    delegacion=[]
    
    def __init__(self,nombre,museos):
        self.nombre=nombre
        self.museos=museos

    def agregarHabitante(self,habitante):
        self.habitantes.append(habitante)
        
    def armarDelegacion(self):
        for i in range(0,len(self.habitantes),1):
            if self.habitantes[i].saberSiEsDestacada()==True:
                self.delegacion.append(self.habitantes[i])
    
    def mostrarDelegacion(self):
        return self.delegacion
    
    def saberSiEsCulto(self):
        inteligencia=True
        for i in range(0,len(self.habitantes),1):
         if self.habitantes[i].calcularInteligencia()==False:
             inteligencia=False
             break   
        if self.museos>=2 and inteligencia==True:
            return True
        
    def saberPotencia(self):
        potencia=0
        for i in range(0,len(self.habitantes),1):
            potencia=self.habitantes[i].calcularPotencia()+potencia
        return potencia
        
        
class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.potencia=20
        self.inteligencia=0
        
    def calcularPotencia(self):
        return int(self.potencia)
    
    def calcularInteligencia(self):
        if self.edad>20 and self.edad<40:
            self.inteligencia=12  
        else:
            self.inteligencia=8
        return self.inteligencia   
                 
    def saberSiEsDestacada(self):
        if self.edad==25 or self.edad==35:
            return True
        else:
            return False           
                            

class Atleta(Persona):

    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        self.peso=4
        self.tecnica=2
        
    def calcularPotencia(self):
        return Persona.calcularPotencia(self)+self.peso*self.tecnica
    
    def saberSiEsDestacada(self):
        return Persona.saberSiEsDestacada(self) or self.tecnica>5
        
    def entrenar(self,dias):
        self.peso +=math.trunc(dias/5)
        
    def aprenderTecnica(self):
        self.tecnica =self.tecnica+1
        print(self.tecnica)
        return self.tecnica

class Docente(Persona):
    def __init__(self,nombre, edad):
        super().__init__(nombre,edad)
        self.cursos=0
    
    def calcularInteligencia(self):
        return super().calcularInteligencia()+2*self.darCursos(self.cursos)
    
    def darCursos(self,cantidadDeCursos):
        self.cursos=cantidadDeCursos
        return self.cursos
        
    def saberSiEsDestacada(self):
        return self.cursos>3
    
nombre=input("Ingrese nombre del planeta")
museos=int(input("Ingrese cantidad de museos"))
triton=Planeta(nombre,museos)


while n=="si":
    nombre=input("Ingrese nombre: ")
    edad=int(input("Ingrese edad: "))
    tipo=input("Ingrese tipo de persona:")
    if tipo=="generica":
        persona=Persona(nombre,edad)
    elif tipo=="atleta":
        persona=Atleta(nombre,edad)
        t=input("Desea entrenar?")
        while t=="si": 
            dias=int(input("Ingrese cantidad de dias: "))
            persona.entrenar(dias)
            t=input("Desea continuar entrenando?")
        m=input("Desea aprender nueva técnica?")
        while m=="si":
            persona.aprenderTecnica()
            m=input("Desea aprender otra nueva técnica?")
    elif tipo=="docente":
        persona=Docente(nombre,edad)
        s=input("Desea cargar cursos?")
        while s=="si":
            cantidad=int(input("Ingrese cantidad: "))
            persona.darCursos(cantidad)
            s=input("Desea seguir cargando cursos?")
    print("Inteligencia: ",persona.calcularInteligencia())
    print("Potencia: ",persona.calcularPotencia())
    print("Es destacada: ",persona.saberSiEsDestacada())
    k=input("Desea agregar al planeta?")
    if k=="si":
        triton.agregarHabitante(persona)
    n=input("Desea cargar otra persona?")
    
    print("Los datos del planeta Tritón son:")
    print("Nombre de los miembros de la delegación son:")
    for i in range(0,len(triton.delegacion),1):
        print("Nombre: ", triton.delegacion(i).nombre)
    
    
    
    