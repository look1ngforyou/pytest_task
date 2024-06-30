from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def sorting_prices(driver, wait, range_num, formatting_price_template):
    prices_list = []
    for i in range(1, range_num + 1):
        dynamic_xpath = formatting_price_template.format(i)
        dynamic_price_xpath = (By.XPATH, dynamic_xpath)

        try:
            game_price_element = wait.until(ec.visibility_of_element_located(dynamic_price_xpath))
            price_text = game_price_element.text.strip()

            if price_text.lower() in ['free to play', 'free', 'бесплатно']:
                continue
            if price_text.lower().startswith('your price:') or price_text.lower().startswith('цена для вас:'):
                price_text = price_text.split(':', 1)[-1].strip()

            price = price_text[:-1].replace(',', '.')
            final_price = float(price)
            prices_list.append(final_price)

        except TimeoutException:
            continue
    return prices_list
