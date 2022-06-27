# 来源：https://blog.csdn.net/woshicver/article/details/125364947
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("my first streamlit app")
st.write("hello world")

# webrtc_streamer(key="example")
# class VideoProcessor:
#     def recv(self, frame):
#         img = frame.to_ndarray(format="bgr24")
#         # 边缘检测算子
#         img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
#
#         return av.VideoFrame.from_ndarray(img, format="bgr24")

class VideoProcessor2:
    def __init__(self):
        self.threshold1 = 100
        self.threshold2 = 200

    # .recv()的输入是来自网络摄像头的图像帧。
    def recv(self, frame):
        # 将图片转成 Numpy 数组
        img = frame.to_ndarray(format="bgr24")
        # 边缘检测算子
        img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)
        # .recv()的输出将显示在屏幕上
        return av.VideoFrame.from_ndarray(img, format="bgr24")

'''
webrtc_streamer返回一个上下文对象，因此我们将其分配给ctx变量。
通过video_processor_factory参数传递给webrtc_streamer()的类对象将被实例化
并设置为ctx。当视频流不活动时，它不会被设置，所以我们用if子句检查它的存在。
'''
ctx = webrtc_streamer(key="example", video_processor_factory=VideoProcessor2)
if ctx.video_processor:
    ctx.video_processor.threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
    ctx.video_processor.threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=100)