import nose
import arrow
import acp_times
from nose.tools import assert_equal

start_time = arrow.get("2023-11-01T00:00:00+00:00")

def test_60_km_control():
    control = 60
    brevet_dist = 200    
    open_expected =  "2023-11-01T01:46:00+00:00"
    close_expected = "2023-11-01T04:00:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)
    
def test_120_km_control():
    control = 120
    brevet_dist = 200    
    open_expected = "2023-11-01T03:32:00+00:00"
    close_expected = "2023-11-01T08:00:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

@nose.tools.istest
def test_150_km_control():
    control = 150
    brevet_dist = 200
    start_time = arrow.get("2023-11-01T00:00:00+00:00")
    
    open_expected = "2023-11-01T04:25:00+00:00"
    close_expected = "2023-11-01T10:00:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

def test_200_km_control():
    control = 200
    brevet_dist = 200    
    open_expected =  "2023-11-01T05:53:00+00:00"
    close_expected =    "2023-11-01T13:30:00+00:00"
    
    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

def test_205_km_control():
    control = 205
    brevet_dist = 200    
    open_expected =  "2023-11-01T05:53:00+00:00"
    close_expected =    "2023-11-01T13:30:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)
    
@nose.tools.istest
def test_311_km_control():
    control = 311
    brevet_dist = 400

    open_expected = "2023-11-01T09:21:00+00:00"
    close_expected = "2023-11-01T20:44:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

@nose.tools.istest
def test_550_km_control():
    control = 550
    brevet_dist = 600

    open_expected = "2023-11-01T17:08:00+00:00"
    close_expected = "2023-11-02T12:40:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

@nose.tools.istest
def test_600_km_control():
    control = 600
    brevet_dist = 600

    open_expected = "2023-11-01T18:48:00+00:00"
    close_expected = "2023-11-02T16:00:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

@nose.tools.istest
def test_700_km_control():
    control = 700
    brevet_dist = 1000

    open_expected = "2023-11-01T22:22:00+00:00"
    close_expected = "2023-11-03T00:45:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

def test_890_km_control():
    control = 890
    brevet_dist = 1000

    open_expected = "2023-11-02T05:09:00+00:00"
    close_expected = "2023-11-03T17:23:00+00:00"

    open_actual = acp_times.open_time(control, brevet_dist, start_time)
    close_actual = acp_times.close_time(control, brevet_dist, start_time)

    assert_equal(open_actual, open_expected)
    assert_equal(close_actual, close_expected)

if __name__ == '__main__':
    nose.run()

##those counted as 2 test cases 
# @nose.tools.istest
# def test_open_times():
#     test_cases = [
#         (150, 200, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-01T04:25:00+00:00"),
#         (700, 1000, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-01T22:22:00+00:00"),
#         (600, 600, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-01T18:48:00+00:00"),
#         (550, 600, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-01T17:08:00+00:00"),
#         (311, 400, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-01T09:21:00+00:00"),
#     ]

#     for control, brevet_dist, start_time, expected_time in test_cases:
#         actual_time = acp_times.open_time(control, brevet_dist, start_time)
#         assert_equal(actual_time, expected_time)

# @nose.tools.istest
# def test_close_times():
#     test_cases = [
#         (150, 200, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-01T10:00:00+00:00"),
#         (700, 1000, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-03T00:45:00+00:00"),
#         (600, 600, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-02T20:00:00+00:00"),
#         (550, 600, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-02T12:40:00+00:00"),
#         (311, 400, arrow.get("2023-11-01T00:00:00+00:00"), "2023-11-01T20:44:00+00:00"),
#     ]

#     for control, brevet_dist, start_time, expected_time in test_cases:
#         actual_time = acp_times.close_time(control, brevet_dist, start_time)
#         assert_equal(actual_time, expected_time)