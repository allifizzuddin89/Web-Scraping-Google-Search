import scrapy
import logging
from scrapy.utils.log import configure_logging
import pandas as pd

class MainSpider(scrapy.Spider):
    name = 'main'
    headers = {
        "authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-arch": "\"x86\"",
        "sec-ch-ua-bitness": "\"64\"",
        "sec-ch-ua-full-version": "\"107.0.1418.62\"",
        "sec-ch-ua-full-version-list": "\"Microsoft Edge\";v=\"107.0.1418.62\", \"Chromium\";v=\"107.0.5304.150\", \"Not=A?Brand\";v=\"24.0.0.0\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "\"\"",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-ch-ua-platform-version": "\"5.4.0\"",
        "sec-ch-ua-wow64": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
    }

    cookies = {
        "OTZ": "6758128_24_24__24_",
        "SID": "RAjSALvA_Uqn4wkMXl_bNHlgrQTU1UHV4vMns_lWPLUSpLCq2BrzSDz3mUuVOeSl2vUBlg.",
        "__Secure-1PSID": "RAjSALvA_Uqn4wkMXl_bNHlgrQTU1UHV4vMns_lWPLUSpLCqrp4fL9ds9pJaerSEkwo37A.",
        "__Secure-3PSID": "RAjSALvA_Uqn4wkMXl_bNHlgrQTU1UHV4vMns_lWPLUSpLCq6ygAkaSyot5KnW0udFQKbg.",
        "HSID": "AS9A4hDQZcERNbhPL",
        "SSID": "A2i-BN379ZZlFz6tH",
        "APISID": "NEtuYds3pSZAptTX/AFvTajtoSAd_0BH_X",
        "SAPISID": "vNbHiIOSWrjRAayB/A1Mh9ubacBMQzpnE-",
        "__Secure-1PAPISID": "vNbHiIOSWrjRAayB/A1Mh9ubacBMQzpnE-",
        "__Secure-3PAPISID": "vNbHiIOSWrjRAayB/A1Mh9ubacBMQzpnE-",
        "AEC": "AakniGMvjJqNfMo8zAvN_PjbZk0LVhMUM5rKKrd-xO3IPrLZ59DvhJihVA",
        "NID": "511=g4WqXbWPbwgEk83BEhP_XZJQAedrglsk8IrcGxsuf0S1pziWHVcoCcLpXN5AzGSZUVUyjc8kMSF4u887QXuSyd0BWSh6INTVRFXJ5S_or-VpWh5a-MarBZ8wtGmN6Z657ie8SMmbSP1nt2AuQhXtyiAlFdjrnQdqB5g7zHcBIMfgDcin4CcFrD1EvXUM61MQkz15fT1XH9caxPbIeFCdwW-PWJtPQFW4yoQEZhJt-M045snEmkMHMPNW3CIwPKonopntpV7IwVbukFxOS9s9tXegcgBtXzCpwyL1TWEWTmd8lUWp0wK4j98UFWaVRZU7IpgVAn68YEOY93rKT0cFh_SMIXPXnPzIEmcLt98cpIlQ3S3mHOrzCxxbQmeCaZsIXsJ2ZRe3W-L-xdv9uCdPBTBZKqe_f8lD-4wZ0D-SB_RicJyLEu2m078ZvZg",
        "1P_JAR": "2022-12-01-08",
        "DV": "Aym1vW5bUUFYACm1QWzNqJ24pJ_MTBih720zclIcMQAAAMBLUjyomhJKOgAAAOBRX6N8aZALLQAAAKJBqsVeeJWmEQAAAA",
        "SIDCC": "AIKkIs2owS-_afL-jdOo3XIdMZ--dT-HVyWqTww4pgGWH18-9I8JocGyAI58YYOk8Ad1c5JhmA",
        "__Secure-1PSIDCC": "AIKkIs1PjJbz54JPdB9hDx4_baLJ2VIULltMQKLXKg6qmY5wJa4_5qpBdyKzFBJ_2CdRx5hPSw",
        "__Secure-3PSIDCC": "AIKkIs2bjsGaatUNFUnqZmjghSKNKa-XgiOoN78cI132u0ZGcYDNOvQi-s5RlL7sj3FEqMKA8g"
    }

    configure_logging(
        install_root_handler=False
    )
    logging.basicConfig(
        filename="Logfile1.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode='w',
        level=logging.DEBUG,
    )

    def start_requests(self):
        url = 'https://www.google.com/search?q=dimensity+8100+mobile+phone+list&sxsrf=ALiCzsZnVzp8OGPeInvJMcB118Yb9HJJsg%3A1669455894842&ei=FuCBY7aBM9i03LUP_tWh0A0&ved=0ahUKEwi25NHsx8v7AhVYGrcAHf5qCNoQ4dUDCA8&uact=5&oq=dimensity+8100+mobile+phone+list&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEOgoIABBHENYEELADOgYIABAWEB46BQgAEIYDOgUIIRCgAToHCCEQoAEQCkoECEEYAEoECEYYAFCGM1jwN2CGOWgBcAF4AIABqQGIAaUFkgEDMC41mAEAoAEByAEIwAEB&sclient=gws-wiz-serp'
        # yield scrapy.Request(self.start_urls[0], headers=self.headers, cookies=self.cookies, callback=self.parse_item)
        yield scrapy.Request(url=url, headers=self.headers, cookies=self.cookies, callback=self.parse_item)

    def parse_item(self, response):
        # df = pd.DataFrame()
        # link = []
        # tags = []
        # link.append(response.url)
        # df['Link'] = link
        # df['tags'] = tags
        # print('\n')
        # print(response.text)
        # print('\n')
        # inspect_response(response, self)
        item1 = response.css('div.MjjYud')
        item2 = response.css('div.hlcw0c')
        item3 = response.css('div.ULSxyf')
        items = []
        while items in item1 or items in item2 or items in item3:
            item = {
                'Title' : response.css('div.LC20lb.MBeuO.DKV0Md::text').get(),
                'Link' : response.css('div.div.yuRUbf>a::attr(href)').get(),
                'Description' : response.css('div.VwiC3b>span::text').get(),
                'Tags' : response.css('div.HiHjCd>a[href]::text').getall(),
            }
            yield item
