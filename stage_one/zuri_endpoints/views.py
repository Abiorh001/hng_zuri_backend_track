from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta


class RetrieveApiEndpoint(APIView):
    def get(self, request):
        slack_name = request.GET.get("slack_name")
        track = request.GET.get("track")

        data = {
            "slack_name": slack_name,
            "current_day": datetime.now().strftime('%A'),
            "utc_time": (datetime.utcnow() + timedelta(hours=0)).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "track": track,
            "github_file_url": "https://github.com/Abiorh001/hng_zuri_backend_track/blob/main/zuri_endpoints/views.py",
            "github_repo_url": "https://github.com/Abiorh001/hng_zuri_backend_track/tree/main",
            "status_code": 200
        }
        return Response(data)
