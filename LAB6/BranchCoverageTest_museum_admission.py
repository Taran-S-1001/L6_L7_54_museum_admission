import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


# ---- ticket_price: every decision both ways ----

def test_unknown_category_raises():
    with pytest.raises(ValueError):
        ticket_price("vip", 30, "tuesday", False)

def test_negative_age_raises():
    with pytest.raises(ValueError):
        ticket_price("adult", -1, "tuesday", False)

def test_child_under_five_free():
    assert ticket_price("child", 3, "tuesday", False) == 0

def test_child_exactly_five_not_free():
    assert ticket_price("child", 5, "tuesday", False) == 100

def test_adult_weekday_no_tour():
    assert ticket_price("adult", 30, "tuesday", False) == 300

def test_adult_monday_half_price():
    assert ticket_price("adult", 30, "monday", False) == 150

def test_adult_saturday_surcharge():
    assert ticket_price("adult", 30, "saturday", False) == 350

def test_adult_sunday_surcharge():
    assert ticket_price("adult", 30, "sunday", False) == 350

def test_student_guided_tour_student_rate():
    assert ticket_price("student", 20, "tuesday", True) == 200

def test_adult_guided_tour_standard_rate():
    assert ticket_price("adult", 30, "tuesday", True) == 400

def test_student_monday_guided():
    assert ticket_price("student", 20, "monday", True) == 125

# ---- group_discount: every decision both ways ----

def test_invalid_group_size_raises():
    with pytest.raises(ValueError):
        group_discount(0, False)

def test_school_group_at_threshold():
    assert group_discount(20, True) == 40

def test_school_group_below_threshold():
    assert group_discount(19, True) == 25

def test_non_school_large_group():
    assert group_discount(15, False) == 20

def test_non_school_medium_group():
    assert group_discount(8, False) == 10

def test_non_school_small_group():
    assert group_discount(7, False) == 0

# ---- gallery_entry: every decision both ways ----

def test_gallery_full_wait():
    assert gallery_entry(100, 100, False) == "wait"

def test_gallery_near_capacity_no_slot_queue():
    assert gallery_entry(95, 100, False) == "queue"

def test_gallery_near_capacity_with_slot_enter():
    assert gallery_entry(95, 100, True) == "enter"

def test_gallery_below_threshold_enter():
    assert gallery_entry(10, 100, False) == "enter"
