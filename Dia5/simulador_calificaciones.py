from faker import Faker
from faker.providers import person

fake = Faker ()
fake.add_provider(person)

for alumno in range (1,51):
    nombre = fake.first_name()
    apellido = fake.last_name()
    correo = fake.email()
    query = f"insert into alumnos (nombre,apellido,correo) values ('{nombre}','{apellido}','{correo}');"
    print(query)

for alumnos_cursos in range (75):
    curso = fake.random_int(1,4)
    alumno = fake.random_int(1,51)
    query = f"insert into alumnos_cursos (alumno_id,curso_id) values ('{alumno}','{curso}');"
    print(query)
