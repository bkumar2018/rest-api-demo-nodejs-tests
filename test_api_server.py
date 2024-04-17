import requests
import pytest


ENDPOINT = "http://localhost:3000/api/v1/students"
#"http://localhost:3000/api/v1/students"

# res = requests.get(ENDPOINT)
# print(res)
# print(res.json())
# print(res.status_code)



# def test_addStudent():
#     payload = {
#         "name": "Tam",
#         "email": "tam@gmail.com",
#         "age": 42,
#         "dob": "1980-12-31"
#     }
#     res = requests.post(ENDPOINT, json=payload)
#     assert res.status_code == 201
#     pass

#@pytest.mark.parametrize("name, email, age, dob", [("Cam","cam@gmail.com",42,"1980-01-01"),("Dam","dam@gmail.com",42,"1980-01-01")])
# @pytest.mark.parametrize("name, email, age, dob", [("Xam","xam@gmail.com",42,"1980-01-01")])
# def test_addStudent(name, email, age, dob):
#     payload = {
#         "name": name,
#         "email": email,
#         "age": age,
#         "dob": dob
#     }
#     res = requests.post(ENDPOINT, json=payload)
#     assert res.status_code == 201
#
#     pass

def test_getStudents():

    # Add new student
    payload = {
        "name": "Zam",
        "email": "Zam@gmail",
        "age": 42,
        "dob": "1980-12-12"
    }
    res = requests.post(ENDPOINT, json=payload)
    assert res.status_code == 201

    # Get all students, and get last added student id
    get_all_students_res = requests.get(ENDPOINT)
    assert get_all_students_res.status_code == 200
    data_of_all_students = get_all_students_res.json()
    #print(len(data_of_all_students))
    #print(data_of_all_students[len(data_of_all_students)-1])
    #print(data_of_all_students[len(data_of_all_students) - 1]["id"])
    student_id = data_of_all_students[len(data_of_all_students) - 1]["id"]

    # Get details of newly added student using Id
    get_student_from_id_res = requests.get(ENDPOINT + f"/{student_id}")
    assert get_student_from_id_res.status_code == 200
    data_of_id_students = get_student_from_id_res.json()
    print("\n Student registered name: " + data_of_id_students[len(data_of_id_students) - 1]["name"])

    # Delete the newly added student
    res_delete_student_from_id = requests.delete(ENDPOINT + f"/{student_id}")
    assert res_delete_student_from_id.status_code == 200

    pass

#def test_removeStudent():
    # Add student

    # Delete student
    # Get student and check its does not found


    # res = requests.delete(ENDPOINT + f"/{id}")
    # assert res.status_code == 200
    # pass

