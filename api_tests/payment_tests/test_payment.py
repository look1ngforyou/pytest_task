import random
from test_data.test_data import TestData
from logger.logger import Logger
import pytest
from faker import Faker
from services.authorization.models.authorization_model.login_dto import LoginDto
from services.payment.payment_model.card_dto import CardDto
from services.payment.payment_model.create_payment_dto import CreatePaymentDto

faker = Faker()


class TestPayment:
    PAYMENT_AMOUNT_VALUE = random.randint(1,11)

    @pytest.mark.parametrize("payment_amount", ([PAYMENT_AMOUNT_VALUE]))
    def test_register_user_create_movie_payment_implementation(self, payment_amount, auth_api_service,
                                                               payment_api_service,
                                                               super_admin_payment_api_service, register_user,
                                                               create_new_movie):
        Logger.info(" !!! Step 1 - Register new user")
        registered_user_info = register_user

        password = registered_user_info.password
        email = registered_user_info.email

        Logger.info(" !!! Step 2 - Log in as new user")
        auth_api_service.update_api_utils(token=None)
        login_dto = LoginDto(email=email, password=password)
        login_response = auth_api_service.login_user(login_dto=login_dto)
        payment_api_service.update_api_utils(token=login_response.access_token)

        Logger.info(f" !!! Step 3 - Create and pay for {payment_amount} movies")
        for i in range(1, payment_amount + 1):
            Logger.debug(f"Create {i} film")

            created_movie = create_new_movie()

            Logger.debug(f"Pay for a {i} movie")
            card_dto = CardDto(card_number=TestData.VALID_CARD_NUMBER,
                               card_holder=faker.first_name() + " " + faker.last_name(),
                               expiration_date=TestData.VALID_EXPIRATION_DATE,
                               security_code=TestData.VALID_CVV
                               )
            create_payment_dto = CreatePaymentDto(movie_id=created_movie.id,
                                                  amount=random.randint(1, 10),
                                                  card=card_dto)
            payment_api_service.post_create(create_payment_dto)

        Logger.info(" !!! Step 4 - Get the payment total amount")
        total_amount_of_payments = super_admin_payment_api_service.get_user_id(login_response.user.id)

        assert len(total_amount_of_payments) == payment_amount, \
            f"The total number of payments {total_amount_of_payments} does not match the expected {payment_amount}"
