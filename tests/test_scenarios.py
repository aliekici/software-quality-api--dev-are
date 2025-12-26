def test_scenario_full_shopping_flow(client):
    
    user_res = client.post("/api/users/", json={"username": "E2EUser", "email": "e2e@test.com", "password": "123"})
    assert user_res.status_code == 201
    user_id = user_res.json()["id"]

    
    cat_res = client.post("/api/categories/", json={"name": "E2E Kategori"})
    assert cat_res.status_code == 201
    cat_id = cat_res.json()["id"]

    prod_res = client.post("/api/products/", json={
        "name": "Laptop", "description": "Gaming", "price": 25000, "stock": 5, "category_id": cat_id
    })
    assert prod_res.status_code == 201
    prod_id = prod_res.json()["id"]

    order_res = client.post("/api/orders/", json={
        "user_id": user_id,
        "items": [
            { "product_id": prod_id, "quantity": 1 }
        ]
    })
    assert order_res.status_code == 201

def test_scenario_inventory_management(client):
  
    cat = client.post("/api/categories/", json={"name": "StokTest"}).json()
    user = client.post("/api/users/", json={"username": "Stokcu", "email": "stokcu@test.com", "password": "123"}).json()
   
    prod = client.post("/api/products/", json={
        "name": "Stok Urun", "description": "x", "price": 10, "stock": 10, "category_id": cat["id"]
    }).json()

    client.post("/api/orders/", json={
        "user_id": user["id"],
        "items": [{ "product_id": prod["id"], "quantity": 3 }]
    })
    
def test_scenario_review_flow(client):
    
    
    cat = client.post("/api/categories/", json={"name": "YorumTest"}).json()
    prod = client.post("/api/products/", json={"name": "Yorumluk Urun", "price": 50, "category_id": cat["id"]}).json()
    

    client.post("/api/reviews/", json={"content": "Super", "rating": 5, "product_id": prod["id"]})
    
   
    reviews = client.get("/api/reviews/").json()
    assert any(r["content"] == "Super" for r in reviews)

def test_scenario_user_lifecycle(client):

    u = client.post("/api/users/", json={"username": "LifeUser", "email": "life@test.com", "password": "123"}).json()
    uid = u["id"]

    up_res = client.put(f"/api/users/{uid}", json={"username": "LifeUserUpdated", "email": "life@test.com", "password": "123"})
    assert up_res.status_code == 200
    assert up_res.json()["username"] == "LifeUserUpdated"
    

    del_res = client.delete(f"/api/users/{uid}")
    assert del_res.status_code == 204

def test_scenario_category_product_relation(client):

    c1 = client.post("/api/categories/", json={"name": "Cat A"}).json()
    c2 = client.post("/api/categories/", json={"name": "Cat B"}).json()
    
    p1 = client.post("/api/products/", json={"name": "Prod A", "price": 10, "category_id": c1["id"]}).json()
    p2 = client.post("/api/products/", json={"name": "Prod B", "price": 20, "category_id": c2["id"]}).json()
    
    all_prods = client.get("/api/products/").json()
    
    prod_a = next(p for p in all_prods if p["id"] == p1["id"])
    prod_b = next(p for p in all_prods if p["id"] == p2["id"])
    
    assert prod_a["category_id"] == c1["id"]
    assert prod_b["category_id"] == c2["id"]