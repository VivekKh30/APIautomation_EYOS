import logging
import time
import requests
from behave import *
from behave import model
from behave.formatter import null
from utilities.AddResources import *
from utilities.BaseClass import BaseClass
from utilities.configurations import get_endpoint

config_property = 'API'
host = 'get_covid_data'
country = 'country'
country_code = 'code'
latitude = 'latitude'
longitude = 'longitude'
baseclass = BaseClass()
url = get_endpoint()[config_property][host] + addresourcse.path


@given('Request is sent to GET Covid-19 data with {code}')
def step_impl(context, code):
    time.sleep(0.5)
    querystring = {"code": code}
    context.response = baseclass.getRequest(url, baseclass.getDefaultHeaders(), querystring)
    baseclass.getlogger().info(context.response)
    context.Covid_case_details = context.response.json()
    context.expected_country_code = code


@then('response is received with HTTP status code {statuscode:d}')
def step_impl(context, statuscode):
    time.sleep(0.5)
    baseclass.getlogger().info(context.response.status_code)
    assert context.response.status_code == statuscode


@then('the response body should return expected details as below')
def step_impl(context):
    time.sleep(0.5)
    for row in context.table:
        row[country], row[country_code], row[latitude], row[longitude]

    for Covid_case_detail in context.Covid_case_details:
        for key, value in Covid_case_detail.items():
            assert value is not null

    actual_response = context.Covid_case_details[0]
    assert actual_response[country] == row[country]
    assert actual_response[country_code] == row[country_code]
    assert actual_response[latitude] == float(row[latitude])
    assert actual_response[longitude] == float(row[longitude])


@when('Request is sent to GET Covid-19 data without country code')
def step_impl(context):
    time.sleep(0.5)
    querystring = {"code": ''}
    context.response = baseclass.getRequest(url, baseclass.getDefaultHeaders(), querystring)
    baseclass.getlogger().info(context.response)
    context.Covid_case_details = context.response.json()


@then('the empty response body should be returned')
def step_impl(context):
    time.sleep(0.5)
    baseclass.getlogger().info(context.response.status_code)
    assert context.Covid_case_details == []


@when('Request is sent to GET Covid-19 data with invalid {country_code}')
def step_impl(context, country_code):
    time.sleep(0.5)
    querystring = {"code": country_code}
    context.response = baseclass.getRequest(url, baseclass.getDefaultHeaders(), querystring)
    baseclass.getlogger().info(context.response)
    context.Covid_case_details = context.response.json()


@then('error response is received with HTTP status code 400')
def step_impl(context):
    time.sleep(0.5)
    baseclass.getlogger().info(context.response.status_code)
    assert context.response.status_code == 400


@then('response should contain an error message as "Invalid country code"')
def step_impl(context):
    time.sleep(0.5)
    error_message = ''
    assert error_message == "Invalid country code"


@when('Request is sent to GET Covid-19 data without an API key')
def step_impl(context):
    time.sleep(0.5)
    headers = {
    }
    querystring = {"code": "IN"}
    context.response = baseclass.getRequest(url, headers, querystring)
    baseclass.getlogger().info(context.response)
    context.Covid_case_details = context.response.json()


@then('error response is received with HTTP status code 401')
def step_impl(context):
    time.sleep(0.5)
    baseclass.getlogger().info(context.response.status_code)
    assert context.response.status_code == 401


@then(
    'response should contain an error message as "Invalid API key. Go to https://docs.rapidapi.com/docs/keys for '
    'more info."')
def step_impl(context):
    time.sleep(0.5)
    assert context.Covid_case_details['message'] == 'Invalid API key. Go to https://docs.rapidapi.com/docs/keys for ' \
                                                    'more info.'


@when('Request is sent to GET Covid-19 data with an invalid API key')
def step_impl(context):
    time.sleep(0.5)
    headers = {'x-rapidapi-key': 'fdwef'}
    querystring = {"code": "IN"}
    context.response = baseclass.getRequest(url, headers, querystring)
    baseclass.getlogger().info(context.response)
    context.Covid_case_details = context.response.json()


@then('error response is received with HTTP status code 403')
def step_impl(context):
    time.sleep(0.5)
    baseclass.getlogger().info(context.response.status_code)
    assert context.response.status_code == 403


@then('response should contain an error message as "You are not subscribed to this API."')
def step_impl(context):
    time.sleep(0.5)
    assert context.Covid_case_details['message'] == 'You are not subscribed to this API.'


@when('Request is sent to GET Covid-19 data without query parameter')
def step_impl(context):
    time.sleep(0.5)
    querystring = {}
    context.response = baseclass.getRequest(url, baseclass.getDefaultHeaders(), querystring)
    baseclass.getlogger().info(context.response)
    context.Covid_case_details = context.response.json()


@then('response should contain an error message as "Bad Request"')
def step_impl(context):
    time.sleep(0.5)
    baseclass.getlogger().info(context.response.status_code)
    assert context.Covid_case_details['detail'] == 'Bad Request'


@given('Request is sent to GET Covid-19 data for {code} and {code2}')
def step_impl(context, code, code2):
    time.sleep(1)
    querystring = {"code": code}
    context.response = baseclass.getRequest(url, baseclass.getDefaultHeaders(), querystring)
    baseclass.getlogger().info(context.response)
    querystring2 = {"code": code2}
    time.sleep(1.5)
    context.response2 = baseclass.getRequest(url, baseclass.getDefaultHeaders(), querystring2)
    baseclass.getlogger().info(context.response2)
    context.Covid_case_details = context.response.json()
    context.Covid_case_details2 = context.response2.json()


@then('Number of confirmed cases for IN should be greater than IT')
def step_impl(context):
    time.sleep(0.5)
    actual_response = context.Covid_case_details[0]
    actual_response2 = context.Covid_case_details2[0]
    assert actual_response['confirmed'] > actual_response2['confirmed']
