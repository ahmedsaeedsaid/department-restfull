import json
from behave import given, when, then
from django.contrib.auth.models import User
from departments.models import Department
from rest_framework.test import APIClient
from behave.runner import Context

@given("a user exists and is authenticated")
def step_impl(context: Context):
    context.client = APIClient()
    context.user = User.objects.create_user(username="PERSON123", password="PASS@123")
    context.client.force_authenticate(user=context.user)

@then("the user should be authenticated")
def step_impl(context: Context):
    response = context.client.get("/api/v1/departments/")
    assert response.status_code != 401, "Expected authenticated access, got 401 Unauthorized"


@given('a department named "{name}" exists')
def step_impl(context, name):
    department = Department.objects.create(name=name, creator= context.user)
    context.department = department

@when('I POST to "{url}" with name "{name}":')
def step_impl(context, url, name):
    data = {"name": name}
    response = context.client.post(url, data, format='json')
    context.response = response



@when('I GET "{url}"')
def step_impl(context, url):
    context.response = context.client.get(url)
    print(context.client.get(url).content.decode())


@when('I PUT "{url}" with name "{name}":')
def step_impl(context, url, name):
    data = {"name": name}
    context.response = context.client.put((url + f'/{context.department.id}/'), data, format='json')

@when('I DELETE "{url}"')
def step_impl(context, url):
    context.response = context.client.delete(url + f'/{context.department.id}/')
    print((url + f'/{context.department.id}/'))

@then("the response status should be {status:d}")
def step_impl(context, status):
    assert context.response.status_code == status, f"Got {context.response.status_code}"

@then('the response should contain "{text}"')
def step_impl(context, text):
    assert text in context.response.content.decode()

@given("the departments table is empty")
def step_impl(context):
    Department.objects.all().delete()