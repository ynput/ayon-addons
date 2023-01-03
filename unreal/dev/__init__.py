from typing import Type

from openpype.addons import BaseServerAddon

from .settings import UnrealSettings, DEFAULT_VALUES


class UnrealAddon(BaseServerAddon):
    name = "unreal"
    title = "Unreal"
    version = "1.0.0"
    settings_model: Type[UnrealSettings] = UnrealSettings
    frontend_scopes = {}
    services = {}

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)
