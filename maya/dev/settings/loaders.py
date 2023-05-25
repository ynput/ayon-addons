from pydantic import Field

from ayon_server.settings import BaseSettingsModel
from ayon_server.types import ColorRGBA_uint8



class ColorsSetting(BaseSettingsModel):
    model: ColorRGBA_uint8 = Field((209, 132, 30, 1.0), title="Model:")
    rig: ColorRGBA_uint8 = Field((59, 226, 235, 1.0), title="Rig:")
    pointcache: ColorRGBA_uint8 = Field((94, 209, 30, 1.0),
        title="Pointcache:")
    animation: ColorRGBA_uint8 = Field((94, 209, 30, 1.0),
        title="Animation:")
    ass: ColorRGBA_uint8 = Field((249, 135, 53, 1.0),
        title="Arnold StandIn:")
    camera: ColorRGBA_uint8 = Field((136, 114, 244, 1.0), title="Camera:")
    fbx: ColorRGBA_uint8 = Field((215, 166, 255, 1.0), title="FBX:")
    mayaAscii: ColorRGBA_uint8 = Field((67, 174, 255, 1.0), title="Maya Ascii:")
    mayaScene: ColorRGBA_uint8 = Field((67, 174, 255, 1.0), title="Maya Scene:")
    setdress: ColorRGBA_uint8 = Field((255, 250, 90, 1.0), title="Set Dress:")
    layout: ColorRGBA_uint8 = Field((255, 250, 90, 1.0), title="Layout:")
    vdbcache: ColorRGBA_uint8 = Field((249, 54, 0, 1.0), title="VDB Cache:")
    vrayproxy: ColorRGBA_uint8 = Field((255, 150, 12, 1.0), title="VRay Proxy:")
    vrayscene_layer: ColorRGBA_uint8 = Field((255, 150, 12, 1.0), title="VRay Scene:")
    yeticache: ColorRGBA_uint8 = Field((99, 206, 220, 1.0), title="Yeti Cache:")
    yetiRig: ColorRGBA_uint8 = Field((0, 205, 125, 1.0), title="Yeti Rig:")


class ReferenceLoaderModel(BaseSettingsModel):
    namespace: str = Field(title="Namespace")
    group_name: str = Field(title="Group name")
    display_handle: bool = Field(title="Display Handle On Load References")


class LoadersModel(BaseSettingsModel):
    colors: ColorsSetting = Field(
        default_factory=ColorsSetting,
        title="Loaded Products Outliner Colors")

    reference_loader: ReferenceLoaderModel = Field(
        default_factory=ReferenceLoaderModel,
        title="Reference Loader"
    )


DEFAULT_LOADERS_SETTING = {
    "colors": {
        "model": [
            209, 132, 30, 1.0
        ],
        "rig": [
            59, 226, 235, 1.0
        ],
        "pointcache": [
            94, 209, 30, 1.0
        ],
        "animation": [
            94, 209, 30, 1.0
        ],
        "ass": [
            249, 135, 53, 1.0
        ],
        "camera": [
            136, 114, 244, 1.0
        ],
        "fbx": [
            215, 166, 255, 1.0
        ],
        "mayaAscii": [
            67, 174, 255, 1.0
        ],
        "mayaScene": [
            67, 174, 255, 1.0
        ],
        "setdress": [
            255, 250, 90, 1.0
        ],
        "layout": [
            255, 250, 90, 1.0
        ],
        "vdbcache": [
            249, 54, 0, 1.0
        ],
        "vrayproxy": [
            255, 150, 12, 1.0
        ],
        "vrayscene_layer": [
            255, 150, 12, 1.0
        ],
        "yeticache": [
            99, 206, 220, 1.0
        ],
        "yetiRig": [
            0, 205, 125, 1.0
        ]
    },
    "reference_loader": {
        "namespace": "{asset_name}_{subset}_##_",
        "group_name": "_GRP",
        "display_handle": True
    }
}
