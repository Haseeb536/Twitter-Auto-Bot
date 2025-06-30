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
from selenium.webdriver.common.action_chains import ActionChains

script_dir = os.path.dirname(os.path.abspath(__file__))

base_path = os.path.join(script_dir, "Elliana Twitter (VA) ✅")
base_path1 = os.path.join(script_dir, "Lexi Twitter (VA)✅")
base_path2 = os.path.join(script_dir, "Miah Twitter (VA)✅")
base_path3 = os.path.join(script_dir, "Katherine Twitter (VA)✅")
# Account details
accounts = [
    
    
    {
    "email": "its_elliana",
    "password": "Elliana!Twitter",
    "cookie_file": os.path.join(script_dir,"cookies.txt"),
    "replied_file": os.path.join(script_dir, "its_elliana_replied.txt"),
    "image_paths": [
        os.path.join(base_path, "IMG_1756.jpeg"),
        os.path.join(base_path, "IMG_1985.jpeg"),
        os.path.join(base_path, "IMG_2883.jpeg"),
        os.path.join(base_path, "IMG_2885.jpeg"),
        os.path.join(base_path, "IMG_3188.jpg"),
        os.path.join(base_path, "IMG_3221.jpg"),
        os.path.join(base_path, "IMG_3222.jpg"),
        os.path.join(base_path, "IMG_3229.jpg"),
        os.path.join(base_path, "IMG_3257.jpg"),
        os.path.join(base_path, "IMG_3258.jpg"),
        os.path.join(base_path, "IMG_3259.jpg"),
        os.path.join(base_path, "IMG_3260.jpg"),
        os.path.join(base_path, "IMG_3261.jpg"),
        os.path.join(base_path, "IMG_3263.jpg"),
        os.path.join(base_path, "IMG_3285.png"),
        os.path.join(base_path, "IMG_3471.png"),
        os.path.join(base_path, "IMG_3473.png"),
        os.path.join(base_path, "IMG_3506.jpg"),
        os.path.join(base_path, "IMG_3559.png"),
        os.path.join(base_path, "IMG_3560.png"),
        os.path.join(base_path, "IMG_3563.png"),
        os.path.join(base_path, "IMG_3565.png"),
        os.path.join(base_path, "IMG_3566.png"),
        os.path.join(base_path, "IMG_3710.jpg"),
        os.path.join(base_path, "IMG_3711.jpg"),
        os.path.join(base_path, "IMG_3712.jpg"),
        os.path.join(base_path, "IMG_3714.jpg"),
        os.path.join(base_path, "IMG_3716.jpg"),
        os.path.join(base_path, "IMG_3718.jpg"),
        os.path.join(base_path, "IMG_3720.mp4"),
        os.path.join(base_path, "IMG_3721.mp4"),
        os.path.join(base_path, "IMG_3765.png"),
        os.path.join(base_path, "IMG_3776.png"),
        os.path.join(base_path, "IMG_4271.png"),
        os.path.join(base_path, "IMG_4272.png"),
        os.path.join(base_path, "IMG_4273.png"),
        os.path.join(base_path, "IMG_4278.png"),
        os.path.join(base_path, "IMG_4643.jpeg"),
        os.path.join(base_path, "IMG_4651.png"),
        os.path.join(base_path, "IMG_4652.png"),
        os.path.join(base_path, "IMG_4654.png"),
        os.path.join(base_path, "IMG_4657.png"),
        os.path.join(base_path, "IMG_4797.jpeg"),
        os.path.join(base_path, "IMG_4836.png"),
        os.path.join(base_path, "IMG_4839.png"),
        os.path.join(base_path, "IMG_4842.png"),
        os.path.join(base_path, "IMG_4889.jpg"),
        os.path.join(base_path, "IMG_5653.png"),
        os.path.join(base_path, "IMG_6625.jpeg"),
        os.path.join(base_path, "IMG_6628.jpeg"),
        os.path.join(base_path, "IMG_6629.jpeg")
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
        "Join me in the hot zone... where things are heating up! 🚨🔥",
        "Dive into the forbidden... it's dangerously tempting! 😈🔥"
        "Embrace the heat of the moment... it's pure bliss! 🔥💕",
        "Unveil the secrets with me... it's a thrilling journey! 🔓😉",
        "Indulge in the passion... it's a wild ride! 🌟😏",
        "Feel the rush of desire... it's electrifying! ⚡🔥",
        "Join me in the firestorm... where fantasies ignite! 🔥✨",
        "Discover the allure of the unknown... it's exhilarating! 🔍😍",
        "Embrace the intensity... it's an addictive adventure! 💥🔥",
        "Let's explore the uncharted... where pleasure awaits! 🌊😘",
        "Escape into the wild side... it's liberating! 🌿🔥",
        "Unlock the mysteries... and let passion guide you! 🔐❤️",
        "Feel the rush of anticipation... it's a tantalizing journey! 🎢😈",
        "Surrender to the allure of temptation... it's irresistible! 🍷🔥",
        "Experience the thrill of the unexpected... it's mesmerizing! ✨😉",
        "Enter the realm of ecstasy... where fantasies come alive! 🌌💫",
        "Engage in the dance of seduction... it's an enchanting symphony! 💃🔥",
        "Let's get lost in the heat of the moment... it's pure ecstasy! 🌋😍",
        "Embrace the heatwave... where passion reigns supreme! 🌞🔥",
        "Delve into the unknown pleasures... it's a journey worth taking! 🌟😘",
        "Feel the pulse of desire... it's an intoxicating rush! 💓🔥",
    ]
},
    {
  "email": "youluvlexi_",
  "password": "Twitter24Lexi",
  "cookie_file": os.path.join(script_dir, "cookies1.txt"),
  "replied_file": os.path.join(script_dir, "youluvlexi_replied.txt"),
  "image_paths": [
    os.path.join(base_path1, "8803657882992479720.mp4"),
    os.path.join(base_path1, "cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_5941_0_0.mp4"),
    os.path.join(base_path1, "cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_5941_1_0.mp4"),
    os.path.join(base_path1, "cm-chat-media-video-1_069923d0-ee14-5d62-8132-d5aeca6e9a31_6095_0_0.mp4"),
    os.path.join(base_path1, "IMG_5971.JPG"),
    os.path.join(base_path1, "IMG_5972.JPG"),
    os.path.join(base_path1, "IMG_5973.JPG"),
    os.path.join(base_path1, "IMG_5974.JPG"),
    os.path.join(base_path1, "IMG_5975.JPG"),
    os.path.join(base_path1, "IMG_5976.JPG"),
    os.path.join(base_path1, "IMG_5977.JPG"),
    os.path.join(base_path1, "IMG_5996.JPG"),
    os.path.join(base_path1, "IMG_5997.JPG"),
    os.path.join(base_path1, "IMG_5998.JPG"),
    os.path.join(base_path1, "IMG_5999.JPG"),
    os.path.join(base_path1, "IMG_6002.JPG"),
    os.path.join(base_path1, "IMG_6003.JPG"),
    os.path.join(base_path1, "IMG_6004.JPG"),
    os.path.join(base_path1, "IMG_6006.JPG"),
    os.path.join(base_path1, "IMG_6007.JPG"),
    os.path.join(base_path1, "IMG_6008.JPG"),
    os.path.join(base_path1, "IMG_6009.JPG"),
    os.path.join(base_path1, "IMG_6032.JPG"),
    os.path.join(base_path1, "IMG_6033.JPG"),
    os.path.join(base_path1, "IMG_6035.JPG"),
    os.path.join(base_path1, "IMG_6037.JPG"),
    os.path.join(base_path1, "IMG_6051.JPG"),
    os.path.join(base_path1, "IMG_6052.JPG"),
    os.path.join(base_path1, "IMG_6053.JPG"),
    os.path.join(base_path1, "IMG_6099.JPG"),
    os.path.join(base_path1, "IMG_6100.JPG"),
    os.path.join(base_path1, "IMG_6101.JPG"),
    os.path.join(base_path1, "IMG_6102.JPG"),
    os.path.join(base_path1, "IMG_6103.JPG"),
    os.path.join(base_path1, "IMG_6104.JPG"),
    os.path.join(base_path1, "IMG_6105.JPG"),
    os.path.join(base_path1, "IMG_6106.JPG"),
    os.path.join(base_path1, "IMG_6378.jpeg"),
    os.path.join(base_path1, "IMG_8605.JPG"),
    os.path.join(base_path1, "IMG_8606.JPG"),
    os.path.join(base_path1, "IMG_8607.JPG"),
    os.path.join(base_path1, "IMG_8628.JPG"),
    os.path.join(base_path1, "IMG_8629.JPG"),
    os.path.join(base_path1, "IMG_8631.JPG"),
    os.path.join(base_path1, "IMG_8632.JPG"),
    os.path.join(base_path1, "IMG_8633.JPG"),
    os.path.join(base_path1, "IMG_8634.JPG"),
    os.path.join(base_path1, "IMG_8636.JPG"),
    os.path.join(base_path1, "IMG_8637.JPG"),
    os.path.join(base_path1, "IMG_8678.JPG"),
    os.path.join(base_path1, "IMG_8679.JPG"),
    os.path.join(base_path1, "IMG_8680.JPG"),
    os.path.join(base_path1, "IMG_8681.JPG"),
    os.path.join(base_path1, "IMG_8683.JPG"),
    os.path.join(base_path1, "IMG_8684.JPG"),
    os.path.join(base_path1, "IMG_8685.JPG"),
    os.path.join(base_path1, "IMG_8689.JPG"),
    os.path.join(base_path1, "IMG_8690.JPG"),
    os.path.join(base_path1, "IMG_8824.JPG"),
    os.path.join(base_path1, "IMG_8825.JPG"),
    os.path.join(base_path1, "IMG_8826.JPG"),
    os.path.join(base_path1, "IMG_8827.JPG"),
    os.path.join(base_path1, "IMG_8828.JPG"),
    os.path.join(base_path1, "IMG_8829.JPG"),
    os.path.join(base_path1, "IMG_8857.JPG"),
    os.path.join(base_path1, "IMG_8859.JPG"),
    os.path.join(base_path1, "IMG_8900.JPG"),
    os.path.join(base_path1, "IMG_8902.JPG"),
    os.path.join(base_path1, "IMG_8923.JPG"),
    os.path.join(base_path1, "IMG_8924.JPG"),
    os.path.join(base_path1, "IMG_8936.JPG"),
    os.path.join(base_path1, "IMG_8937.JPG"),
    os.path.join(base_path1, "IMG_8940.JPG"),
    os.path.join(base_path1, "IMG_8943.JPG"),
    os.path.join(base_path1, "IMG_8949.JPG"),
    os.path.join(base_path1, "IMG_8950.JPG"),
    os.path.join(base_path1, "IMG_8951.JPG"),
    os.path.join(base_path1, "IMG_8952.JPG"),
    os.path.join(base_path1, "IMG_9018.JPG"),
    os.path.join(base_path1, "IMG_9241.JPG"),
    os.path.join(base_path1, "IMG_9242.JPG"),
    os.path.join(base_path1, "1056C23F-F9F9-4D78-A9EC-837C93C4FABD.jpg"),
    os.path.join(base_path1, "-641734583770310966.mp4"),
    os.path.join(base_path1, "-1761824865159514732.mp4"),
    os.path.join(base_path1, "-3324362399840736369.mp4"),
    os.path.join(base_path1, "-6765252637462730363.mp4"),
    os.path.join(base_path1, "-8309298344705269712.mp4")
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
        "Join me in the hot zone... where things are heating up! 🚨🔥",
        "Dive into the forbidden... it's dangerously tempting! 😈🔥"
        "Embrace the heat of the moment... it's pure bliss! 🔥💕",
        "Unveil the secrets with me... it's a thrilling journey! 🔓😉",
        "Indulge in the passion... it's a wild ride! 🌟😏",
        "Feel the rush of desire... it's electrifying! ⚡🔥",
        "Join me in the firestorm... where fantasies ignite! 🔥✨",
        "Discover the allure of the unknown... it's exhilarating! 🔍😍",
        "Embrace the intensity... it's an addictive adventure! 💥🔥",
        "Let's explore the uncharted... where pleasure awaits! 🌊😘",
        "Escape into the wild side... it's liberating! 🌿🔥",
        "Unlock the mysteries... and let passion guide you! 🔐❤️",
        "Feel the rush of anticipation... it's a tantalizing journey! 🎢😈",
        "Surrender to the allure of temptation... it's irresistible! 🍷🔥",
        "Experience the thrill of the unexpected... it's mesmerizing! ✨😉",
        "Enter the realm of ecstasy... where fantasies come alive! 🌌💫",
        "Engage in the dance of seduction... it's an enchanting symphony! 💃🔥",
        "Let's get lost in the heat of the moment... it's pure ecstasy! 🌋😍",
        "Embrace the heatwave... where passion reigns supreme! 🌞🔥",
        "Delve into the unknown pleasures... it's a journey worth taking! 🌟😘",
        "Feel the pulse of desire... it's an intoxicating rush! 💓🔥",
    ]
},
    
    {
  "email": "peachyymiah",
  "password": "Twitter24Miah",
  "cookie_file": os.path.join(script_dir, "cookies2.txt"),
  "replied_file": os.path.join(script_dir, "peachyymiah_replied.txt"),
  "image_paths":[
    os.path.join(base_path2, "Facetune_31-05-2024-19-32-49.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-33-19.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-34-16(1).jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-34-16.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-34-47.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-36-41.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-37-30.jpeg"),
    os.path.join(base_path2, "IMG_6053.jpeg"),
    os.path.join(base_path2, "IMG_6055.jpeg"),
    os.path.join(base_path2, "IMG_6079.jpeg"),
    os.path.join(base_path2, "IMG_6082.jpeg"),
    os.path.join(base_path2, "IMG_6086.jpeg"),
    os.path.join(base_path2, "IMG_6093.jpeg"),
    os.path.join(base_path2, "IMG_6102.jpeg"),
    os.path.join(base_path2, "IMG_6106.jpeg"),
    os.path.join(base_path2, "IMG_6123.jpeg"),
    os.path.join(base_path2, "IMG_6136.jpeg"),
    os.path.join(base_path2, "IMG_6144.jpeg"),
    os.path.join(base_path2, "IMG_6146.jpeg"),
    os.path.join(base_path2, "IMG_6149.jpeg"),
    os.path.join(base_path2, "IMG_6164.jpeg"),
    os.path.join(base_path2, "IMG_6166.jpeg"),
    os.path.join(base_path2, "IMG_6176.jpeg"),
    os.path.join(base_path2, "IMG_6181.jpeg"),
    os.path.join(base_path2, "IMG_6183.jpeg"),
    os.path.join(base_path2, "IMG_6187.jpeg"),
    os.path.join(base_path2, "IMG_6188.jpeg"),
    os.path.join(base_path2, "IMG_6198.jpeg"),
    os.path.join(base_path2, "IMG_6200.jpeg"),
    os.path.join(base_path2, "IMG_6203.jpeg"),
    os.path.join(base_path2, "IMG_6206.jpeg"),
    os.path.join(base_path2, "IMG_6207.mp4"),
    os.path.join(base_path2, "IMG_6209.jpeg"),
    os.path.join(base_path2, "IMG_6210.jpeg"),
    os.path.join(base_path2, "IMG_6211.jpeg"),
    os.path.join(base_path2, "IMG_6213.jpeg"),
    os.path.join(base_path2, "IMG_6216.jpeg"),
    os.path.join(base_path2, "IMG_6219.jpeg"),
    os.path.join(base_path2, "IMG_6220.mp4"),
    os.path.join(base_path2, "IMG_6228.jpeg"),
    os.path.join(base_path2, "Photo 2024-05-24 04.11.16 PM.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-18-53-58.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-18-56-10.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-18-59-16.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-00-56.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-02-57.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-10-49.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-13-01.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-14-08.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-27-08.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-27-44.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-30-12.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-31-22.jpeg"),
    os.path.join(base_path2, "Facetune_31-05-2024-19-32-19.jpeg")
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
        "Join me in the hot zone... where things are heating up! 🚨🔥",
        "Dive into the forbidden... it's dangerously tempting! 😈🔥"
        "Embrace the heat of the moment... it's pure bliss! 🔥💕",
        "Unveil the secrets with me... it's a thrilling journey! 🔓😉",
        "Indulge in the passion... it's a wild ride! 🌟😏",
        "Feel the rush of desire... it's electrifying! ⚡🔥",
        "Join me in the firestorm... where fantasies ignite! 🔥✨",
        "Discover the allure of the unknown... it's exhilarating! 🔍😍",
        "Embrace the intensity... it's an addictive adventure! 💥🔥",
        "Let's explore the uncharted... where pleasure awaits! 🌊😘",
        "Escape into the wild side... it's liberating! 🌿🔥",
        "Unlock the mysteries... and let passion guide you! 🔐❤️",
        "Feel the rush of anticipation... it's a tantalizing journey! 🎢😈",
        "Surrender to the allure of temptation... it's irresistible! 🍷🔥",
        "Experience the thrill of the unexpected... it's mesmerizing! ✨😉",
        "Enter the realm of ecstasy... where fantasies come alive! 🌌💫",
        "Engage in the dance of seduction... it's an enchanting symphony! 💃🔥",
        "Let's get lost in the heat of the moment... it's pure ecstasy! 🌋😍",
        "Embrace the heatwave... where passion reigns supreme! 🌞🔥",
        "Delve into the unknown pleasures... it's a journey worth taking! 🌟😘",
        "Feel the pulse of desire... it's an intoxicating rush! 💓🔥",
    ]
},
    {
  "email": "Katheri94919893",
  "password": "Katherine!Twitter",
  "cookie_file": os.path.join(script_dir, "cookies3.txt"),
  "replied_file": os.path.join(script_dir, "Katheri94919893_replied.txt"),
  "image_paths": [
    os.path.join(base_path, "filtered-E3456281-EBA2-4003-A285-49B26C79A5B7.mp4"),
    os.path.join(base_path, "IMG_6792.png"),
    os.path.join(base_path, "IMG_6988.jpeg"),
    os.path.join(base_path, "IMG_7014.jpg"),
    os.path.join(base_path, "IMG_7064.png"),
    os.path.join(base_path, "IMG_7067.jpeg"),
    os.path.join(base_path, "IMG_7083.jpeg"),
    os.path.join(base_path, "IMG_7084.jpeg"),
    os.path.join(base_path, "IMG_7087.jpeg"),
    os.path.join(base_path, "IMG_7088.jpeg"),
    os.path.join(base_path, "IMG_7118.jpeg"),
    os.path.join(base_path, "IMG_7120.jpeg"),
    os.path.join(base_path, "IMG_7121.jpeg"),
    os.path.join(base_path, "IMG_7124.png"),
    os.path.join(base_path, "IMG_7127.mp4"),
    os.path.join(base_path, "IMG_7131.png"),
    os.path.join(base_path, "IMG_7134.png"),
    os.path.join(base_path, "IMG_7135.jpeg"),
    os.path.join(base_path, "IMG_7136.jpeg"),
    os.path.join(base_path, "IMG_7152.mp4"),
    os.path.join(base_path, "IMG_7286.jpg"),
    os.path.join(base_path, "IMG_7320.jpeg"),
    os.path.join(base_path, "IMG_7321.jpeg"),
    os.path.join(base_path, "IMG_7336.jpeg"),
    os.path.join(base_path, "IMG_7338.jpeg"),
    os.path.join(base_path, "IMG_7339.jpeg"),
    os.path.join(base_path, "IMG_7342.jpeg"),
    os.path.join(base_path, "IMG_7376.jpeg"),
    os.path.join(base_path, "IMG_7543.jpeg"),
    os.path.join(base_path, "IMG_7649.jpg"),
    os.path.join(base_path, "IMG_7676.jpeg"),
    os.path.join(base_path, "IMG_7707.jpg"),
    os.path.join(base_path, "IMG_7712.jpg"),
    os.path.join(base_path, "IMG_7714.jpg"),
    os.path.join(base_path, "IMG_7875.png"),
    os.path.join(base_path, "IMG_7876.png"),
    os.path.join(base_path, "IMG_7881.jpeg"),
    os.path.join(base_path, "IMG_7883.jpeg"),
    os.path.join(base_path, "IMG_8055.jpeg"),
    os.path.join(base_path, "IMG_8057.jpeg"),
    os.path.join(base_path, "IMG_8059.jpeg"),
    os.path.join(base_path, "IMG_8060.jpeg"),
    os.path.join(base_path, "IMG_8061.jpeg"),
    os.path.join(base_path, "filtered-53EA9964-70E6-49CD-9B14-2EF24D3FD795.mp4"),
    os.path.join(base_path, "filtered-E6046DED-D4D4-4FA4-A958-6B6DB0D721BA.mp4")
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
        "Join me in the hot zone... where things are heating up! 🚨🔥",
        "Dive into the forbidden... it's dangerously tempting! 😈🔥"
        "Embrace the heat of the moment... it's pure bliss! 🔥💕",
        "Unveil the secrets with me... it's a thrilling journey! 🔓😉",
        "Indulge in the passion... it's a wild ride! 🌟😏",
        "Feel the rush of desire... it's electrifying! ⚡🔥",
        "Join me in the firestorm... where fantasies ignite! 🔥✨",
        "Discover the allure of the unknown... it's exhilarating! 🔍😍",
        "Embrace the intensity... it's an addictive adventure! 💥🔥",
        "Let's explore the uncharted... where pleasure awaits! 🌊😘",
        "Escape into the wild side... it's liberating! 🌿🔥",
        "Unlock the mysteries... and let passion guide you! 🔐❤️",
        "Feel the rush of anticipation... it's a tantalizing journey! 🎢😈",
        "Surrender to the allure of temptation... it's irresistible! 🍷🔥",
        "Experience the thrill of the unexpected... it's mesmerizing! ✨😉",
        "Enter the realm of ecstasy... where fantasies come alive! 🌌💫",
        "Engage in the dance of seduction... it's an enchanting symphony! 💃🔥",
        "Let's get lost in the heat of the moment... it's pure ecstasy! 🌋😍",
        "Embrace the heatwave... where passion reigns supreme! 🌞🔥",
        "Delve into the unknown pleasures... it's a journey worth taking! 🌟😘",
        "Feel the pulse of desire... it's an intoxicating rush! 💓🔥",
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
def init_driver(lock):
    with lock:
        options = Options()
        options.add_argument("--headless")
        driver = uc.Chrome()
    return driver

# Function to log in to Twitter using cookies
def login_with_cookies(driver, cookie_file, lock):
    with lock:
        driver.get("https://twitter.com")
        time.sleep(4)
        load_cookies(driver, cookie_file)
        driver.refresh()
        time.sleep(10)

# Function to scrape the links of the posts that @andriaa_xo has replied to using BeautifulSoup
def scrape_replied_post_links(driver, main_account):
    driver.get(f"https://twitter.com/{main_account}/with_replies")
    time.sleep(5)
    post_links = set()
    
    while True:
        # Scroll down to load more replies
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all the replied posts
        tweets = soup.find_all('a', {'role': 'link'}, href=True)
        for tweet in tweets:
            link = tweet['href']

            # Filter links to match the pattern of status updates and photo links
            if re.match(r'^/[\w_]+/status/\d+($|/photo/\d+$)', link):
                post_links.add("https://twitter.com" + link)
                print(post_links)
        
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
def reply_to_post(account, post_links, replied_links, lock):
    
    driver = init_driver(lock)
    login_with_cookies(driver, account['cookie_file'], lock)
    time.sleep(1)  # Adding a slight delay to avoid rate limits

    unique_post_links = list(set(post_links) - set(replied_links))
    for post in unique_post_links:
        try:
            
            driver.get(post)
            time.sleep(10)
            wait = WebDriverWait(driver, 20)
            try:
                button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="reply" and contains(@aria-label, "Replies. Reply")]')))
                button.click()
            except:
                # Find the button element using its aria-label attribute
                button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="0 Replies. Reply"]')

                # Scroll to the button if it's not in view
                actions = ActionChains(driver)
                actions.move_to_element(button).perform()

                # Click the button
                button.click()

            time.sleep(10)
            editable_div = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0" and @contenteditable="true"]')))
            editable_div.click()

            # Select a random caption and insert into tweet text
            caption = select_random_caption(account)
            driver.execute_script("arguments[0].innerText = arguments[1];", editable_div, caption)

            # Select a random image path
            image_path = select_random_image(account)
            file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
            file_input.send_keys(image_path)

            sleep(2)
            reply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="tweetButton"]')))
            reply_button.click()

            # Save replied link to file to prevent duplicate replies
            replied_links.add(post)
            save_replied_links(account, [post])

            sleep(20)

        except Exception as e:
            pass

        
    driver.quit()
    
# Function to handle multiprocessing for replying to posts
def process_replies(accounts, post_links):

    lock = multiprocessing.Lock()
    processes = []

    for account in accounts:
        replied_links = load_replied_links(account)
        process = multiprocessing.Process(target=reply_to_post, args=(account, post_links, replied_links, lock))
        processes.append(process)
        process.start()
        time.sleep(1)  # Adding a slight delay to avoid rate limits

    for process in processes:
        process.join()

    print("All accounts have processed.")

# Function to post a main tweet
def post_main_tweet(driver, account, lock):
    with lock:
        try:
            driver.get("https://twitter.com/compose/tweet")
            time.sleep(5)

            wait = WebDriverWait(driver, 20)
            tweet_text_area = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Tweet text"]')))
            caption = select_random_caption(account)
            tweet_text_area.send_keys(caption)

            image_path = select_random_image(account)
            file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
            file_input.send_keys(image_path)

            time.sleep(2)
            tweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
            tweet_button.click()

            time.sleep(10)
            print(f"Main tweet posted for account {account['email']}")
            return True
        except Exception as e:
            print(f"Failed to post main tweet for account {account['email']}: {str(e)}")
            return False

# Function to handle multiprocessing for posting main tweets
def process_main_tweets(accounts):
    lock = multiprocessing.Lock()
    drivers = []
    for account in accounts:
        driver = init_driver(lock)
        login_with_cookies(driver, account['cookie_file'], lock)
        drivers.append(driver)
        time.sleep(1)  # Adding a slight delay to avoid rate limits

    processes = []

    for i, account in enumerate(accounts):
        process = multiprocessing.Process(target=post_main_tweet, args=(drivers[i], account, lock))
        processes.append(process)
        process.start()
        time.sleep(1)  # Adding a slight delay to avoid rate limits

    for process in processes:
        process.join()

    for driver in drivers:
        driver.quit()

    print("All main tweets have been posted.")

def main():
    main_account = "andriaa_xo"  # Replace with your main account
    lock = multiprocessing.Lock()
    driver = init_driver(lock)
    login_with_cookies(driver, accounts[2]['cookie_file'], lock)
    post_links = scrape_replied_post_links(driver, main_account)
    driver.quit()

    # Process replies
    process_replies(accounts, post_links)

    # Process main tweets
    process_main_tweets(accounts)

if __name__ == '__main__':
    main()