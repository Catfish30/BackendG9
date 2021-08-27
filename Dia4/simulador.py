from faker import Faker
from faker.providers import person, misc

fake = Faker()
fake.add_provider(person)
fake.add_provider(misc)


print(fake.name())
print(fake.first_name_male())
print(fake.first_name_female())
print(fake.random_int(min=1,max=5))
print(fake.uuid4())

personal = []

# Factories

for id in range(1,150):

    nombre = fake.first_name()
    apellido = fake.last_name()
    departamento = fake.random_int(min=1,max=4)
    identificador = fake.uuid4()

    if id ==1:
        supervisor = 'null'
    else:
        supervisor_id = fake.random_int(min=-10,max=id-1)
        supervisor =  "null" if supervisor_id <= 0 else supervisor_id

    texto = f"""insert into personal (IDENTIFICADOR,NOMBRE,APELLIDO,DEPARTAMENTO_ID,SUPERVISOR_ID) VALUES
                                        ('{identificador}','{nombre}','{apellido}',{departamento},{supervisor});"""

    print(texto)