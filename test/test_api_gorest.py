import requests
import pytest
import logging
from faker import Faker
import pathlib
from test.conftest import logger
import time

# se utiliza la URL pública de GoRest para los usuarios
BASE_URL = "https://gorest.co.in/public/v2" 
ACCESS_TOKEN = "900a9edd9ab30e8d7c7d4a2fa40deb4a8ba0b3535ed5671262f803188aedf242"

GOREST_HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
fake = Faker()

class TestGoRest:
    print ("- Tests for GoRest API - ")
    
    # TEST 1: GET - Obtener lista de usuarios (Éxito)
    def test_get_users_success(self):
        """Obtener lista de usuarios exitosamente"""
        logger.info("\n=== Test 1: GET Users ===")
        print("\n=== Test 1: GET Users ===")
        # URL específica para la lista de usuarios
        endpoint = f"{BASE_URL}/users" 
        
        # Hacer petición GET
        response = requests.get(endpoint)
        
        # Validar código de estado
        assert response.status_code == 200, f"Esperado 200, Obtenido {response.status_code}"
        print("✅ State code 200 - OK")
        logger.info("✅ State code 200 - OK")
        
        # Convertir a JSON
        data = response.json()
        
        # Validar estructura del JSON
        assert isinstance(data, list), "La respuesta debería ser una lista de usuarios"
        assert len(data) > 0, "La lista de usuarios no debería estar vacía"
        print("✅ Correct JSON structure (List)")
        logger.info("✅ Correct JSON structure (List)")
        # Validar estructura del primer usuario
        first_user = data[0]
        required_fields = ["id", "name", "email", "gender", "status"] 
        for field in required_fields:
            assert field in first_user, f"Campo '{field}' no encontrado en el usuario"
        print("✅ Correct user structure")
        logger.info("✅ Correct user structure")
        # Validar tipos de datos
        assert isinstance(first_user["id"], int)
        assert isinstance(first_user["name"], str)
        assert isinstance(first_user["email"], str)
        assert isinstance(first_user["gender"], str) 
        assert isinstance(first_user["status"], str) 
        print("✅ Correct data types")
        logger.info("✅ Correct data types")
        print("🎉 GoRest GET Users test successfully completed!")
        logger.info("🎉 GoRest GET Users test successfully completed!")

    # TEST 2: POST - Crear un nuevo usuario (Éxito)
    def test_create_post_sucess(self):
        """POST/users - Crear un nuevo usuario exitosamente""" 
        logger.info("\n=== Test 2: Post Create User ===")
        print("\n=== Test 2: Post Create User ===")

        # 1. Datos para crear el usuario (usando Faker para datos únicos)
        post_data = {
            "name": fake.name(),
            "gender": fake.random_element(elements=('male', 'female')),
            # Usar un email con timestamp para garantizar que sea único y evitar 422 Duplicado
            "email": f"test_user_{time.time()}@gorest.com",
            "status": "active"
        }

        # URL específica para la creación
        endpoint = f"{BASE_URL}/users"

        # 2. Hacer petición POST
        response = requests.post(endpoint, json=post_data,headers=GOREST_HEADERS)
    
        # 3. Validar código de estado
        # La creación exitosa debe devolver 201 Created
        assert response.status_code == 201, (
            f"Fallo al crear usuario. Esperado 201, Obtenido {response.status_code}. "
            f"Respuesta: {response.text}"
        )
        print("✅ State code 201 - Created")
        logger.info("✅ State code 201 - Created")

        # 4. Convertir a JSON
        data = response.json()
        
        # 5. Validar estructura de respuesta
        expected_fields = ["id", "name", "email", "gender", "status"]
        for field in expected_fields:
            assert field in data, f"Campo '{field}' no encontrado en respuesta"
        print("✅ Correct answer structure")
        logger.info("✅ Correct answer structure")

        # 6. Validar que los datos se guardaron correctamente
        assert data["name"] == post_data["name"]
        assert data["email"] == post_data["email"]
        assert data["gender"] == post_data["gender"]
        assert data["status"] == post_data["status"]
        print("✅ Data saved successfully")
        logger.info("✅ Data saved successfully")
        
        # 7. Validar el ID generado
        # El ID generado debe ser un entero y no nulo.
        assert isinstance(data["id"], int)
        assert data["id"] is not None
        print(f"✅ ID assigned correctly: {data['id']}")
        logger.info("✅ ID assigned correctly: {data['id']}")
        print("🎉 CREATE User test completed successfully!")
        logger.info("🎉 CREATE User test completed successfully!")

    # TEST 3: DELETE - Eliminar un usuario (Éxito)
    def test_delete_user_success(self):
        """DELETE /users/{id} - Crea un usuario y luego lo elimina exitosamente."""
        logger.info("\n=== Test 3: DELETE User ===")
        print("\n=== Test 3: DELETE User ===")
        
        # --- PASO 1: CREAR EL RECURSO A ELIMINAR (SETUP) ---
        print("🔧 STEP 1: Creating a temporary user for DELETE...")
        
        # Datos para crear el post
        post_data = {
            "name": fake.name(),
            "gender": fake.random_element(elements=('male', 'female')),
            "email": f"user_delete_{time.time()}@correo.com",
            "status": "inactive"
        }
        
        # Ejecutar POST
        creation_response = requests.post( f"{BASE_URL}/users", json=post_data, headers=GOREST_HEADERS)
        
        # Validar la creación inicial
        assert creation_response.status_code == 201, "Falló el Setup: No se pudo crear el usuario."
        created_user_id = creation_response.json()["id"]
        
        print(f"✅ User created with ID: {created_user_id}")
        logger.info(f"User {created_user_id} created for DELETE.")
        
        # --- PASO 2: EJECUTAR DELETE ---
        
        # ID del usuario a eliminar
        user_id_to_delete = created_user_id
        
        # Hacer petición DELETE con el ID y los headers de autorización
        delete_endpoint = f"{BASE_URL}/users/{user_id_to_delete}"
        response = requests.delete(delete_endpoint, headers=GOREST_HEADERS)
        
        # --- PASO 3: VALIDACIONES DE DELETE ---
        
        # 3.1 Validar código de estado
        # GoRest, a diferencia de JSONPlaceholder, devuelve 204 No Content para DELETE exitoso.
        assert response.status_code == 204, (
            f"Esperado 204 No Content, obtenido {response.status_code}. Respuesta: {response.text}"
        )
        print("✅ State code 204 - No Content")
        logger.info("✅ State code 204 - No Content")
        
        # 3.2 Validar cuerpo de la respuesta
        # Para 204, el cuerpo debe estar vacío (no hay contenido para analizar en JSON)
        assert response.text == "", f"Esperado cuerpo vacío, obtenido: {response.text}"
        print("✅ Correct answer: DELETE (Empty body)")
        
        # --- PASO 4: VERIFICAR ELIMINACIÓN (TEARDOWN / OPCIONAL) ---
        
        # Intentar obtener el recurso eliminado para asegurar que devuelve 404
        verification_response = requests.get(delete_endpoint)
        
        # Validar código de estado 404 Not Found
        assert verification_response.status_code == 404, (
            f"Fallo en verificación: Se esperaba 404, obtenido {verification_response.status_code}"
        )
        print("✅ Verification 404 successful (User does not exist)")
        logger.info("✅ Verification 404 successful (User does not exist)")
        print(f"🎉 Test DELETE User ID {created_user_id} successfully completed!")
        logger.info("🎉 Test DELETE User ID {created_user_id} successfully completed!")