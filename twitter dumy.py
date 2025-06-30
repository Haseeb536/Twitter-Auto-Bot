import json
import os
import random
from time import sleep
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import multiprocessing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import schedule
import time

# Account details
accounts = [
    
    {
    "email": "its_elliana",
    "password": "Elliana!Twitter",
    "cookie_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\cookies.txt",
    "replied_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\its_elliana_replied.txt",
    "image_paths": [
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_1756.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_1985.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_2883.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_2885.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3188.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3221.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3222.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3229.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3257.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3258.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3259.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3260.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3261.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3263.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3285.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3471.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3473.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3506.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3559.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3560.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3563.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3565.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3566.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3710.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3711.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3712.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3714.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3716.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3718.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3720.mp4",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3721.mp4",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3765.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_3776.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4271.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4272.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4273.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4278.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4643.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4651.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4652.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4654.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4657.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4797.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4836.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4839.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4842.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_4889.jpg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_5653.png",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_6625.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_6628.jpeg",
        r"C:\Users\Haseeb\Desktop\twitter\Elliana Twitter (VA) ✅\IMG_6629.jpeg"
    ],
    "captions": [
        "Come closer and see what you've been missing! 🔥😉",
        "I've been leaked too... and it's incredibly thrilling! 😏🔞",
        "That moment when it gets hot and steamy... 🌡️🔥",
        "Explore the heat with me... it's getting intense! 🔥🥵",
        "Discover the spicy side of life with me! 🌶️😍",
        "I'm feeling the heat... and it's irresistible! 🔥😘",
        "Get ready to be amazed by the sizzling moments ahead! 🌟🔥",
        "It's getting leaked, and I'm loving every moment of it! 😈💋",
        "Step into the steamy side of life... it's oh-so-sexy! 💦🔥",
        "Join me in the hot zone... where things are heating up! 🚨🔥"
    ]
},
    {
  "email": "youluvlexi_",
  "password": "Twitter24Lexi",
  "cookie_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\cookies1.txt",
  "replied_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\youluvlexi_replied.txt",
  "image_paths": [
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\1056C23F-F9F9-4D78-A9EC-837C93C4FABD.jpg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\-641734583770310966.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\-1761824865159514732.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\-3324362399840736369.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\-6765252637462730363.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\-8309298344705269712.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\8803657882992479720.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_5941_0_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_5941_1_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6095_0_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6106_8_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6178_6_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6178_7_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6345_1_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6379_7_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6379_8_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6424_9_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6424_10_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6424_11_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6510_7_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6575_0_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6791_8_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6793_0_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_7612_10_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_7835_2_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_7835_3_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_8114_4_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_8114_7_0.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5384.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5386.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5484.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5513.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5520.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5521.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5564.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5565.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5566.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5567.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5568.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5569.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5570.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5571.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5572.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5573.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5574.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5575.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5576.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5577.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5578.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5579.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5580.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5581.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5582.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5583.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5584.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5585.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5586.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5587.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5588.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5589.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5590.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5591.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5592.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5593.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5594.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5595.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5596.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5597.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5598.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5599.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5600.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5601.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5602.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5603.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5604.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5605.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5606.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5607.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5608.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5609.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5610.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5611.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5612.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5613.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5614.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5615.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5616.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5617.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5618.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5619.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5620.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5621.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5622.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5623.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5624.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5625.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5626.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5627.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5628.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5629.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5630.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5631.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5632.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5633.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5634.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5635.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5636.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5637.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5638.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5639.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5640.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5641.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5642.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5643.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5644.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5645.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5646.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5647.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5648.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5649.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5650.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5651.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5652.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5653.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5654.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5655.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5656.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5657.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5658.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5659.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5660.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5661.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5662.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5663.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5664.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5665.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5666.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5667.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5668.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5669.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5670.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5671.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5672.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5673.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5674.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5675.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5676.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5677.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5678.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5679.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5680.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5681.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5682.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5683.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5684.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5685.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5686.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5687.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5688.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5689.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5690.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5691.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5692.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5693.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5694.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5695.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5696.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5697.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5698.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5699.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5700.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5701.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5702.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5703.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5704.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5705.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5706.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5707.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5708.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5709.JPG",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Lexi Twitter (VA)✅\\IMG_5710.JPG"
    
    ],
    "captions": [
        "Come closer and see what you've been missing! 🔥😉",
        "I've been leaked too... and it's incredibly thrilling! 😏🔞",
        "That moment when it gets hot and steamy... 🌡️🔥",
        "Explore the heat with me... it's getting intense! 🔥🥵",
        "Discover the spicy side of life with me! 🌶️😍",
        "I'm feeling the heat... and it's irresistible! 🔥😘",
        "Get ready to be amazed by the sizzling moments ahead! 🌟🔥",
        "It's getting leaked, and I'm loving every moment of it! 😈💋",
        "Step into the steamy side of life... it's oh-so-sexy! 💦🔥",
        "Join me in the hot zone... where things are heating up! 🚨🔥"
    ]
},
    
    {
  "email": "peachyymiah",
  "password": "Twitter24Miah",
  "cookie_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\cookies2.txt",
  "replied_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\peachyymiah_replied.txt",
  "image_paths": [
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-32-49.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-33-19.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-34-16(1).jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-34-16.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-34-47.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-36-41.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-37-30.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6053.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6055.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6079.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6082.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6086.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6093.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6102.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6106.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6123.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6136.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6144.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6146.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6149.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6164.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6166.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6176.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6181.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6183.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6187.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6188.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6198.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6200.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6203.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6206.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6207.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6209.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6210.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6211.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6213.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6216.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6219.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6220.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\IMG_6228.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Photo 2024-05-24 04.11.16 PM.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-18-53-58.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-18-56-10.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-18-59-16.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-00-56.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-02-57.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-10-49.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-13-01.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-14-08.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-27-08.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-27-44.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-30-12.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-31-22.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Miah Twitter (VA)✅\\Facetune_31-05-2024-19-32-19.jpeg"
  ],
  "captions": [
        "Come closer and see what you've been missing! 🔥😉",
        "I've been leaked too... and it's incredibly thrilling! 😏🔞",
        "That moment when it gets hot and steamy... 🌡️🔥",
        "Explore the heat with me... it's getting intense! 🔥🥵",
        "Discover the spicy side of life with me! 🌶️😍",
        "I'm feeling the heat... and it's irresistible! 🔥😘",
        "Get ready to be amazed by the sizzling moments ahead! 🌟🔥",
        "It's getting leaked, and I'm loving every moment of it! 😈💋",
        "Step into the steamy side of life... it's oh-so-sexy! 💦🔥",
        "Join me in the hot zone... where things are heating up! 🚨🔥"
    ]
},

        {
  "email": "Katheri94919893",
  "password": "Katherine!Twitter",
  "cookie_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\cookies3.txt",
  "replied_file": "C:\\Users\\Haseeb\\Desktop\\twitter\\Katheri94919893_replied.txt",
  "image_paths": [
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\filtered-E3456281-EBA2-4003-A285-49B26C79A5B7.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_6792.png",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_6988.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7014.jpg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7064.png",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7067.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7083.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7084.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7087.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7088.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7118.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7120.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7121.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7124.png",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7127.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7131.png",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7134.png",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7135.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7136.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7152.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7286.jpg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7320.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7321.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7336.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7338.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7339.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7342.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7376.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7543.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7649.jpg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7676.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7707.jpg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7712.jpg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7714.jpg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7875.png",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7876.png",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7881.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_7883.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_8055.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_8057.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_8059.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_8060.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\IMG_8061.jpeg",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\filtered-53EA9964-70E6-49CD-9B14-2EF24D3FD795.mp4",
    "C:\\Users\\Haseeb\\Desktop\\twitter\\Katherine Twitter (VA)✅\\filtered-E6046DED-D4D4-4FA4-A958-6B6DB0D721BA.mp4"
  ],
  "captions": [
        "Come closer and see what you've been missing! 🔥😉",
        "I've been leaked too... and it's incredibly thrilling! 😏🔞",
        "That moment when it gets hot and steamy... 🌡️🔥",
        "Explore the heat with me... it's getting intense! 🔥🥵",
        "Discover the spicy side of life with me! 🌶️😍",
        "I'm feeling the heat... and it's irresistible! 🔥😘",
        "Get ready to be amazed by the sizzling moments ahead! 🌟🔥",
        "It's getting leaked, and I'm loving every moment of it! 😈💋",
        "Step into the steamy side of life... it's oh-so-sexy! 💦🔥",
        "Join me in the hot zone... where things are heating up! 🚨🔥"
    ]
}

]

url = "https://twitter.com"

# Function to load cookies from a text file
def load_cookies(driver, path):
    with open(path, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)

# Function to initialize the Chrome driver safely
def init_driver():
    options = Options()
    options.add_argument("--headless")
    driver = uc.Chrome()
    return driver

# Function to log in to a Twitter account using cookies
def login_with_cookies(driver, cookie_file):
    driver.get(url)
    sleep(4)
    load_cookies(driver, cookie_file)
    driver.refresh()
    sleep(10)

# Function to scrape the links of the posts that @andriaa_xo has replied to using BeautifulSoup
def scrape_replied_post_links(driver, main_account):
    driver.get(f"https://twitter.com/{main_account}/with_replies")
    sleep(5)
    post_links = set()
    
    while True:
        # Scroll down to load more replies
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all the replied posts
        tweets = soup.find_all('a', {'role': 'link'}, href=True)
        for tweet in tweets:
            link = tweet['href']

            # Filter links to match the pattern of status updates and photo links
            if re.match(r'^/[\w_]+/status/\d+($|/photo/\d+$)', link):
                post_links.add("https://twitter.com" + link)
        
        # Break if there are no more new links to add
        if len(post_links) >= 100:
            break
    
    return list(post_links)

# Function to save replied links to a file
def save_replied_links(account, replied_links):
    with open(account['replied_file'], 'a') as file:
        for link in replied_links:
            file.write(link + '\n')

# Function to load replied links from a file
def load_replied_links(account):
    replied_links = set()
    with open(account['replied_file'], 'r') as file:
        for line in file:
            replied_links.add(line.strip())
    return replied_links

# Function to select a random image path
def select_random_image(account):
    return random.choice(account['image_paths'])

# Function to select a random caption
def select_random_caption(account):
    return random.choice(account['captions'])

# Function to reply to a post
def reply_to_post(driver, account, post_url, replied_links):
    try:
        driver.get(post_url)
        sleep(10)
        wait = WebDriverWait(driver, 20)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Reply"]')))
        button.click()

        sleep(10)
        editable_div = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Tweet text"]')))
        editable_div.click()

        # Select a random caption and insert into tweet text
        caption = select_random_caption(account)
        driver.execute_script("arguments[0].innerText = arguments[1];", editable_div, caption)

        # Select a random image path
        image_path = select_random_image(account)
        file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
        file_input.send_keys(image_path)

        sleep(2)
        reply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
        reply_button.click()

        # Save replied link to file to prevent duplicate replies
        replied_links.add(post_url)
        save_replied_links(account, [post_url])

        sleep(5)
        return True
    except Exception as e:
        print(f"Account {account['email']} failed to post: {str(e)}")
        return False

# Function to post the main tweet
def post_main_tweet(driver, account):
    try:
        driver.get("https://twitter.com/compose/tweet")
        sleep(5)

        wait = WebDriverWait(driver, 20)
        tweet_text_area = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Tweet text"]')))
        caption = select_random_caption(account)
        tweet_text_area.send_keys(caption)

        image_path = select_random_image(account)
        file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
        file_input.send_keys(image_path)

        sleep(2)
        tweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
        tweet_button.click()

        sleep(10)
        print(f"Main tweet posted for account {account['email']}")
        return True
    except Exception as e:
        print(f"Failed to post main tweet for account {account['email']}: {str(e)}")
        return False

# Function to handle multiprocessing for replying to posts
def process_replies(accounts, post_links):
    drivers = []
    for account in accounts:
        driver = init_driver()
        login_with_cookies(driver, account['cookie_file'])
        drivers.append(driver)
        sleep(1)  # Adding a slight delay to avoid rate limits

    output_queue = multiprocessing.Queue()
    processes = []

    for i, account in enumerate(accounts):
        replied_links = load_replied_links(account)
        for post_url in post_links:
            if post_url not in replied_links:
                process = multiprocessing.Process(target=reply_to_post, args=(drivers[i], account, post_url, replied_links))
                processes.append(process)
                process.start()
                sleep(1)  # Adding a slight delay to avoid rate limits

    for process in processes:
        process.join()

    for driver in drivers:
        driver.quit()

    print("All accounts have processed.")

# Function to handle multiprocessing for posting main tweets
def process_main_tweets(accounts):
    drivers = []
    for account in accounts:
        driver = init_driver()
        login_with_cookies(driver, account['cookie_file'])
        drivers.append(driver)
        sleep(1)  # Adding a slight delay to avoid rate limits

    output_queue = multiprocessing.Queue()
    processes = []

    for i, account in enumerate(accounts):
        process = multiprocessing.Process(target=post_main_tweet, args=(drivers[i], account))
        processes.append(process)
        process.start()
        sleep(1)  # Adding a slight delay to avoid rate limits

    for process in processes:
        process.join()

    for driver in drivers:
        driver.quit()

    print("All main tweets have been posted.")

def job_scrape_replied_post_links(accounts):
    main_account = "andriaa_xo"
    driver = init_driver()
    login_with_cookies(driver, accounts[0]['cookie_file'])
    post_links = scrape_replied_post_links(driver, main_account)
    driver.quit()
    process_replies(accounts, post_links)

def job_process_main_tweets(accounts):
    process_main_tweets(accounts)

def scheduler():
    # Schedule the job to scrape replied post links and process replies every hour
    schedule.every().hour.do(job_scrape_replied_post_links, accounts)

    # Schedule the job to process main tweets once a day at a specific time
    schedule.every().day.at("09:00").do(job_process_main_tweets, accounts)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    scheduler()