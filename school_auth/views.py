from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SchoolAdmin, ExternalAccess
from .serializers import SchoolAdminSerializer, UserSerializer, GroupSerializer, ExternalAccessSerializer
from rest_framework import status
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.
def hello(request):
    message = 'These endpoints expose the authentication of school admins, principal and all the way down to support staff'
    return HttpResponse(message)

@api_view(['GET'])
def list_school_admins(request):
    if request.method == 'GET':
        school_admins = SchoolAdmin.objects.all()
        serializer = SchoolAdminSerializer(school_admins, many=True)
        return Response({'school_admins': serializer.data}, status=status.HTTP_200_OK)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def create_admin(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = SchoolAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'school_admin': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def getPlatformAdmins(request):
    if request.method == 'GET':
        platform_admins = User.objects.all()
        serializer = UserSerializer(platform_admins, many=True)
        return Response({'platform_admins': serializer.data}, status=status.HTTP_200_OK)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def getAdminById(request, admin_id):
    try:
        admin = User.objects.get(id=admin_id)
    except User.DoesNotExist:
        return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(admin)
        return Response({'platform_admin': serializer.data}, status=status.HTTP_200_OK)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def getPlatformGroups(request):
    if request.method == 'GET':
        platform_groups = Group.objects.all()
        serializer = GroupSerializer(platform_groups, many=True)
        return Response({'Platform Groups': serializer.data}, status=status.HTTP_200_OK)
    return Response({'error': 'Method not allow'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def getGroupById(request, group_id, *args, **kwargs):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return Response({'error': "Group not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response({'Platform Group': serializer.data}, status=status.HTTP_200_OK)
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)    

@api_view(['POST'])
def createAccessExternal(request):
    serializer = ExternalAccessSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # password is hashed automatically
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginAccess(request):
    email = request.data.get("admin_email")
    password = request.data.get("admin_password")

    if not email or not password:
        return Response(
            {"error": "Email and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = ExternalAccess.objects.get(
            admin_email=email.lower().strip()
        )
    except ExternalAccess.DoesNotExist:
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not check_password(password, user.admin_password):
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    serializer = ExternalAccessSerializer(
        user,
        context={"request": request}
    )

    return Response(
        {
            "message": "Login successful",
            "user": serializer.data
        },
        status=status.HTTP_200_OK
    )





        


