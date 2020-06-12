from utilities import gen

from labthings.server.find import find_component
from labthings.server.view import PropertyView

from flask import Response

class MjpegStream(PropertyView):
    """
    Real-time MJPEG stream from the microscope camera
    """

    @doc_response(200, mimetype="multipart/x-mixed-replace")
    def get(self):
        """
        MJPEG stream from the Pi camera.
        """
        camera = find_component("org.raspberrypi.camera")

        return Response(
            gen(camera), mimetype="multipart/x-mixed-replace; boundary=frame"
        )


class SnapshotStream(PropertyView):
    """
    Single JPEG snapshot from the camera stream
    """

    @doc_response(200, description="Snapshot taken", mimetype="image/jpeg")
    def get(self):
        """
        Single snapshot from the camera stream
        """
        camera = find_component("org.raspberrypi.camera")

        return Response(camera.get_frame(), mimetype="image/jpeg")
