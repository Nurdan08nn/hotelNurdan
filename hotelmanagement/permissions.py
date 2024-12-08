from rest_framework import permissions
from rest_framework.permissions import BasePermission
from urllib3 import request


class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'hotel_owner':
            return False
        if request.user.role == 'client':
            return True


class IsHotelOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
      if request.user.role == 'hotel_owner':
          return False
      if request.user.role == 'client':
          return True


class IsClient(BasePermission):
    def has_object_permission(self, request, view, obj):
      if request.user.role == 'hotel_owner':
          return False
      if request.user.role == 'client':
          return True

class CannotBookOwnRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
      if request.user.role == 'hotel_owner':
          return False
      if request.user.role == 'client':
          return True
