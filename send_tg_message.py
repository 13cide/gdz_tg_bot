
import config
import requests


def send_tg(file):
    requests.get(f'https://api.telegram.org/bot{config.tg_token}/sendMessage?chat_id={config.chat_id}&text={file}')
    pdf = {'document': open(f"pdf/{file}.pdf", 'rb')}
    requests.post(f'https://api.telegram.org/bot{config.tg_token}/sendDocument?chat_id={config.chat_id}', files=pdf)
    files = {'document': open(f"zip/{file}.zip", 'rb')}
    requests.post(f'https://api.telegram.org/bot{config.tg_token}/sendDocument?chat_id={config.chat_id}', files=files)
