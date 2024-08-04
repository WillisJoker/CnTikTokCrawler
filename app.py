import pprint
import requests
import re
from urllib.parse import unquote
import json

def GetResponse(url):
    headers = {
        'Cookie': 'douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; __ac_nonce=066af2de400a74afd4205; __ac_signature=_02B4Z6wo00f01cwSXOQAAIDD1rfQURdUnP3MMlhAABWtda; ttwid=1%7C2hoe3GpRIT_juj3pqcuD-8ZWDj1L0BDMJSUZImvmFJs%7C1722756580%7C4f36f72a666c3eeda274dbe0ff9b6329536c2ebe166cf49c70154154198085c8; UIFID_TEMP=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b0d757658c254468182be97f962f921203dcb16c9abcf9bb893a0f3c37fd69ab47cdf8eb195e91fe7f36ae0f4ec0f56413; s_v_web_id=verify_lzf8sepv_J8PKQFAe_vcAf_4tB7_AKAo_hKA9qmx4NbWm; dy_swidth=1536; dy_sheight=864; csrf_session_id=630d5a78add6ddf83d380b32f52f4456; fpk1=U2FsdGVkX1+5+UD2Lq2Ck9itOiE2gi8FZdUr7y/npUhgufu9stidH+EmBoa1SUyBhbGBq+BjAOXGFPXwxOdpvg==; fpk2=362d7fe3d8b2581bffa359f0eeda7106; strategyABtestKey=%221722756584.316%22; UIFID=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b0d757658c254468182be97f962f92120392bbf4c94272496f4558d71ce117b5e77053403d8b6a18e1ffd33b93524895b2501919b145a16b4b057adc3e3bd04bd9e125979df55fdec80fb11e5cf7fc735c9bbfaee7cb4178b9de09a54597816690fe2e820c2e67ae4e6496827b69789eb47dee5c831eb896b00033f0807521c394; passport_csrf_token=ea8fedb698578444b99fcd913371629f; passport_csrf_token_default=ea8fedb698578444b99fcd913371629f; bd_ticket_guard_client_web_domain=2; WallpaperGuide=%7B%22showTime%22%3A1722756962009%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A12%2C%22cursor2%22%3A0%7D; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; odin_tt=164451b35c98f0eb14d67a6451d173346b1d14e177a8874c21ff74c720bf80e290eace64d3c730e62128cc35d1e5230ccc30371f3810413a3b9f0e52b96cdc2a7225819f8979e84469b4345659b0a471; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; download_guide=%223%2F20240804%2F0%22; home_can_add_dy_2_desktop=%221%22; biz_trace_id=d9663cb2; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRGVCaWtQeEVFYUQyV2xPWmtvaFd3TU1tMXZOSXJBTFRESGlyVk9wckZnb1dKcWZQK1hGYUJZNEgwREZqN08rZ2orVXdFdGowSitkM1I4OGRVS2h3SUE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; IsDouyinActive=false',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    return response

def GetVideo():
    url = 'https://www.douyin.com/user/MS4wLjABAAAAaPBWqW4O1Tj5bnUDMXjujRcROo9JumzAIWkH1XkxiDA?modal_id=7378113158986157331&showTab=post'
    html = GetResponse(url = url).text
    info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', html)[0]
    json_data = json.loads(unquote(info))
    video_url = 'https:' + json_data['app']['videoDetail']['video']['bitRateList'][0]['playAddr'][0]['src']
    return video_url

def Save(title, video_url):
    video_content = GetResponse(url = video_url).content
    with open('E:/video/' + title + '.mp4', mode = 'wb') as f:
        f.write(video_content)


if __name__ == '__main__':
    video_url = GetVideo()
    Save(title='video', video_url=video_url)