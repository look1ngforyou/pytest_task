from typing import List
import json


class TestUtils:
    @staticmethod
    def parse_config(file_path='config.json'):
        with open(file_path) as config_file:
            config = json.load(config_file)
        return config

    @staticmethod
    def sorting_prices(price_texts: List, range_num: int) -> List:
        prices_list = []
        for i in range(min(range_num, len(price_texts))):
            price_text = price_texts[i].strip()

            if price_text.lower() in ['free  to play', 'free', 'бесплатно']:
                continue
            if price_text.lower().startswith('your price:') or price_text.lower().startswith('цена для вас:'):
                price_text = price_text.split(':', 1)[-1].strip()

            price = price_text[:-1].replace(',', '.')
            final_price = float(price)
            prices_list.append(final_price)

        return prices_list
