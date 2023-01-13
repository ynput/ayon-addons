from pydantic import Field

from ayon_server.settings import BaseSettingsModel


class SimpleCreatorPlugin(BaseSettingsModel):
    _layout = "expanded"
    family: str = Field("", title="Family")
    # TODO add placeholder
    identifier: str = Field("", title="Identifier")
    label: str = Field("", title="Label")
    icon: str = Field("", title="Icon")
    default_variants: list[str] = Field(
        default_factory=list,
        title="Default Variants"
    )
    description: str = Field(
        "",
        title="Description",
        widget="textarea"
    )
    detailed_description: str = Field(
        "",
        title="Detailed Description",
        widget="textarea"
    )
    allow_sequences: bool = Field(
        False,
        title="Allow sequences"
    )
    allow_multiple_items: bool = Field(
        False,
        title="Allow multiple items"
    )
    extensions: list[str] = Field(
        default_factory=list,
        title="Extensions"
    )


DEFAULT_SIMPLE_CREATORS = [
    {
        "family": "workfile",
        "identifier": "",
        "label": "Workfile",
        "icon": "fa.file",
        "default_variants": [
            "Main"
        ],
        "description": "Backup of a working scene",
        "detailed_description": "Workfiles are full scenes from any application that are directly edited by artists. They represent a state of work on a task at a given point and are usually not directly referenced into other scenes.",
        "allow_sequences": False,
        "allow_multiple_items": False,
        "extensions": [
            ".ma",
            ".mb",
            ".nk",
            ".hrox",
            ".hip",
            ".hiplc",
            ".hipnc",
            ".blend",
            ".scn",
            ".tvpp",
            ".comp",
            ".zip",
            ".prproj",
            ".drp",
            ".psd",
            ".psb",
            ".aep"
        ]
    },
    {
        "family": "model",
        "identifier": "",
        "label": "Model",
        "icon": "fa.cubes",
        "default_variants": [
            "Main",
            "Proxy",
            "Sculpt"
        ],
        "description": "Clean models",
        "detailed_description": "Models should only contain geometry data, without any extras like cameras, locators or bones.\n\nKeep in mind that models published from tray publisher are not validated for correctness. ",
        "allow_sequences": False,
        "allow_multiple_items": True,
        "extensions": [
            ".ma",
            ".mb",
            ".obj",
            ".abc",
            ".fbx",
            ".bgeo",
            ".bgeogz",
            ".bgeosc",
            ".usd",
            ".blend"
        ]
    },
    {
        "family": "pointcache",
        "identifier": "",
        "label": "Pointcache",
        "icon": "fa.gears",
        "default_variants": [
            "Main"
        ],
        "description": "Geometry Caches",
        "detailed_description": "Alembic or bgeo cache of animated data",
        "allow_sequences": True,
        "allow_multiple_items": True,
        "extensions": [
            ".abc",
            ".bgeo",
            ".bgeogz",
            ".bgeosc"
        ]
    },
    {
        "family": "plate",
        "identifier": "",
        "label": "Plate",
        "icon": "mdi.camera-image",
        "default_variants": [
            "Main",
            "BG",
            "Animatic",
            "Reference",
            "Offline"
        ],
        "description": "Footage Plates",
        "detailed_description": "Any type of image seqeuence coming from outside of the studio. Usually camera footage, but could also be animatics used for reference.",
        "allow_sequences": True,
        "allow_multiple_items": True,
        "extensions": [
            ".exr",
            ".png",
            ".dpx",
            ".jpg",
            ".tiff",
            ".tif",
            ".mov",
            ".mp4",
            ".avi"
        ]
    },
    {
        "family": "render",
        "identifier": "",
        "label": "Render",
        "icon": "mdi.folder-multiple-image",
        "default_variants": [],
        "description": "Rendered images or video",
        "detailed_description": "Sequence or single file renders",
        "allow_sequences": True,
        "allow_multiple_items": True,
        "extensions": [
            ".exr",
            ".png",
            ".dpx",
            ".jpg",
            ".jpeg",
            ".tiff",
            ".tif",
            ".mov",
            ".mp4",
            ".avi"
        ]
    },
    {
        "family": "camera",
        "identifier": "",
        "label": "Camera",
        "icon": "fa.video-camera",
        "default_variants": [],
        "description": "3d Camera",
        "detailed_description": "Ideally this should be only camera itself with baked animation, however, it can technically also include helper geometry.",
        "allow_sequences": False,
        "allow_multiple_items": True,
        "extensions": [
            ".abc",
            ".ma",
            ".hip",
            ".blend",
            ".fbx",
            ".usd"
        ]
    },
    {
        "family": "image",
        "identifier": "",
        "label": "Image",
        "icon": "fa.image",
        "default_variants": [
            "Reference",
            "Texture",
            "Concept",
            "Background"
        ],
        "description": "Single image",
        "detailed_description": "Any image data can be published as image family. References, textures, concept art, matte paints. This is a fallback 2d family for everything that doesn't fit more specific family.",
        "allow_sequences": False,
        "allow_multiple_items": True,
        "extensions": [
            ".exr",
            ".jpg",
            ".jpeg",
            ".dpx",
            ".bmp",
            ".tif",
            ".tiff",
            ".png",
            ".psb",
            ".psd"
        ]
    },
    {
        "family": "vdb",
        "identifier": "",
        "label": "VDB Volumes",
        "icon": "fa.cloud",
        "default_variants": [],
        "description": "Sparse volumetric data",
        "detailed_description": "Hierarchical data structure for the efficient storage and manipulation of sparse volumetric data discretized on three-dimensional grids",
        "allow_sequences": True,
        "allow_multiple_items": True,
        "extensions": [
            ".vdb"
        ]
    },
    {
        "family": "matchmove",
        "identifier": "",
        "label": "Matchmove",
        "icon": "fa.empire",
        "default_variants": [
            "Camera",
            "Object",
            "Mocap"
        ],
        "description": "Matchmoving script",
        "detailed_description": "Script exported from matchmoving application to be later processed into a tracked camera with additional data",
        "allow_sequences": False,
        "allow_multiple_items": True,
        "extensions": []
    },
    {
        "family": "rig",
        "identifier": "",
        "label": "Rig",
        "icon": "fa.wheelchair",
        "default_variants": [],
        "description": "CG rig file",
        "detailed_description": "CG rigged character or prop. Rig should be clean of any extra data and directly loadable into it's respective application\t",
        "allow_sequences": False,
        "allow_multiple_items": False,
        "extensions": [
            ".ma",
            ".blend",
            ".hip",
            ".hda"
        ]
    },
    {
        "family": "simpleUnrealTexture",
        "identifier": "",
        "label": "Simple UE texture",
        "icon": "fa.image",
        "default_variants": [],
        "description": "Simple Unreal Engine texture",
        "detailed_description": "Texture files with Unreal Engine naming conventions",
        "allow_sequences": False,
        "allow_multiple_items": True,
        "extensions": []
    }
]
