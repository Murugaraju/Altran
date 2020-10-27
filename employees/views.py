from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
# Create your views here.
from .serializers import EmployeeSerializer

class Employeeviewset(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeAPIView(APIView):
    def get(request,*args,**kwargs):
        d=[]
        for i in Employee.objects.all():
            t={}
            t['EmployeeName']=i.name
            t['EmployeeId']=i.empid
            t['ReportingTo']='CEO' if i.reportingto==None else i.reportingto.name
            d.append(t)
        
        
        


        return Response(d)
