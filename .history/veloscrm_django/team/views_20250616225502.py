from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Team
from .serializers import TeamSerializer, UserSerializer, UserCreateSerializer


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user])

    def perform_create(self, serializer):
        team = serializer.save(created_by=self.request.user)
        team.members.add(self.request.user)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {'id': serializer.data['id'], 'username': serializer.data['username'], 'email': serializer.data['email']}
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_team(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    if not team:
        return Response({'detail': 'Geen team gevonden'}, status=404)

    serializer = TeamSerializer(team)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_member(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    if not team:
        return Response({'detail': 'Geen team gevonden'}, status=404)

    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is verplicht'}, status=400)

    try:
        user = User.objects.get(username=email)
    except User.DoesNotExist:
        return Response({'error': 'Gebruiker niet gevonden'}, status=404)

    team.members.add(user)
    return Response({'message': f'{user.username} toegevoegd aan team'})