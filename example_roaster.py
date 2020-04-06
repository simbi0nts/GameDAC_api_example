
import random
import time

from communicator import GameDACCommunicator


communicator = GameDACCommunicator("ROASTER", display_app_name="Silly Roaster")

gamedac_handlers = [{
    "device-type": "screened-128x52",
    "mode": "screen",
    "zone": "one",
    "datas": [
        {
            "icon-id": random.randint(1, 24),
            "lines": [
                {
                    "has-text": True,
                    "context-frame-key": "first-line"
                },
                {
                    "has-text": True,
                    "context-frame-key": "second-line"
                }
            ]
        }
    ]
}]

communicator.register_event("RANDOM_ROAST", gamedac_handlers)


first_parts_of_roast = ['Incompetent', 'Stupid', 'Lazy', 'Ugly', 'Useless']
second_parts_of_roast = ['idiot', 'swine', 'scumbag', 'trash', 'peasant']


while True:
    data_to_send = {
        "value": 0,
        "frame": {
            "first-line": random.choice(first_parts_of_roast),
            "second-line": random.choice(second_parts_of_roast)
        }
    }

    communicator.send_event("RANDOM_ROAST", data_to_send)

    time.sleep(60 * 10)  # send every 10 minutes
