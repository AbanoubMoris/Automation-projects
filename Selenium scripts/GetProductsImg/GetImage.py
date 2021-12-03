from time import sleep

from selenium import webdriver
import os
import GetProductsImg.Constant as const

class ImageUrl(webdriver.Chrome):

    def __init__(self, driver_path="chromedriver.exe",teardown=False):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.teardown=teardown
        super().__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.Base_URL)

    def fetch_image_urls(self,query: str, max_links_to_fetch: int):
        def scroll_to_end(wd):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)

            # build the google query

        search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

        # load the page
        self.get(search_url.format(q=query))

        image_urls = set()
        image_count = 0
        results_start = 0
        while image_count < max_links_to_fetch:
            # get all image thumbnail results
            thumbnail_results = self.find_elements_by_css_selector("img.Q4LuWd")
            number_results = len(thumbnail_results)

            print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

            for img in thumbnail_results[results_start:number_results]:
                # try to click every thumbnail such that we can get the real image behind it
                try:
                    img.click()
                    sleep(.6)
                except Exception:
                    continue

                # extract image urls
                actual_images = self.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in actual_images:
                    url=actual_image.get_attribute('src')
                    if not url.endswith(('.png', '.jpg', '.jpeg')):
                        continue
                    if actual_image.get_attribute('src') and 'http' in url:
                        image_urls.add(url)

                image_count = len(image_urls)

                if len(image_urls) >= max_links_to_fetch:
                    print(f"Found: {len(image_urls)} image links, done!")
                    break
            else:
                print("Found:", len(image_urls), "image links, looking for more ...")
                sleep(30)
                return
                load_more_button = self.find_element_by_css_selector(".mye4qd")
                if load_more_button:
                    self.execute_script("document.querySelector('.mye4qd').click();")

            results_start = len(thumbnail_results)
            #scroll_to_end(self)

        return image_urls