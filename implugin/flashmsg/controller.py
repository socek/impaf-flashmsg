from impaf.controller import Controller

from .requestable import FlashMessageRequestable
from .widget import FlashMessageWidget


class FlashMessageController(Controller, FlashMessageRequestable):

    def _create_widgets(self):
        super()._create_widgets()
        self.add_widget('flashmsg', FlashMessageWidget())
