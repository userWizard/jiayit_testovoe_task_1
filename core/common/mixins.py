from rest_framework import generics

class BaseCreateListRetriceUpdateDestroyApiVew(
    generics.CreateAPIView,
    generics.ListAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView
):
    ...