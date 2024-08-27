class Configuration:
    URL_TEMPLATE = "https://{}.dev-cinescope.store/"

    MOVIE_SERVICE_URL = URL_TEMPLATE.format('api')
    AUTH_SERVICE_URL = URL_TEMPLATE.format('auth')
    PAYMENT_SERVICE_URL = URL_TEMPLATE.format('payment')
