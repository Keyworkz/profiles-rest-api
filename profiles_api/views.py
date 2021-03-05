from rest_framework.views import APIView
from rest_framework.response import Response
# for POST & PATCH import
from rest_framework import status

from profiles_api import serializers


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
