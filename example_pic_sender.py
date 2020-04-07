import time

from communicator import GameDACCommunicator
from bitmap_images import pepe

communicator = GameDACCommunicator("ROASTER", display_app_name="Silly Roaster")

image_data = pepe  # pepe

gamedac_handlers = [{
    "device-type": "screened-128x52",
    "mode": "screen",
    "zone": "one",
    "datas": [
        {
            "has-text": False,
            "image-data": image_data
        }
    ]
}]

communicator.register_event("SEND_PIC", gamedac_handlers)

while True:
    data_to_send = {
        "value": 0
    }

    communicator.send_event("SEND_PIC", data_to_send)

    time.sleep(60 * 10)  # send every 10 minutes
