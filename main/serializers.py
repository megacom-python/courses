from typing import Any, Dict
from rest_framework import serializers
from .models import Course, Contact, Category, Branch


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ("course",)


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ("course",)


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data: Dict[str, Any]):
        contacts_data = validated_data.pop("contacts")
        branches_data = validated_data.pop("branches")
        instance = Course.objects.create(**validated_data)
        for contact_data in contacts_data:
            Contact.objects.create(course=instance, **contact_data)
        for branch_data in branches_data:
            Branch.objects.create(course=instance, **branch_data)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
