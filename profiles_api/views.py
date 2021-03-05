from rest_framework.views import APIView
from rest_framework.response import Response
# below import is for POST & PATCH
from rest_framework import status
# below is required for a viewset
from rest_framework import viewsets

from profiles_api import serializers

# All of below code covers an APIView to support your endpoint for http methods
class HelloApiView(APIView):
    """Test API View"""
    # Below line connects to the serializers python file
    serializer_class = serializers.HelloSerializer
    
    # GET FUNCTIONALITY
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP megthods as function (get, post, patch, put, delete)',
            'Is similar to a tradituinal Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({ 'message': 'Hello', 'an_apiview': an_apiview })

    # POST FUNCTIONALITY
    def post(self, request):
        """Create a hello message with our name"""
        # Now pull data from the serializer python file
        serializer = self.serializer_class(data=request.data)
        # Now validate this input of 10 char
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # Now create a message variable as
            message = f'Hello { name }'
            return Response({'message':message})
        # What if this request failes?
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                 )

    # PUT FUNCTIONALITY
    def put(self, request, pk=None):
        """Handle updating an object on its privatekey level"""
        return Response({'method': 'PUT'})

    # PATCH FUNCTIONALITY
    def patch(self, request, pk=None):
        """Handle a partial update of an object for ex only your lastname"""
        return Response({'method': 'PATCH'})

    # DELETE FUNCTIONALITY
    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'DELETE'})    


# All of below code covers a Viewset which covers actions to apply to an API
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})