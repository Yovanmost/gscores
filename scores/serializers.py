from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    total_group_a = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def get_total_group_a(self, obj):
        # Ensure these fields are not None
        toan = obj.toan or 0
        vat_li = obj.vat_li or 0
        hoa_hoc = obj.hoa_hoc or 0
        return toan + vat_li + hoa_hoc