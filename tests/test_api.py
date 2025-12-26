def test_create_user_success(client):
    response = client.post("/api/users/", json={
        "username": "TestUser1", 
        "email": "test1@example.com", 
        "password": "strongpassword123"
    })
    assert response.status_code == 201
    assert "id" in response.json()

def test_read_users(client):

    client.post("/api/users/", json={"username": "U2", "email": "read@test.com", "password": "123"})
    response = client.get("/api/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_category(client):
    response = client.post("/api/categories/", json={"name": "Elektronik"})
    assert response.status_code == 201
    assert response.json()["name"] == "Elektronik"

def test_read_categories(client):
    response = client.get("/api/categories/")
    assert response.status_code == 200

def test_create_product_success(client):

    cat = client.post("/api/categories/", json={"name": "Bilgisayar"}).json()
    
    response = client.post("/api/products/", json={
        "name": "Laptop", 
        "description": "Oyun Bilgisayarı", 
        "price": 25000.0, 
        "stock": 10, 
        "category_id": cat["id"]
    })
    assert response.status_code == 201
    assert response.json()["stock"] == 10

def test_create_order_success(client):
   
    u = client.post("/api/users/", json={"username": "Buyer", "email": "buyer@test.com", "password": "123"}).json()
    c = client.post("/api/categories/", json={"name": "OrderCat"}).json()
    p = client.post("/api/products/", json={"name": "Satilik", "price": 100, "stock": 50, "category_id": c["id"]}).json()
    

    order_data = {
        "user_id": u["id"],
        "items": [
            { "product_id": p["id"], "quantity": 2 }
        ]
    }
    response = client.post("/api/orders/", json=order_data)
    assert response.status_code == 201
    


def test_delete_user(client):

    create_res = client.post("/api/users/", json={"username": "Silinecek", "email": "del@test.com", "password": "123"})
    user_id = create_res.json()["id"]
    
    # 2. Sil
    del_res = client.delete(f"/api/users/{user_id}")
    assert del_res.status_code == 204
    

    list_res = client.get("/api/users/")
    users = list_res.json()
    assert not any(u["id"] == user_id for u in users)

def test_create_category_duplicate(client):
    client.post("/api/categories/", json={"name": "DuplicateCat"})
    res = client.post("/api/categories/", json={"name": "DuplicateCat"})
  
    assert res.status_code != 201 

def test_create_review_success(client):
   
    cat = client.post("/api/categories/", json={"name": "ReviewCat"}).json()
    prod = client.post("/api/products/", json={"name": "ReviewProd", "price": 10, "category_id": cat["id"]}).json()
    
  
    res = client.post("/api/reviews/", json={
        "content": "Harika ürün",
        "rating": 5,
        "product_id": prod["id"]
    })
    assert res.status_code == 201
    assert res.json()["rating"] == 5

def test_read_reviews(client):
    response = client.get("/api/reviews/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_review_invalid_product(client):
    res = client.post("/api/reviews/", json={
        "content": "Kotu", "rating": 1, "product_id": 99999
    })
    assert res.status_code == 404

def test_create_product_invalid_category(client):
    res = client.post("/api/products/", json={
        "name": "Hayali", "price": 10, "category_id": 99999
    })
    assert res.status_code == 404

def test_create_user_missing_field(client):
   
    res = client.post("/api/users/", json={"username": "EksikUser", "email": "eksik@test.com"})
    assert res.status_code == 422  

def test_get_nonexistent_endpoint(client):
    res = client.get("/api/olmayan-bir-sayfa")
    assert res.status_code == 404