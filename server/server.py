from flask import Flask, render_template
import sqlite3
from utils import get_site_impact

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/website-impact')
def get_website_impact():
    impact = get_site_impact('https://www.google.com')  # REPLACE THIS WITH PRODUCTION URL
    return render_template('website-impact.html', impact=impact)


@app.route('/demo/product-page/:product')
def demo_product_page(product):
    product = product.lower()  # dynamic product render?
    con = sqlite3.connect("VISA.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM products WHERE prodid='BAN101'")  # maybe product var go here?? - Zach

    rows = cur.fetchall()
    con.close()
    return render_template(
        'product-page-demo.html',
        rows=rows
    )


if __name__ == "__main__":
    app.run(debug=True)
