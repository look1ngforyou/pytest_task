import pytest
from faker import Faker
from logger.logger import Logger
from services.authorization.models.user_model.edit_user_dto import EditUserDto

faker = Faker()


class TestChangeUserData:
    @pytest.mark.parametrize("verified, banned", [(False, True)])
    def test_register_user_change_user_data(self, verified, banned, auth_api_service,
                                            register_user):
        Logger.info(" !!! Step 1 - Register new user")
        registered_user = register_user

        Logger.info(" !!! Step 2 - Change the newly created user data")
        edit_user_dto = EditUserDto(roles=registered_user.user.roles, verified=verified, banned=banned)
        editing_response = auth_api_service.patch_user(user_id=registered_user.user.id,
                                                       edit_user_dto=edit_user_dto)
        assert editing_response.banned is banned, \
            f"Expected field banned: {banned} for new created user, got banned: {editing_response.banned} instead"

        assert editing_response.verified is verified, \
            f"Expected verified: {verified} for new created user, got verified: {editing_response.verified} instead"
