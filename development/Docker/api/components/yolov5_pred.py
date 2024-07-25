import torch
import cv2
import subprocess
import sys

# 必要なモジュールのインストール/再インストール

class yolov5_model:
    def __init__(self, model_path = '../models/yolov5s_20240723.pt'):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path = model_path, force_reload=True)
    
    def pred(self, img):
        results = self.model(img)
        print(results)
        res_df = results.pandas().xyxy[0]
        if not res_df.empty:
            res = res_df.iloc[0]['name'] # 予測した物体の名前を取得
        else:
            res = None
        return res
    
    def pip_install(self, package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
    
if __name__ == '__main__':
    # モデルの読み込み
    model = yolov5_model(model_path = '../models/yolov5s_20240723.pt')
    # 画像の読み込み
    img_path = input('画像のパスを入力してください：')
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 予測
    res = model.pred(image)
    print('予測結果：',res)