from rest_framework import serializers

from solver.models import Solver

class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ['id','name']