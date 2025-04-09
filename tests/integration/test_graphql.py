# tests/integration/test_graphql.py
def test_graphql_users_query(client, db):
    # Add test data to db
    db.add(User(email="test@example.com"))
    db.commit()
    
    # GraphQL query
    query = """
        query {
            users {
                id
                email
            }
        }
    """
    
    response = client.post("/graphql", json={"query": query})
    
    assert response.status_code == 200
    assert len(response.json()["data"]["users"]) == 1
    assert response.json()["data"]["users"][0]["email"] == "test@example.com"