from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Manager, Supervisor, Project, Task
from .serializers import UserSerializer, ManagerSerializer, SupervisorSerializer, ProjectSerializer, TaskSerializer
 
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')
 
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
 
    user = User.objects.create_user(username=username, email=email, password=password)
 
    if role == 'Manager':
        Manager.objects.create(user=user)
    elif role == 'Supervisor':
        Supervisor.objects.create(user=user)
 
    token = Token.objects.create(user=user)
    return Response({'message': 'User registered successfully.', 'token': token.key}, status=status.HTTP_201_CREATED)
 
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
 
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'User login successful.', 'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_profile(request):
    user = request.user
    user_data = UserSerializer(user).data
 
    manager = getattr(user, 'manager', None)
    supervisor = getattr(user, 'supervisor', None)
 
    profile_data = {
        'message': 'Profile retrieved successfully.',
        'user': user_data
    }
 
    if manager:
        manager_data = ManagerSerializer(manager).data
        profile_data['manager'] = manager_data
    elif supervisor:
        supervisor_data = SupervisorSerializer(supervisor).data
        profile_data['supervisor'] = supervisor_data
 
    return Response(profile_data, status=status.HTTP_200_OK)
 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    if not hasattr(request.user, 'manager'):
        return Response({'error': 'Only managers can create projects.'}, status=status.HTTP_403_FORBIDDEN)
 
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user.manager)
        return Response({'message': 'Project created successfully.', 'project': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_projects(request):
    projects = Project.objects.filter(created_by=request.user.manager)
    serializer = ProjectSerializer(projects, many=True)
    return Response({'message': 'Projects retrieved successfully.', 'projects': serializer.data}, status=status.HTTP_200_OK)
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id, created_by=request.user.manager)
        serializer = ProjectSerializer(project)
        return Response({'message': 'Project retrieved successfully.', 'project': serializer.data}, status=status.HTTP_200_OK)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        try:
            project = Project.objects.get(id=request.data['project'])
            if project.created_by != request.user.manager:
                return Response({'error': 'You do not have permission to add tasks to this project.'}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response({'message': 'Task created successfully.', 'task': serializer.data}, status=status.HTTP_201_CREATED)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_tasks(request, project_id):
    try:
        project = Project.objects.get(id=project_id, created_by=request.user.manager)
        tasks = project.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({'message': 'Tasks retrieved successfully.', 'tasks': serializer.data}, status=status.HTTP_200_OK)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found.'}, status=status.HTTP_404_NOT_FOUND)
 