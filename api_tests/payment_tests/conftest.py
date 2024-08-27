import pytest

from api_tests.conftest import email, password
from config.config import Configuration
from services.authorization.authorization_api_service import AuthorizationService
from services.authorization.models.authorization_model.login_dto import LoginDto
from services.payment.payment_service import PaymentService
from utilities.api_utilities import ApiUtilities


@pytest.fixture(scope="session", autouse=False)
def payment_api_service():
    anonymous_api_utils = ApiUtilities(Configuration.PAYMENT_SERVICE_URL)
    api_service = PaymentService(anonymous_api_utils)
    yield api_service


@pytest.fixture(scope="session", autouse=False)
def super_admin_payment_api_service(auth_api_utilities):
    auth_service = AuthorizationService(api_utils=auth_api_utilities)
    login_dto = LoginDto(email=email, password=password)
    login_response = auth_service.login_user(login_dto)

    api_utils_super_admin = ApiUtilities(Configuration.PAYMENT_SERVICE_URL, headers={
        "Authorization": f"Bearer {login_response.access_token}"})

    api_service = PaymentService(api_utils_super_admin)
    yield api_service
