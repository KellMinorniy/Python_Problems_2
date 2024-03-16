import subprocess
import pytest

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact': [
        (5, 120)
    ]
}

from fact import fact_it

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

#fact
from fact import fact_it, fact_rec

@pytest.mark.parametrize("input_data, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

def test_fact_rec():
    assert fact_rec(0) == 1
    assert fact_rec(1) == 1
    assert fact_rec(5) == 120
    assert fact_rec(10) == 3628800

def test_fact_it():
    assert fact_it(0) == 1
    assert fact_it(1) == 1
    assert fact_it(5) == 120
    assert fact_it(10) == 3628800

def test_fact_comparison():
    rec_time = fact_rec(5)
    it_time = fact_it(5)
    assert it_time < rec_time

#fibonacci
from fibonacci import fibonacci, cube
def test_fibonacci():
    input_data = "5"
    expected_output = "[0, 1, 1, 8, 27]"
    assert run_script('fibonacci.py', [input_data]) == expected_output

def test_cube():
    assert cube(0) == 0
    assert cube(1) == 1
    assert cube(2) == 8
    assert cube(3) == 27

def test_fibonacci():
    assert fibonacci(0) == [0]
    assert fibonacci(1) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_cube():
    assert list(map(cube, fibonacci(5))) == [0, 1, 1, 8, 27]

#file_search
from file_search import find_file
def test_file_search():
    filename = "test.py"
    expected_output = "Введите название файла"
    assert run_script('file_search.py', [filename]) == expected_output

#files_sort
from files_sort import main
def test_files_sort():
    directory = "."
    expected_output = "Введите путь к директории"
    assert run_script('files_sort.py', [directory]) == expected_output

#my_sum_argv
from my_sum_argv import my_sum
def test_my_sum_argv():
    input_data = "1 2 3 4 5"
    expected_output = "0"
    assert run_script('my_sum_argv.py', [input_data]) == expected_output

def test_my_sum_no_arguments():
    assert my_sum() == 0

def test_my_sum_single_argument():
    assert my_sum(5) == 5

def test_my_sum_multiple_arguments():
    assert my_sum(1, 2, 3, 4, 5) == 15

#show_employee
from show_employee import show_employee
def test_show_employee():
    input_data = "Иванов Иван Иванович 30000"
    expected_output = "Иванов Иван Иванович: 30000р.\nАртемов Артем Артемович: 100000р."
    assert run_script('show_employee.py', [input_data]) == expected_output


def test_show_employee_with_salary():
    assert show_employee("Иванов Иван Иванович", 30000) == "Иванов Иван Иванович: 30000р."

def test_show_employee_without_salary():
    assert show_employee("Артемов Артем Артемович") == "Артемов Артем Артемович: 100000р."

def test_show_employee_with_custom_default_salary():
    original_default_salary = 100000
    new_default_salary = 50000
    assert show_employee("Петров Петр Петрович") == f"Петров Петр Петрович: {original_default_salary}р."
    show_employee.default_salary = new_default_salary
    assert show_employee("Петров Петр Петрович") == f"Петров Петр Петрович: {new_default_salary}р."
    show_employee.default_salary = original_default_salary

#sum_and_sub
from sum_and_sub import sum_and_sub
def test_sum_and_sub():
    input_data = "10.5 2234.2"
    expected_output = "Сумма: 2244.7\nРазность: -2223.7"
    assert run_script('sum_and_sub.py', [input_data]) == expected_output

def test_sum_and_sub_positive_numbers():
    sum_result, sub_result = sum_and_sub(10.5, 2234.2)
    assert sum_result == 2244.7
    assert sub_result == -2223.7

def test_sum_and_sub_negative_numbers():
    sum_result, sub_result = sum_and_sub(-10.5, -2234.2)
    assert sum_result == -2223.7
    assert sub_result == 2223.7

def test_sum_and_sub_zero():
    sum_result, sub_result = sum_and_sub(0, 2234.2)
    assert sum_result == 2234.2
    assert sub_result == -2234.2

#average_scores
from average_score import compute_average_scores

def test_compute_average_scores_single_student():
    input_data = "1 3\n85 90 78"
    expected_output = (85.0,)
    assert compute_average_scores(input_data) == expected_output

def test_compute_average_scores_multiple_students():
    input_data = "2 3\n85 90 78\n88 92 88"
    expected_output = (85.0, 88.0)
    assert compute_average_scores(input_data) == expected_output

def test_compute_average_scores_multiple_subjects():
    input_data = "1 4\n85 90 78 92"
    expected_output = (85.0,)
    assert compute_average_scores(input_data) == expected_output

def test_compute_average_scores_no_students():
    input_data = "0 3\n85 90 78"
    expected_output = ()
    assert compute_average_scores(input_data) == expected_output

def test_compute_average_scores_no_subjects():
    input_data = "1 0\n85 90 78"
    expected_output = (0.0,)
    assert compute_average_scores(input_data) == expected_output

#plane_angle
import math
from plane_angle import Point, plane_angle

def test_point_subtraction():
    A = Point(1, 2, 3)
    B = Point(4, 5, 6)
    AB = B - A
    assert AB.x == 3
    assert AB.y == 3
    assert AB.z == 3

def test_point_dot_product():
    A = Point(1, 2, 3)
    B = Point(4, 5, 6)
    dot_product = A * B
    assert dot_product == 32

def test_point_cross_product():
    A = Point(1, 2, 3)
    B = Point(4, 5, 6)
    cross_product = A.cross(B)
    assert cross_product.x == -3
    assert cross_product.y == 6
    assert cross_product.z == -3

def test_point_magnitude():
    A = Point(1, 2, 3)
    magnitude = A.magnitude()
    assert math.isclose(magnitude, 3.741657517027076, rel_tol=1e-9)

def test_plane_angle_90_degrees():
    A = Point(0, 0, 0)
    B = Point(1, 0, 0)
    C = Point(0, 1, 0)
    D = Point(0, 0, 1)
    angle = plane_angle(A, B, C, D)
    assert math.isclose(angle, 90, rel_tol=1e-9), f"Expected 90 degrees, but got {angle} degrees"

#Phone_number
from phone_number import sort_phone

def test_sort_phone_numbers():
    input_numbers = [
        "89123456789",
        "+79123456789",
        "09123456789",
        "9123456789",
        "89123456788",
        "89123456787"
    ]
    expected_output = [
        "+7(912)345-67-89",
        "+7(912)345-67-88",
        "+7(912)345-67-87",
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-88"
    ]
    assert sort_phone(input_numbers) == expected_output

def test_sort_phone_numbers_with_special_cases():
    input_numbers = [
        "9123456789",
        "09123456789",
        "89123456789",
        "+79123456789"
    ]
    expected_output = [
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-89"
    ]
    assert sort_phone(input_numbers) == expected_output

def test_sort_phone_numbers_with_duplicates():
    input_numbers = [
        "89123456789",
        "89123456789",
        "89123456789"
    ]
    expected_output = [
        "+7(912)345-67-89"
    ]
    assert sort_phone(input_numbers) == expected_output

def test_sort_phone_numbers():
    input_numbers = [
        "89123456789",
        "+79123456789",
        "09123456789",
        "9123456789",
        "89123456788",
        "89123456787"
    ]
    expected_output = [
        "+7(912)345-67-87",
        "+7(912)345-67-88",
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-88",
        "+7(912)345-67-89"
    ]
    assert sort_phone(input_numbers) == expected_output

def test_sort_phone_numbers_with_special_cases():
    input_numbers = [
        "9123456789",
        "09123456789",
        "89123456789",
        "+79123456789"
    ]
    expected_output = [
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-89"
    ]
    assert sort_phone(input_numbers) == expected_output

def test_sort_phone_numbers_with_duplicates():
    input_numbers = [
        "89123456789",
        "89123456789",
        "89123456789"
    ]
    expected_output = [
        "+7(912)345-67-89"
    ]
    assert sort_phone(input_numbers) == expected_output

def test_sort_phone_numbers_with_different_formats():
    input_numbers = [
        "89123456789",
        "+79123456789",
        "09123456789",
        "9123456789"
    ]
    expected_output = [
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-89",
        "+7(912)345-67-89"
    ]
    assert sort_phone(input_numbers) == expected_output

def test_sort_phone_numbers_with_empty_list():
    input_numbers = []
    expected_output = []
    assert sort_phone(input_numbers) == expected_output

#people_sort

from people_sort import name_format

def test_name_format_single_person():
    people = [["John", "Doe", "30", "M"]]
    expected_output = "Mr. John Doe"
    assert name_format(people) == expected_output

def test_name_format_multiple_people():
    people = [
        ["John", "Doe", "30", "M"],
        ["Jane", "Doe", "25", "F"],
        ["Alice", "Smith", "35", "F"]
    ]
    expected_output = [
        "Ms. Jane Doe",
        "Mr. John Doe",
        "Ms. Alice Smith"
    ]
    assert name_format(people) == expected_output

def test_name_format_same_age():
    people = [
        ["John", "Doe", "30", "M"],
        ["Jane", "Doe", "30", "F"]
    ]
    expected_output = [
        "Mr. John Doe",
        "Ms. Jane Doe"
    ]
    assert name_format(people) == expected_output

def test_name_format_empty_list():
    people = []
    expected_output = []
    assert name_format(people) == expected_output

def test_name_format_single_person():
    people = [["John", "Doe", "30", "M"]]
    expected_output = "Mr. John Doe"
    assert name_format(people) == expected_output

def test_name_format_multiple_people():
    people = [
        ["John", "Doe", "30", "M"],
        ["Jane", "Doe", "25", "F"],
        ["Alice", "Smith", "35", "F"]
    ]
    expected_output = [
        "Ms. Jane Doe",
        "Mr. John Doe",
        "Ms. Alice Smith"
    ]
    assert name_format(people) == expected_output

def test_name_format_same_age():
    people = [
        ["John", "Doe", "30", "M"],
        ["Jane", "Doe", "30", "F"]
    ]
    expected_output = [
        "Mr. John Doe",
        "Ms. Jane Doe"
    ]
    assert name_format(people) == expected_output

#complex_numbers
from complex_numbers import Complex 

def test_addition():
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    result = c1 + c2
    assert result.real == 4
    assert result.imaginary == 6

def test_subtraction():
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    result = c1 - c2
    assert result.real == -2
    assert result.imaginary == -2

def test_multiplication():
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    result = c1 * c2
    assert result.real == -5
    assert result.imaginary == 10

def test_division():
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    result = c1 / c2
    assert round(result.real, 2) == -0.42
    assert round(result.imaginary, 2) == 0.29

def test_modulus():
    c = Complex(3, 4)
    result = c.mod()
    assert round(result, 2) == 5.00

#circle_sqake_mk
    
from circle_sqake_mk import circle_sqake_mk

def test_circle_sqake_mk():
    r = 5
    n = 100000
    mk_area = circle_sqake_mk(r, n)
    formula_area = 3.14159 * r**2
    mk_error = abs(mk_area - formula_area) / formula_area * 100

    assert mk_error <= 1

    assert abs(mk_area - formula_area) <= 0.01 * formula_area

import pytest
from circle_sqake_mk import circle_sqake_mk

def test_circle_sqake_mk_small_circle():
    r = 1
    n = 100000
    mk_area = circle_sqake_mk(r, n)
    formula_area = 3.14159 * r**2
    mk_error = abs(mk_area - formula_area) / formula_area * 100
    assert mk_error <= 1

def test_circle_sqake_mk_large_circle():
    r = 10
    n = 100000
    mk_area = circle_sqake_mk(r, n)
    formula_area = 3.14159 * r**2
    mk_error = abs(mk_area - formula_area) / formula_area * 100
    assert mk_error <= 1

def test_circle_sqake_mk_negative_radius():
    r = -5
    n = 100000
    mk_area = circle_sqake_mk(r, n)
    assert mk_area == 0, "Площадь окружности с отрицательным радиусом должна быть равна нулю"

def test_circle_sqake_mk_zero_radius():
    r = 0
    n = 100000
    mk_area = circle_sqake_mk(r, n)
    assert mk_area == 0, "Площадь окружности с нулевым радиусом должна быть равна нулю"

#Log_Decorator

import pytest
import os
from log_decorator import function_logger, greeting_format

def test_function_logger_decorator():
    log_file_path = 'test.log'
    if os.path.exists(log_file_path):
        os.remove(log_file_path) 

    greeting_format('Artem')

    with open(log_file_path, 'r') as file:
        log_content = file.read()

    assert 'greeting_format' in log_content
    assert 'Hello Artem!' in log_content
    assert 'seconds' in log_content

def test_function_logger_multiple_calls():
    log_file_path = 'test.log'
    if os.path.exists(log_file_path):
        os.remove(log_file_path) 

    greeting_format('Artem')
    greeting_format('John')

    with open(log_file_path, 'r') as file:
        log_content = file.read()

    assert log_content.count('greeting_format') == 2
    assert log_content.count('Hello Artem!') == 1
    assert log_content.count('Hello John!') == 1

def test_function_logger_no_log_file():
    log_file_path = 'non_existent_test.log'
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    greeting_format('Artem')

    assert os.path.exists(log_file_path)

def test_function_logger_log_file_creation():
    log_file_path = 'test.log'
    if os.path.exists(log_file_path):
        os.remove(log_file_path) 

    greeting_format('Artem')

    assert os.path.exists(log_file_path)

def test_function_logger_log_file_append():
    log_file_path = 'test.log'
    if os.path.exists(log_file_path):
        os.remove(log_file_path) 

    greeting_format('Artem')
    greeting_format('John')

    with open(log_file_path, 'r') as file:
        log_content = file.read()

    assert log_content.count('Hello Artem!') == 1
    assert log_content.count('Hello John!') == 1