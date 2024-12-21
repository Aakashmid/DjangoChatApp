from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializer import ServerSerializer, ChannelSerializer

server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            description="Filter servers by category",
            required=False,
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            description="Specify the quantity of servers to retrieve",
            required=False,
        ),
        OpenApiParameter(
            name="by_user",
            type=OpenApiTypes.BOOL,
            description="Filter servers by user",
            required=False,
        ),
        OpenApiParameter(
            name="by_serverid",
            type=OpenApiTypes.STR,
            description="Filter servers by server ID",
            required=False,
        ),
        OpenApiParameter(
            name="with_num_members",
            type=OpenApiTypes.BOOL,
            description="Include the number of members in the response",
            required=False,
        ),
    ],
)
