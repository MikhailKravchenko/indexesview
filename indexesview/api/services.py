import asyncio
import json
import re
import aiohttp as aiohttp

from urlextract import URLExtract

from .models import Price


class GetCoingeckoIndexes:

    @staticmethod
    async def get_indexes(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                headers = resp.headers
                insexes = await resp.text()
        return insexes, headers


# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

extractor = URLExtract()




class GetIndexes:
    def __init__(self):
        self.max_number_page = None
        self._price = []

    def parse_index(self, url, last_time):
        if last_time:
            indexes, headers = asyncio.run(
                GetCoingeckoIndexes().get_indexes(url))
            json_indexes = json.loads(indexes)
            self._price.append(json_indexes)
            return
        else:
            indexes, headers = asyncio.run(
                GetCoingeckoIndexes().get_indexes(url))
            json_indexes = json.loads(indexes)
            self._price.append(json_indexes)
            try:
                urls = extractor.find_urls(headers['Link'])
            except KeyError:
                return

            nums = re.findall(r'\d+', urls[-1])
            b = urls[-1]
            if int(nums[1]) != self.max_number_page:
                self.parse_index(urls[-1], False)
            else:
                self.parse_index(urls[-1], True)
                return

    def get_max_number_page(self, url):

        indexes, headers = asyncio.run(GetCoingeckoIndexes().get_indexes(url))
        urls = extractor.find_urls(headers['Link'])
        nums = re.findall(r'\d+', urls[0])
        self.max_number_page = int(nums[1])
    def get_ptice(self):
        return self._price


class ParsePrice:
    def __init__(self, price):
        self.price = price
    def parse_price_and_write_to_db(self):


        for list_price in self.price:
            for detail in list_price:
                if detail['last'] is not None:
                    updated_values = {'price': float(detail['last'])}

                    obj, created = Price.objects.update_or_create(
                        market=detail['market'], name_coin=detail['id'],
                        defaults=updated_values
                    )