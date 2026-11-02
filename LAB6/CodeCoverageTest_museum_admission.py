import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


# ---- ticket_price ----

def test_unknown_category_raises():
    with pytest.raises(ValueError):
        ticket_price("vip", 30, "tuesday", False)

def test_negative_age_raises():
    with pytest.raises(ValueError):
        ticket_price("adult", -1, "tuesday", False)

def test_child_under_five_free():
    assert ticket_price("child", 3, "tuesday", False) == 0

def test_adult_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300

def test_adult_monday_half_price():
    assert ticket_price("adult", 30, "monday", False) == 150

def test_adult_weekend_surcharge():
    assert ticket_price("adult", 30, "saturday", False) == 350

def test_student_guided_tour():
    assert ticket_price("student", 20, "tuesday", True) == 200

def test_adult_guided_tour():
    assert ticket_price("adult", 30, "tuesday", True) == 400

# ---- group_discount ----

def test_invalid_group_size_raises():
    with pytest.raises(ValueError):
        group_discount(0, False)

def test_school_large_group():
    assert group_discount(25, True) == 40

def test_school_small_group():
    assert group_discount(10, True) == 25

def test_large_group():
    assert group_discount(15, False) == 20

def test_medium_group():
    assert group_discount(8, False) == 10

def test_small_group():
    assert group_discount(4, False) == 0

# ---- gallery_entry ----

def test_gallery_full_wait():
    assert gallery_entry(100, 100, True) == "wait"

def test_gallery_near_capacity_queue():
    assert gallery_entry(95, 100, False) == "queue"

def test_gallery_enter():
    assert gallery_entry(10, 100, False) == "enter"
