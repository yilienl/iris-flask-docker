# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# 建立 Flask App
app = Flask(__name__)

# 載入模型
model = joblib.load('iris_model.pkl')

# 設定首頁
@app.route('/')
def home():
    return "Iris ML Model API is running!"

# 預測端點
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)  # 從 JSON 取得輸入資料

    try:
        # 將資料轉換為 numpy 陣列（模型需要）
        input_data = np.array(data['features']).reshape(1, -1)

        # 預測
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data).max()

        # 回傳預測結果
        return jsonify({
            'prediction': int(prediction[0]),
            'confidence': f"{probability * 100:.2f}%"
        })

    except Exception as e:
        return jsonify({'error': str(e)})

# 啟動伺服器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
