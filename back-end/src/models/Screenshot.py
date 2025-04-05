from pyppeteer import launch
import uuid
import os
class Screenshot:

    def __init__(self, link):
        self.link = link


    @staticmethod
    def generate_hex(extension='jpg'):
        unique_id = uuid.uuid4().hex
        return f"{unique_id}.{extension}"


    async def capture(self):
       
        browser = await launch(
            executablePath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            headless=True,)

        page = await browser.newPage()

        await page.setViewport({'width': 1280, 'height': 720})

        try:
            response = await page.goto(self.link,{'timeout':20000})

            if response.status != 200:
                return {'error': 'Erro ao acessar a página'}

            
            
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
            static_img_path = os.path.join(base_dir, 'static', 'img')  

        
            new_hex = self.generate_hex()
            path = os.path.join(static_img_path, new_hex)


            await page.screenshot({
                'path': path ,
                'fullPage': False
            })

            return {'success': new_hex}

        except Exception as e:
            return {'error': f"Erro ao acessar a página: {e}"}

        finally:
            await browser.close()






