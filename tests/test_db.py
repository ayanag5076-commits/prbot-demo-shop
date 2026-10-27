def test_seed_loads_users_and_orders(conn):
    assert conn.execute("SELECT COUNT(*) FROM users").fetchone() == (3,)
    assert conn.execute("SELECT COUNT(*) FROM orders").fetchone() == (3,)
