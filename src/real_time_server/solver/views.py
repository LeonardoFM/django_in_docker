from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from solver.models import Solver

from .serializers import SolverSerializer

class SolverListCreateView(ListCreateAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer


class SolverDetailView(RetrieveAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer


class SolverUpdateView(UpdateAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer


class SolverDeleteView(DestroyAPIView):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer
