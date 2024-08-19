# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2024-08-19T03:45:20+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, EmailStr, Field


class ArtifactUrls(BaseModel):
    small: Optional[str] = Field(None, title="Small")
    large: str = Field(..., title="Large")


class AuthResponse(BaseModel):
    api_key: str = Field(..., title="Api Key")


class BodySetUrdfUrdfUploadListingIdPost(BaseModel):
    file: bytes = Field(..., title="File")


class BodyUploadArtifactsUploadListingIdPost(BaseModel):
    files: List[bytes] = Field(..., title="Files")


class ClientIdResponse(BaseModel):
    client_id: str = Field(..., title="Client Id")


class DeleteTokenResponse(BaseModel):
    message: str = Field(..., title="Message")


class EmailSignUpRequest(BaseModel):
    email: EmailStr = Field(..., title="Email")


class EmailSignUpResponse(BaseModel):
    message: str = Field(..., title="Message")


class GetListingResponse(BaseModel):
    id: str = Field(..., title="Id")
    name: str = Field(..., title="Name")
    description: Optional[str] = Field(..., title="Description")
    child_ids: List[str] = Field(..., title="Child Ids")
    tags: List[str] = Field(..., title="Tags")
    can_edit: bool = Field(..., title="Can Edit")


class GetTokenResponse(BaseModel):
    id: str = Field(..., title="Id")
    email: str = Field(..., title="Email")


class GithubAuthRequest(BaseModel):
    code: str = Field(..., title="Code")


class GithubAuthResponse(BaseModel):
    api_key: str = Field(..., title="Api Key")


class GoogleLogin(BaseModel):
    token: str = Field(..., title="Token")


class ArtifactType(Enum):
    image = "image"


class ArtifactType1(Enum):
    urdf = "urdf"
    mjcf = "mjcf"


class ArtifactType2(Enum):
    stl = "stl"
    obj = "obj"
    dae = "dae"
    ply = "ply"


class ArtifactType3(Enum):
    tgz = "tgz"
    zip = "zip"


class ListArtifactsItem(BaseModel):
    artifact_id: str = Field(..., title="Artifact Id")
    listing_id: str = Field(..., title="Listing Id")
    name: str = Field(..., title="Name")
    artifact_type: Union[ArtifactType, ArtifactType1, ArtifactType2, ArtifactType3] = Field(..., title="Artifact Type")
    description: Optional[str] = Field(..., title="Description")
    timestamp: int = Field(..., title="Timestamp")
    urls: ArtifactUrls
    is_new: Optional[bool] = Field(None, title="Is New")


class ListArtifactsResponse(BaseModel):
    artifacts: List[ListArtifactsItem] = Field(..., title="Artifacts")


class ListListingsResponse(BaseModel):
    listing_ids: List[str] = Field(..., title="Listing Ids")
    has_next: Optional[bool] = Field(False, title="Has Next")


class Listing(BaseModel):
    id: str = Field(..., title="Id")
    user_id: str = Field(..., title="User Id")
    name: str = Field(..., title="Name")
    child_ids: List[str] = Field(..., title="Child Ids")
    description: Optional[str] = Field(..., title="Description")


class ListingInfoResponse(BaseModel):
    id: str = Field(..., title="Id")
    name: str = Field(..., title="Name")
    description: Optional[str] = Field(..., title="Description")
    child_ids: List[str] = Field(..., title="Child Ids")
    image_url: Optional[str] = Field(..., title="Image Url")


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., title="Email")
    password: str = Field(..., title="Password")


class LoginResponse(BaseModel):
    user_id: str = Field(..., title="User Id")
    token: str = Field(..., title="Token")


class Permission(Enum):
    is_admin = "is_admin"


class MyUserInfoResponse(BaseModel):
    user_id: str = Field(..., title="User Id")
    email: str = Field(..., title="Email")
    github_id: Optional[str] = Field(..., title="Github Id")
    google_id: Optional[str] = Field(..., title="Google Id")
    permissions: Optional[List[Permission]] = Field(..., title="Permissions")


class NewListingRequest(BaseModel):
    name: str = Field(..., title="Name")
    child_ids: List[str] = Field(..., title="Child Ids")
    description: Optional[str] = Field(..., title="Description")


class NewListingResponse(BaseModel):
    listing_id: str = Field(..., title="Listing Id")


class PublicUserInfoResponseItem(BaseModel):
    id: str = Field(..., title="Id")
    email: str = Field(..., title="Email")
    permissions: Optional[List[Permission]] = Field(None, title="Permissions")
    created_at: Optional[int] = Field(None, title="Created At")
    updated_at: Optional[int] = Field(None, title="Updated At")
    first_name: Optional[str] = Field(None, title="First Name")
    last_name: Optional[str] = Field(None, title="Last Name")
    name: Optional[str] = Field(None, title="Name")
    bio: Optional[str] = Field(None, title="Bio")


class PublicUsersInfoResponse(BaseModel):
    users: List[PublicUserInfoResponseItem] = Field(..., title="Users")


class UpdateArtifactRequest(BaseModel):
    name: Optional[str] = Field(None, title="Name")
    description: Optional[str] = Field(None, title="Description")


class UpdateListingRequest(BaseModel):
    name: Optional[str] = Field(None, title="Name")
    child_ids: Optional[List[str]] = Field(None, title="Child Ids")
    description: Optional[str] = Field(None, title="Description")
    tags: Optional[List[str]] = Field(None, title="Tags")


class UploadArtifactResponse(BaseModel):
    artifacts: List[ListArtifactsItem] = Field(..., title="Artifacts")


class UrdfInfo(BaseModel):
    artifact_id: str = Field(..., title="Artifact Id")
    url: str = Field(..., title="Url")


class UrdfResponse(BaseModel):
    urdf: Optional[UrdfInfo]
    listing_id: str = Field(..., title="Listing Id")


class UserInfoResponseItem(BaseModel):
    id: str = Field(..., title="Id")
    email: str = Field(..., title="Email")


class UserPublic(BaseModel):
    id: str = Field(..., title="Id")
    email: str = Field(..., title="Email")
    permissions: Optional[List[Permission]] = Field(None, title="Permissions")
    created_at: Optional[int] = Field(None, title="Created At")
    updated_at: Optional[int] = Field(None, title="Updated At")
    first_name: Optional[str] = Field(None, title="First Name")
    last_name: Optional[str] = Field(None, title="Last Name")
    name: Optional[str] = Field(None, title="Name")
    bio: Optional[str] = Field(None, title="Bio")


class UserSignup(BaseModel):
    signup_token_id: str = Field(..., title="Signup Token Id")
    email: str = Field(..., title="Email")
    password: str = Field(..., title="Password")


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class DumpListingsResponse(BaseModel):
    listings: List[Listing] = Field(..., title="Listings")


class GetBatchListingsResponse(BaseModel):
    listings: List[ListingInfoResponse] = Field(..., title="Listings")


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title="Detail")
