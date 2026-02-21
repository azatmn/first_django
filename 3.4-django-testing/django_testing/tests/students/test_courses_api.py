import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make(Course, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make(Student, **kwargs)
    return factory


@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    course = course_factory()
    response = client.get(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 200
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    courses = course_factory(_quantity=3)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    assert len(response.data) == 3
    ids = {c['id'] for c in response.data}
    for course in courses:
        assert course.id in ids


@pytest.mark.django_db
def test_filter_courses_by_id(client, course_factory):
    courses = course_factory(_quantity=5)
    target = courses[2]
    response = client.get('/api/v1/courses/', data={'id': target.id})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == target.id


@pytest.mark.django_db
def test_filter_courses_by_name(client, course_factory):
    course_factory(_quantity=4)
    target = course_factory(name='Unique Course Name')
    response = client.get('/api/v1/courses/', data={'name': 'Unique Course Name'})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == target.name


@pytest.mark.django_db
def test_create_course(client):
    data = {'name': 'New Course', 'students': []}
    response = client.post('/api/v1/courses/', data=data, format='json')
    assert response.status_code == 201
    assert response.data['name'] == 'New Course'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(name='Old Name')
    data = {'name': 'Updated Name', 'students': []}
    response = client.put(f'/api/v1/courses/{course.id}/', data=data, format='json')
    assert response.status_code == 200
    assert response.data['name'] == 'Updated Name'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    response = client.delete(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 204