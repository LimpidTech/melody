from rest_framework_jwt import views
from rest_framework_jwt import serializers

class JSONWebTokenAPIView(views.JSONWebTokenAPIView):
    def post(self, request, *args, **kwargs):
        response = super(JSONWebTokenAPIView, self).post(request, *args, **kwargs)

        # Don't do extra work unless we successfully changed the user.
        if response.status_code < 200 or response.status_code > 299:
            return response

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            # We need to verify validity for the serializer to not get
            # angry at us, even though the parent view has done so already
            # since we had to create a new instance. Hooray! :D
            return response

        user = serializer.object.get('user')

        if not user:
            return response

        # User has authenticated, so we can update `request.user` safely.
        request.user = user

        return response


# Inherit views from JWT views to inherit new behavior.
class ObtainJSONWebToken(JSONWebTokenAPIView):
    serializer_class = serializers.JSONWebTokenSerializer


class VerifyJSONWebToken(JSONWebTokenAPIView):
    serializer_class = serializers.VerifyJSONWebTokenSerializer


class RefreshJSONWebToken(JSONWebTokenAPIView):
    serializer_class = serializers.RefreshJSONWebTokenSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()