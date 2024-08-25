from uuid import UUID
from services.authorization.helpers.authorization_helper import AuthorizationHelper
from services.authorization.helpers.user_helper import UserHelper
from services.authorization.models.user_model.edit_user_dto import EditUserDto
from services.authorization.models.user_model.editing_user_real_response import EditingUserRealResponse
from services.authorization.models.authorization_model.login_dto import LoginDto
from services.authorization.models.authorization_model.login_response import LoginResponse
from services.authorization.models.user_model.user_response import UserResponse
from utilities.api_utilities import ApiUtilities
from services.authorization.models.authorization_model.register_dto import RegisterDto


class AuthorizationService:
    def __init__(self, api_utils: ApiUtilities):
        self.api_utils = api_utils
        self.user_helper = UserHelper(api_utils)
        self.authorization_helper = AuthorizationHelper(api_utils)

    def update_api_utils(self, token: str or None):
        self.api_utils.update_headers(headers={"Authorization": f"Bearer {token}"})

    def login_user(self, login_dto: LoginDto) -> LoginResponse:
        response = self.authorization_helper.post_login_user(
            json=login_dto.model_dump(by_alias=True, exclude_defaults=True))
        return LoginResponse(**response.json())

    def register_user(self, register_dto: RegisterDto) -> UserResponse:
        response = self.authorization_helper.post_register_user(
            json=register_dto.model_dump(by_alias=True, exclude_defaults=True))
        return UserResponse(**response.json())

    def delete_user(self, user_id: UUID):
        response = self.user_helper.delete_user(user_id=user_id)
        return response

    def patch_user(self, user_id: UUID, edit_user_dto: EditUserDto) -> EditingUserRealResponse:
        response = self.user_helper.patch_user(user_id=user_id, json=edit_user_dto.model_dump())
        return EditingUserRealResponse(**response.json())
