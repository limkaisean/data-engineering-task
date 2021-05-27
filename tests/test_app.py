# tests/test_app.py
# tests for src/app.py

import pytest
from src.app import root
from src.app import average_product_review
from src.app import average_reviewer_review
from sqlalchemy import create_engine

db_engine = create_engine("sqlite:///data/musical_instrument_reviews.sqlite")

def test_root():
    rsp = root()
    assert rsp.data.decode("utf8") == "It's alive!", "Unexpected response message"
    assert rsp.status_code == 200, "Status code was not 200"

def test_average_product_review():
    '''
    test_average_product_review

    assert that the output of average_product_review is the same as expected

    '''
    rsp = average_product_review('0739079891')
    assert rsp.data.decode("utf8") == "{'productID': '0739079891', 'avgRating': 3.8484848484848486, 'noOfRatings': 33}", "Unexpected response message"
    assert rsp.status_code == 200, "Status code was not 200"

def test_average_reviewer_review():
    '''
    test_average_reviewer_review

    assert that the output of average_reviewer_review is the same as expected

    '''
    rsp = average_reviewer_review('A3FO5AKVTFRCRJ')
    assert rsp.data.decode("utf8") == "{'reviewerID': 'A3FO5AKVTFRCRJ', 'reviewerName': 'francisco', 'avgRating': 5.0, 'noOfRatings': 8}", "Unexpected response message"
    assert rsp.status_code == 200, "Status code was not 200"
