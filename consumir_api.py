import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
respuesta = requests.get(url)


if respuesta.status_code == 200:
    data = respuesta.json()
    print(data)
    # Obtener la cantidad de empleados
    cantidad_empleados = len(data['data'])
    print(f'Cantidad de empleados: {cantidad_empleados}')

    # Calcular el promedio de salario de los empleados
    salarios = [empleado['employee_salary'] for empleado in data['data']]
    promedio_salario = sum(salarios) / cantidad_empleados
    print(f'Promedio de salario: {promedio_salario}')

    # Calcular el promedio de edad de los empleados
    edades = [empleado['employee_age'] for empleado in data['data']]
    promedio_edad = sum(edades) / cantidad_empleados
    print(f'Promedio de edad: {promedio_edad}')

    # Calcular salario mínimo y máximo
    salario_minimo = min(salarios)
    salario_maximo = max(salarios)
    print(f'Salario mínimo: {salario_minimo}')
    print(f'Salario máximo: {salario_maximo}')

    # Encontrar la edad menor y mayor
    edad_menor = min(edades)
    edad_mayor = max(edades)
    print(f'Edad menor: {edad_menor}')
    print(f'Edad mayor: {edad_mayor}')

else:
    print(f'Error al obtener los datos. Código de estado: {respuesta.status_code}')
