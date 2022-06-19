import re
import requests
import os
from lxml import etree

ffmpeg = 'D:/tools/ffmpeg/bin/ffmpeg.exe'
bvNumList = []
layer_num = 0
url_file = open('video_url.txt', 'w')


def video_download_test():
    url_30077 = 'https://cn-tj-fx-bcache-02.bilivideo.com/upgcxcode/37/49/719694937/719694937-1-30077.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1652628796&gen=playurlv2&os=bcache&oi=3396406601&trid=00007d20ebfdab844fd59da2ff19485a39adu&platform=pc&upsig=4687445dd806020bd25bfe0e5c152e38&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=69902&mid=142330377&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=37367&logo=80000000'
    url_30280 = 'https://cn-tj-fx-bcache-02.bilivideo.com/upgcxcode/37/49/719694937/719694937_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1652628796&gen=playurlv2&os=bcache&oi=3396406601&trid=00007d20ebfdab844fd59da2ff19485a39adu&platform=pc&upsig=84931ad2760a7440c3ddd97c0b24815c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=69902&mid=142330377&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=16266&logo=80000000'
    # 构造请求头参数
    headers_ = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
        'referer': 'https://www.bilibili.com/video/BV1oR4y1A7GA'
    }
    # 发送请求，获取响应对象
    response_30077 = requests.get(url_30077, headers=headers_)
    response_30280 = requests.get(url_30280, headers=headers_)

    data_30077 = response_30077.content
    data_30280 = response_30280.content

    # 保存数据到本地
    with open('video_30077.mp4', 'wb') as f:
        f.write(data_30077)
    with open('video_30280.mp3', 'wb') as f:
        f.write(data_30280)
    os.system(ffmpeg + ' -i "video_30077.mp4" -i "video_30280.mp3" -c copy "video_full.mp4"')


def crawlVideo():
    url_ = input('url:')
    layer = input('layer:')
    crawlVideos(url_,layer)
    url_file.close()


def crawlVideos(url_,layer):
    global layer_num,url_file
    layer_num = layer_num + 1
    _,_,url_list = getUrl(url_)
    for i in url_list:
        url_file.write(i+'\n')
    url_file.write('\n')
    if(layer_num < layer):
        for url in url_list:
            crawlVideos(url,layer)
    else:
        layer_num = layer_num - 1
        return


# def crawlOneVideo(url_):
#     title_name,html_obj,next_url = getUrl(url_)
#     #下载视频
#     #downloadVideo(html_obj, url_, title_name)
#     return next_url


def getUrl(url_):
    global bvNumList
    headers_ = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
        'cookie': "usercookie",
            }
    # 对主页发送请求，获取响应对象
    response_ = requests.get(url_, headers=headers_)
    data_ = response_.text
    # 转换类型
    html_obj = etree.HTML(data_)
    # 获取名称和BV号
    title_name = html_obj.xpath("//title/text()")[0]
    if re.findall(r'(.*?)_哔哩哔哩', title_name) != []:
        title_name = re.findall(r'(.*?)_哔哩哔哩', title_name)[0]
    bvNum = re.findall(r'/video/(.*?)\?', url_)[0]
    if bvNum[-1] == '/':
        bvNum = bvNum[:-1]
    bvNumList.append(bvNum)
    print('---------------------------------------')
    print(title_name, bvNum)

    # 提取推荐视频列表
    recommend_url = html_obj.xpath("//div[contains(@class,'framepreview-box')]/a/@href")
    bvNumNext = re.findall(r'/video/(.*?)/', recommend_url[0])[0]
    # print(bvNumNext)
    # 通过BV号是否相同判断下个视频是否被爬过
    i = 1
    url_list = []
    while (i<=5):
        while (bvNumNext in bvNumList):
            i = i + 1
            bvNumNext = re.findall(r'/video/(.*?)/', recommend_url[i])[0]
            print(i, bvNumNext)
        next_url = 'https://www.bilibili.com' + recommend_url[i]
        url_list.append(next_url)
        i = i + 1
        print("next_url=", next_url)

    return title_name, html_obj, url_list

def downloadVideo(html_obj,url_,title_name):
    global ffmpeg
    # 提取音视频链接
    url_str = html_obj.xpath("//script[contains(text(),'window.__play')]/text()")[0]
    video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"', url_str)[0]
    audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"', url_str)[0]
    # print(video_url)
    # print(audio_url)
    # 发送请求，获取响应对象
    headers_ = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
        'referer': url_
    }
    response_video = requests.get(url=video_url, headers=headers_)
    response_audio = requests.get(url=audio_url, headers=headers_)
    data_video = response_video.content
    data_audio = response_audio.content

    # 保存数据到本地
    with open('video.mp4', 'wb') as f:
        f.write(data_video)
    with open('audio.mp3', 'wb') as f:
        f.write(data_audio)
    os.system(ffmpeg + f' -i "video.mp4" -i "audio.mp3" -c copy "./video/{title_name}.mp4"')
    os.remove("video.mp4")
    os.remove("audio.mp3")


if __name__ =="__main__":
    crawlVideo()




