from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

def custom_logout(request):
    logout(request)
    return redirect('/')  # Redirect to the home page after logout
