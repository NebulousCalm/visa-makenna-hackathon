from flask import Flask, render_template

from utils import get_site_impact

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/website-impact')
def get_website_impact():
    impact = get_site_impact('https://www.google.com')  # REPLACE THIS WITH PRODUCTION URL
    return render_template('website-impact.html', impact=impact)


@app.route('/temp/demo')
def temp_demo():
    return render_template('demo.temp.html')


@app.route('/demo/product-page')
def demo_product_page():
    return render_template('product-page-demo.html')


if __name__ == "__main__":
    app.run(debug=True)
