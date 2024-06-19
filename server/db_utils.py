import sqlite3


def create_sql_db(DATABASE='VISA.db'):
    try:
        with sqlite3.connect(DATABASE) as conn:
            print("Connected to database successfully")

            # Create table if not exists
            conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    prodid TEXT,     
                    name TEXT,
                    desc TEXT,
                    rating INT,
                    price TEXT,
                    quantity TEXT
                )
            ''')
            print("Created table successfully!")

            # Insert a record using parameters
            product_data = ('BAN101', 'Fresh Banana',
                            'Fresh and delicious, our bananas are the perfect snack or addition to your favorite recipes. These naturally sweet and nutritious fruits are rich in potassium, vitamins, and fiber, providing a quick energy boost anytime.',
                            4, '0.70', 'EACH')
            conn.execute('INSERT INTO products (prodid ,name, desc, rating, price, quantity) VALUES (?, ?, ?, ?, ?, ?)',
                         product_data)
            print("Inserted a record into products table successfully!")

    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")

    return None


if __name__ == '__main__':
    create_sql_db()
