from pydantic import Field

from openpype.settings import BaseSettingsModel

class ListPerPlatform(BaseSettingsModel):
    windows: list[str] = Field(default_factory=list)
    linux: list[str] = Field(default_factory=list)
    darwin: list[str] = Field(default_factory=list)


class GoogleDriveSubmodel(BaseSettingsModel):
    """Specific settings for Google Drive sites.

    credentials_url: .json file for service account which must have access
        to shared GDrive folder/drive
    root: root folder on GDrive, `/My Drive` prefix is required for classic
        GDrive, shared disks don't need that
    """
    _layout = "compact"
    credentials_url: ListPerPlatform = Field(
        title="Credentials url",
        default_factory=ListPerPlatform,
        description="""Path to credentials .json available on shared disk."""
    )

    root: str = Field(
        "",
        title="Roots",
        description="Root folder on Google Drive",
    )
