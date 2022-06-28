import streamlit as st
from webcam import webcam
import av

captured_image = webcam()

def recv(self, frame):
    # 将图片转成 Numpy 数组
    img = frame.to_ndarray(format="bgr24")
    # 边缘检测算子
    img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)
    # .recv()的输出将显示在屏幕上
    return av.VideoFrame.from_ndarray(img, format="bgr24")

if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    
    image = recv(captured_image)
    st.image(image)
    
