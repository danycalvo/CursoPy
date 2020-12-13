import clases
pp = clases.Persona()
pp.setNombre("pepae")
name = pp.getNombre()
print(name)

inf = clases.Informatico()
inf.setNombre("dc")
inf.setEdad(61)
inf.apender("peras")

print(inf.getNombre())
print(inf.getEdad())
print(inf.getLenguages())
print(inf.programar())
print(inf.caminar())

tec = clases.Tenico()
tec.setNombre("was")
print("tecnico")
print(tec.getNombre())
print(tec.getLenguages())
print(tec.queHace())
