import requests
import json
import sys

# Azureの設定
ENDPOINT = "YOUR_AZURE_COGNITIVE_SERVICES_ENDPOINT"  # 例: "https://your-region.api.cognitive.microsoft.com/"
API_KEY = "YOUR_AZURE_COGNITIVE_SERVICES_API_KEY"
ANALYZE_URL = ENDPOINT + "vision/v3.0/describe"

def describe_image(image_path):
    # 画像をバイナリとして読み込む
    with open(image_path, 'rb') as image_file:
        headers = {
            'Ocp-Apim-Subscription-Key': API_KEY,
            'Content-Type': 'application/octet-stream'
        }
        params = {
            'maxCandidates': '1'  # 返される説明の数
        }
        response = requests.post(ANALYZE_URL, headers=headers, params=params, data=image_file)

        response.raise_for_status()

        analysis = response.json()

        # 分析結果から説明を取得
        description = analysis["description"]["captions"][0]["text"]
        return description

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    result = describe_image(image_path)
    print(result)
