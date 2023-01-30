from typing import Literal
from pydantic import validator, Field
from ayon_server.settings import (
    BaseSettingsModel,
    ensure_unique_names
    MultiplatformPathListModel,
)

from .common import KnobModel


class NodesModel(BaseSettingsModel):
    """# TODO: This needs to be somehow labeled in settings panel
    or at least it could show gist of configuration
    """
    plugins: list[str] = Field(
        title="Used in plugins"
    )
    # TODO: rename `nukeNodeClass` to `nuke_node_class`
    nukeNodeClass: str = Field(
        title="Nuke Node Class",
    )

    """ # TODO: Need complete rework of knob types
    in nuke integration. We could not support v3 style of settings.
    """
    knobs: list[KnobModel] = Field(
        title="Knobs",
    )

    @validator("knobs")
    def ensure_unique_names(cls, value):
        """Ensure name fields within the lists have unique names."""
        ensure_unique_names(value)
        return value


class NodesSetting(BaseSettingsModel):
    # TODO: rename `requiredNodes` to `required_nodes`
    requiredNodes: list[NodesModel] = Field(
        title="Plugin required",
        default_factory=list
    )
    # TODO: rename `overrideNodes` to `override_nodes`
    overrideNodes: list[NodesModel] = Field(
        title="Plugin's node overrides",
        default_factory=list
    )

ocio_configs_switcher_enum = [
    {"value": "nuke-default", "label": "nuke-default"},
    {"value": "spi-vfx", "label": "spi-vfx"},
    {"value": "spi-anim", "label": "spi-anim"},
    {"value": "aces_0.1.1", "label": "aces_0.1.1"},
    {"value": "aces_0.7.1" , "label": "aces_0.7.1"},
    {"value": "aces_1.0.1", "label": "aces_1.0.1"},
    {"value": "aces_1.0.3", "label": "aces_1.0.3"},
    {"value": "aces_1.1", "label": "aces_1.1"},
    {"value": "aces_1.2", "label": "aces_1.2"},
    {"value": "aces_1.3", "label": "aces_1.3"},
    {"value": "custom", "label": "custom"}
]

class WorkfileColorspaceSettings(BaseSettingsModel):
    """Nuke workfile colorspace preset. """
    """# TODO: enhance settings with host api:
    we need to add mapping to resolve properly keys.
    Nuke is excpecting camel case key names,
    but for better code consistency we need to
    be  using snake_case:

    color_management = colorManagement
    ocio_config = OCIO_config
    custom = customOCIOConfigPath
    working_space_name = workingSpaceLUT
    monitor_name = monitorLut
    monitor_out_name = monitorOutLut
    int_8_name = int8Lut
    int_16_name = int16Lut
    log_name = logLut
    float_name = floatLut
    """

    colorManagement: Literal["Nuke", "OCIO"] = Field(
        title="Color Management"
    )

    OCIO_config: str = Field(
        title="OpenColorIO Config",
        description="Switch between OCIO configs",
        enum_resolver=lambda: ocio_configs_switcher_enum,
        conditionalEnum=True
    )

    customOCIOConfigPath: MultiplatformPathListModel = Field(
        default_factory=MultiplatformPathListModel,
        title="Custom OCIO config path"
    )

    workingSpaceLUT: str = Field(
        title="Working Space"
    )
    monitorLut: str = Field(
        title="Monitor"
    )
    monitorOutLut: str = Field(
        title="Monitor Output"
    )
    int8Lut: str = Field(
        title="8-bit files"
    )
    int16Lut: str = Field(
        title="16-bit files"
    )
    logLut: str = Field(
        title="Log files"
    )
    floatLut: str = Field(
        title="Float files"
    )


class ReadColorspaceRulesItems(BaseSettingsModel):
    _layout = "expanded"

    regex: str = Field("", title="Regex expression")
    colorspace: str = Field("", title="Colorspace")

class RegexInputsModel(BaseSettingsModel):
    inputs: list[ReadColorspaceRulesItems] = Field(
        default_factory=list,
        title="Inputs"
    )

class ViewProcessModel(BaseSettingsModel):
    viewerProcess: str = Field(
        title="Viewer Process Name"
    )

class ImageIOSettings(BaseSettingsModel):
    """Nuke color management project settings. """
    _isGroup: bool = True

    enabled: bool

    """# TODO: enhance settings with host api:
    to restruture settings for simplification.

    now: nuke/imageio/viewer/viewerProcess
    future: nuke/imageio/viewer
    """
    viewer: ViewProcessModel = Field(
        default_factory=ViewProcessModel,
        title="Viewer",
        description="""Viewer profile is used during
        Creation of new viewer node at knob viewerProcess"""
    )

    """# TODO: enhance settings with host api:
    to restruture settings for simplification.

    now: nuke/imageio/baking/viewerProcess
    future: nuke/imageio/baking
    """
    baking: ViewProcessModel = Field(
        default_factory=ViewProcessModel,
        title="Baking",
        description="""Baking profile is used during
        publishing baked colorspace data at knob viewerProcess"""
    )

    workfile: WorkfileColorspaceSettings = Field(
        default_factory=WorkfileColorspaceSettings,
        title="Workfile"
    )

    nodes: NodesSetting = Field(
        default_factory=NodesSetting,
        title="Nodes"
    )
    """# TODO: enhance settings with host api:
    - old settings are using `regexInputs` key but we
      need to rename to `regex_inputs`
    - no need for `inputs` middle part. It can stay
      directly on `regex_inputs`
    """
    regexInputs:  RegexInputsModel = Field(
        default_factory=RegexInputsModel,
        title="Assign colorspace to read nodes via rules"
    )


DEFAULT_IMAGEIO_SETTINGS = {
    "enabled": True,
    "viewer": {
        "viewerProcess": "sRGB"
    },
    "baking": {
        "viewerProcess": "rec709"
    },
    "workfile": {
        "colorManagement": "Nuke",
        "OCIO_config": "nuke-default",
        "customOCIOConfigPath": {
            "windows": [],
            "darwin": [],
            "linux": []
        },
        "workingSpaceLUT": "linear",
        "monitorLut": "sRGB",
        "monitorOutLut": "rec709",
        "int8Lut": "sRGB",
        "int16Lut": "sRGB",
        "logLut": "Cineon",
        "floatLut": "linear"
    },
    "nodes": {
        "requiredNodes": [
            {
                "plugins": [
                    "CreateWriteRender"
                ],
                "nukeNodeClass": "Write",
                "knobs": [
                    {
                        "type": "text",
                        "name": "file_type",
                        "text": "exr"
                    },
                    {
                        "type": "text",
                        "name": "datatype",
                        "text": "16 bit half"
                    },
                    {
                        "type": "text",
                        "name": "compression",
                        "text": "Zip (1 scanline)"
                    },
                    {
                        "type": "boolean",
                        "name": "autocrop",
                        "boolean": True
                    },
                    {
                        "type": "color_gui",
                        "name": "tile_color",
                        "color_gui": [
                            186,
                            35,
                            35
                        ]
                    },
                    {
                        "type": "text",
                        "name": "channels",
                        "text": "rgb"
                    },
                    {
                        "type": "text",
                        "name": "colorspace",
                        "text": "linear"
                    },
                    {
                        "type": "boolean",
                        "name": "create_directories",
                        "boolean": True
                    }
                ]
            },
            {
                "plugins": [
                    "CreateWritePrerender"
                ],
                "nukeNodeClass": "Write",
                "knobs": [
                    {
                        "type": "text",
                        "name": "file_type",
                        "text": "exr"
                    },
                    {
                        "type": "text",
                        "name": "datatype",
                        "text": "16 bit half"
                    },
                    {
                        "type": "text",
                        "name": "compression",
                        "text": "Zip (1 scanline)"
                    },
                    {
                        "type": "boolean",
                        "name": "autocrop",
                        "boolean": True
                    },
                    {
                        "type": "color_gui",
                        "name": "tile_color",
                        "color_gui": [
                            171,
                            171,
                            10
                        ]
                    },
                    {
                        "type": "text",
                        "name": "channels",
                        "text": "rgb"
                    },
                    {
                        "type": "text",
                        "name": "colorspace",
                        "text": "linear"
                    },
                    {
                        "type": "boolean",
                        "name": "create_directories",
                        "boolean": True
                    }
                ]
            },
            {
                "plugins": [
                    "CreateWriteStill"
                ],
                "nukeNodeClass": "Write",
                "knobs": [
                    {
                        "type": "text",
                        "name": "file_type",
                        "text": "tiff"
                    },
                    {
                        "type": "text",
                        "name": "datatype",
                        "text": "16 bit"
                    },
                    {
                        "type": "text",
                        "name": "compression",
                        "text": "Deflate"
                    },
                    {
                        "type": "color_gui",
                        "name": "tile_color",
                        "color_gui": [
                            56,
                            162,
                            7
                        ]
                    },
                    {
                        "type": "text",
                        "name": "channels",
                        "text": "rgb"
                    },
                    {
                        "type": "text",
                        "name": "colorspace",
                        "text": "sRGB"
                    },
                    {
                        "type": "boolean",
                        "name": "create_directories",
                        "boolean": True
                    }
                ]
            }
        ],
        "overrideNodes": []
    },
    "regexInputs": {
        "inputs": [
            {
                "regex": "(beauty).*(?=.exr)",
                "colorspace": "linear"
            }
        ]
    }
}
