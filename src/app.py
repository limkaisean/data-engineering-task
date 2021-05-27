# app.py
# provides the Flask application

from flask import Flask, Response
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app = Flask(__name__)  # create a Flask app

db_engine = create_engine("sqlite:///data/musical_instrument_reviews.sqlite")


#uncomment the part below to connect to a postgresql db
'''
POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}


db = 'postgres+psycopg2://%s:%s@%s:%s/%s'%(POSTGRES['user'], POSTGRES['pw'], POSTGRES['host'], POSTGRES['port'], POSTGRES['db'])

db_engine = create_engine(db)

'''

@app.route("/", methods=["GET"])
def root() -> Response:
    """
    root - returns 200 OK

    """
    return Response("It's alive!", status=200)


@app.route("/product/<product_id>")
def average_product_review(product_id: str) -> Response:
    """
    average_product_review

    Retrieve aggregated review information for a product with a specific product_id (eg. '0739079891'). 
    Obtain relevant review information for the product by returning the productID, average rating and number of ratings.

    TO-DO: ADD DOCUMENTATION
    
    """
    sql = text(
        "SELECT productID, AVG(overall), COUNT(*) FROM reviews WHERE productID = :product_id;"
    )
    result = db_engine.execute(sql, product_id=product_id).fetchall()

    response = {
        'productID': result[0][0],
        'avgRating': result[0][1],
        'noOfRatings': result[0][2]
    }

    return Response(str(response), 200)

@app.route("/reviewer/<reviewer_id>")
def average_reviewer_review(reviewer_id: str) -> Response:
    """
    average_reviewer_review

    Retrieve aggregated review information from a reviewer with a specific reviewer_id (eg. 'A3FO5AKVTFRCRJ'). 
    Obtain relevant review information from the product by returning the reviewerID, reviewerName, average rating and number of ratings.

    """
    sql = text(
        "SELECT reviewerID, reviewerName, AVG(overall), COUNT(*) FROM reviews WHERE reviewerID = :reviewer_id;"
    )
    result = db_engine.execute(sql, reviewer_id=reviewer_id).fetchall()

    response = {
        'reviewerID': result[0][0],
        'reviewerName': result[0][1],
        'avgRating': result[0][2],
        'noOfRatings': result[0][3]
    }

    return Response(str(response), 200)


if __name__ == '__main__':
    app.run()