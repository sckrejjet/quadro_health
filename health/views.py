from django.shortcuts import render
from django.http import JsonResponse
from .con1 import get_hospitals_with_service, add_hospital_to_db, add_service_to_db
from .helpers import generate_hosp_list


def home(request):
    hosps_sql = get_hospitals_with_service('')

    context = {
        'hospitals': hosps_sql
    }

    return render(request, 'health/home.html', context)


def about(request):
    return render(request, 'health/about.html', {'title': 'About'})


def adding_page(request):
    return render(request, 'health/add_hospital.html', {'title': 'Add New Hospital!'})


def add_hospital(request):
    if request.is_ajax() and request.method == 'GET':
        add_hospital_to_db(request.GET)

        return JsonResponse({}, status=200)


def filtered_hospitals(request):
    if request.is_ajax() and request.method == 'GET':
        data = request.GET['text']

        hosps_sql = get_hospitals_with_service(data)

        result_html = generate_hosp_list(hosps_sql)

        resp_data = {
            'html': result_html
        }

        return JsonResponse(resp_data, status=200)


# def adding_service_page(request):

def add_service(request):
    if request.is_ajax() and request.method == 'GET':
        add_service_to_db(request.GET)

        return JsonResponse({}, status=200)