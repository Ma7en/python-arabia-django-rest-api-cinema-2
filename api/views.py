from django.shortcuts import render
from django.http import request
from django.contrib.auth.models import User


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer, UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # search => (django rest frame work viewset how to do extra actions)
    @action(methods=["post"], detail=True)
    def rate_meal(self, request, pk=None):
        if "stars" in request.data:
            """
            create or update
            """
            meal = Meal.objects.get(id=pk)
            stars = request.data["stars"]
            user = request.user
            # username = request.data["username"]
            # user = User.objects.get(username=username)

            try:
                # update
                rating = Rating.objects.get(user=user.id, meal=meal.id)  # specific rste
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)

                json = {
                    "message": "Meal rate updated successfully",
                    "result": serializer.data,
                }
                return Response(json, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                # create if the rate not exist
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    "message": "Meal rate Created successfully",
                    "result": serializer.data,
                }
                return Response(json, status=status.HTTP_200_OK)

        else:
            json = {
                "message": "stars not provided",
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        response = {
            "message": "Invalid way to create or update",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {
            "message": "Invalid way to create or update",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
