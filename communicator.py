
import json
import os
import requests


class GameDACCommunicator(object):
    def __init__(self, app_name, display_app_name=None, *args, **kwargs):
        corePropsPath = os.getenv('PROGRAMDATA') + "\SteelSeries\SteelSeries Engine 3\coreProps.json" 
        self.sseAddress = json.load(open(corePropsPath))["address"]
        self.app_name = app_name
        self.display_app_name = display_app_name if display_app_name else app_name
        self.icon_color_id = getattr(kwargs, 'icon_color_id', 5)
        self.__register_metadata()

    def __register_metadata(self):
        metadata = {
            "game": self.app_name,
            "game_display_name": self.display_app_name,
            "icon_color_id": self.icon_color_id
        }
        requests.post(self._get_game_metadata_address(), json=metadata)

    def __register_event(self, event_name, gamedac_handlers):
        handlers = {
            "game": self.app_name,
            "event": event_name,
            "handlers": gamedac_handlers
        }
        requests.post(self._get_bind_game_event_address(), json=handlers)

    def __send_event(self, event_name, data_to_send):
        handlers = {
            "game": self.app_name,
            "event": event_name,
            "data": data_to_send
        }
        requests.post(self._get_game_event_address(), json=handlers)

    def _get_game_metadata_address(self):
        return "http://" + self.sseAddress + "/game_metadata"

    def _get_bind_game_event_address(self):
        return "http://" + self.sseAddress + "/bind_game_event"

    def _get_game_event_address(self):
        return "http://" + self.sseAddress + "/game_event"

    def _get_remove_game_address(self):
        return "http://" + self.sseAddress + "/remove_game"

    def register_event(self, event_name, gamedac_handlers):
        self.__register_event(event_name, gamedac_handlers)

    def send_event(self, event_name, data_to_send):
        self.__send_event(event_name, data_to_send)
