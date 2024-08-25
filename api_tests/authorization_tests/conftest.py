import pytest
from config.config import Configuration
from services.authorization.authorization_api_service import AuthorizationService
from services.authorization.models.authorization_model.login_dto import LoginDto
from api_tests.conftest import email, password
from utilities.api_utilities import ApiUtilities



