import postgresql.driver as pg_driver

CREDENTIALS = {
    'database': os.getenv('POSTGRES_DB', 'test'),
    'user': os.getenv('POSTGRES_USER', 'testuser'),
    'password': os.getenv('POSTGRES_PASSWORD', 'testpassword'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': '5432'
}

conn = pg_driver.connect(**CREDENTIALS)

conn.execute(
"""
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS addresses (
    id SERIAL PRIMARY KEY,
    book INTEGER REFERENCES books(id),
    first_name VARCHAR(256),
    last_name VARCHAR(256),
    address VARCHAR(256),
    city VARCHAR(256),
    country VARCHAR(256),
    zip VARCHAR(10),
    phone VARCHAR(25),
    email VARCHAR(50),
    web VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS test (
    id SERIAL PRIMARY KEY,
    test VARCHAR(256)
);
"""
)