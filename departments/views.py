from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Department
from .permissions import IsOwnerOrReadOnly
from .serializers import DepartmentSerializer
from .pagination import CustomPagination
from .filters import DepartmentFilter


class ListCreateDepartmentAPIView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DepartmentFilter

    def perform_create(self, serializer):
        # Assign the user who created the Department
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyDepartmentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]





