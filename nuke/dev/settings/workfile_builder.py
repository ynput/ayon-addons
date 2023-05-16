from pydantic import Field
from ayon_server.settings import (
    BaseSettingsModel,
    task_types_enum,
    MultiplatformPathModel,
)


class CustomTemplateModel(BaseSettingsModel):
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    path: MultiplatformPathModel = Field(
        default_factory=MultiplatformPathModel,
        title="Gizmo Directory Path"
    )


class BuilderProfileItemModel(BaseSettingsModel):
    subset_name_filters: list[str] = Field(
        default_factory=list,
        title="Subset name"
    )
    families: list[str] = Field(
        default_factory=list,
        title="Families"
    )
    repre_names: list[str] = Field(
        default_factory=list,
        title="Representations"
    )
    loaders: list[str] = Field(
        default_factory=list,
        title="Loader plugins"
    )


class BuilderProfileModel(BaseSettingsModel):
    task_types: list[str] = Field(
        default_factory=list,
        title="Task types",
        enum_resolver=task_types_enum
    )
    tasks: list[str] = Field(
        default_factory=list,
        title="Task names"
    )
    current_context: list[BuilderProfileItemModel] = Field(
        title="Current context")
    linked_assets: list[BuilderProfileItemModel] = Field(
        title="Linked assets/shots")


class WorkfileBuilderModel(BaseSettingsModel):
    create_first_version: bool = Field(
        title="Create first workfile")
    custom_templates: list[CustomTemplateModel] = Field(
        title="Custom templates")
    builder_on_start: bool = Field(
        title="Run Builder at first workfile")
    profiles: list[BuilderProfileModel] = Field(
        title="Builder profiles")


DEFAULT_WORKFILE_BUILDER_SETTINGS = {
    "create_first_version": False,
    "custom_templates": [],
    "builder_on_start": False,
    "profiles": []
}
