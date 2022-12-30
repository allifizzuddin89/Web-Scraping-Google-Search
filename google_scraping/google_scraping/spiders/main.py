import scrapy
import logging
from scrapy.utils.log import configure_logging
import pandas as pd
from scrapy.shell import inspect_response

class MainSpider(scrapy.Spider):
    name = 'main'
    headers = {
        "authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
        "cache-control": "max-age=0",
        "dnt": "1",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Microsoft Edge\";v=\"108\"",
        "sec-ch-ua-arch": "\"x86\"",
        "sec-ch-ua-bitness": "\"64\"",
        "sec-ch-ua-full-version": "\"108.0.1462.54\"",
        "sec-ch-ua-full-version-list": "\"Not?A_Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"108.0.5359.125\", \"Microsoft Edge\";v=\"108.0.1462.54\"",
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
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
    }


    cookies = {
        "OTZ": "6832252_24_24__24_",
        "AEC": "AakniGNR38W5GS2VIc05EmBUGtXVm5BMh2Sxjd_sdxjBvv9pYDK_ZG6FRA",
        "1P_JAR": "2022-12-30-02",
        "SID": "SQjSAFSeR3m3sRvgZf329pgx1XVt9urKFakvoIJDE2fsyPS_bNKt7-lfZYBSOGd94PhN7Q.",
        "__Secure-1PSID": "SQjSAFSeR3m3sRvgZf329pgx1XVt9urKFakvoIJDE2fsyPS_veqiiUIXALEzGQui6X1W8w.",
        "__Secure-3PSID": "SQjSAFSeR3m3sRvgZf329pgx1XVt9urKFakvoIJDE2fsyPS_OcGJNKj5KSZ1blqa4PZQLw.",
        "HSID": "Anj06PpVz82PfZuPa",
        "SSID": "Aw-AwyKkCqINq2Bjw",
        "APISID": "zFK_bzM0aYWXsks3/Aep-ycl9fTywmW-Q4",
        "SAPISID": "JNg7BJpEmmN1pxYi/Ar0X1QTYpgIf8vLiL",
        "__Secure-1PAPISID": "JNg7BJpEmmN1pxYi/Ar0X1QTYpgIf8vLiL",
        "__Secure-3PAPISID": "JNg7BJpEmmN1pxYi/Ar0X1QTYpgIf8vLiL",
        "NID": "511=OBirSfPwvj-8lEiiQ5ORjBAM1MW_lip8E8F6BQpdFrbbcrakoq_bGK98LjLE9fVj2ev8NDkvVcg1ujTnpxy5jmXoLQYINZu2Hmb4R2xuCWOhLlP9dp6Vc3LHuZIJs7wY0CLVNvsqUmDfNg7tgp7q6_T3bfNX3cox5ZVUpxZ75_vsWHgwUKnGKylloHDMm1dqZ_sncj22qCW1K_kZSFh16ovF9KAk-55ATlsoWbcO1u_L5APogHf24XBEH1ENHurq-HGgL365Ja8vnGo_N84vMA4J9yABSLTZpmYarO1dSi9hLlgyNH2j9RR6XfMM-Q3ShoKIqYQ",
        "DV": "Aym1vW5bUUFYIBqkWuyFV2m6_mQPVhgvSfGgakooqQAAAEDoe9uMnBRHXAAAAOBRX6N8aZALYQAAAJBSG8TWjNqJGAAAAA",
        "UULE": "a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjcyMzY5MDM2NTM5MDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDI5NzUwMTIwCiAgbG9uZ2l0dWRlX2U3OiAxMDE1NzU0NzEwCn0KcmFkaXVzOiA3MTkyMApwcm92ZW5hbmNlOiA2Cg==",
        "SIDCC": "AIKkIs1tEoZbPqFLQbSSUjRxxC2EhgqXnnw26OoX9lgUEW8p850iFSCWM_mLfwAmbutW7L1Z-LM",
        "__Secure-1PSIDCC": "AIKkIs3XxBCDMBEF3YW6Z-eENFoxcsZqBMjXrwAGWMN5RJumV5y9HM82rdlnjXya7CnmjO2ddA",
        "__Secure-3PSIDCC": "AIKkIs2O_nDwhb8sVcxqCKhR_mXD0GFOQWtPwas1XwXvcEA-jpJIR62HmdBusYXKwSxzt2Zm-vQ"
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
        inspect_response(response, self)
        # item1 = response.css('div.MjjYud')
        # item2 = response.css('div.hlcw0c')
        # item3 = response.css('div.ULSxyf')
        # items = []
        # while items in item1 or items in item2 or items in item3:
        #     item = {
        #         'Title' : items.css('h3.LC20lb.MBeuO.DKV0Md::text').get(),
        #         'Link' : items.css('div.div.yuRUbf>a::attr(href)').get(),
        #         'Description' : items.css('div.VwiC3b>span::text').get(),
        #         'Tags' : items.css('div.HiHjCd>a[href]::text').getall(),
        #     }
        #     yield item

