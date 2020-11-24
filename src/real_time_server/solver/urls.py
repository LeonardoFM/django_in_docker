from django.urls import path

from .views import ( 
    SolverListCreateView, 
    SolverDetailView, 
    SolverDeleteView,
    SolverUpdateView,
)

urlpatterns = [
    path('solver/', SolverListCreateView.as_view()),
    path('solver/<pk>/', SolverDetailView.as_view()),
    path('solver/update/<pk>/', SolverUpdateView.as_view()),
    path('solver/<pk>/delete/', SolverDeleteView.as_view()),
]