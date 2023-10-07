# ImageDescriber

## Overview
ImageDescriber is a straightforward Python script that leverages Azure Cognitive Services to analyze and describe the contents of an image. This script is ideal for those looking to quickly obtain descriptive information about images without extensive setup.

## Installation
1. Ensure you have Python 3.x installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the project directory and run the following command to install the necessary dependencies:
```bash
pip install -r requirements.txt
```
4. Set up an Azure Cognitive Services account, and replace `YOUR_AZURE_COGNITIVE_SERVICES_ENDPOINT` and `YOUR_AZURE_COGNITIVE_SERVICES_API_KEY` in `main.py` with your own credentials.

## Usage
Run the following command in your terminal, replacing `<path_to_image>` with the path to the image you want to analyze:
```bash
python main.py <path_to_image>
```

## Notes
- Ensure that the image path provided is correct to avoid any file not found errors.
- The script currently only returns one description, regardless of the number of objects in the image.

## License
This project is licensed under the terms of the MIT license.

---

# ImageDescriber（日本語）

## 概要
ImageDescriberは、Azure Cognitive Servicesを利用して、ユーザーが提供する画像の内容を分析し、説明するシンプルなPythonスクリプトです。このスクリプトは、広範な設定なしで画像に関する記述情報を素早く取得したい人に理想的です。

## インストール方法
1. お使いのマシンにPython 3.xがインストールされていることを確認します。
2. このリポジトリをローカルマシンにクローンします。
3. プロジェクトディレクトリに移動し、以下のコマンドを実行して必要な依存関係をインストールします：
```bash
pip install -r requirements.txt
```
4. Azure Cognitive Servicesアカウントを設定し、`main.py`の`YOUR_AZURE_COGNITIVE_SERVICES_ENDPOINT`および`YOUR_AZURE_COGNITIVE_SERVICES_API_KEY`を自分の資格情報に置き換えます。

## 使い方
ターミナルで以下のコマンドを実行し、`<path_to_image>`を分析する画像のパスに置き換えます：
```bash
python main.py <path_to_image>
```

## 注意点
- ファイルが見つからないエラーを避けるために、提供される画像のパスが正しいことを確認してください。
- 現在のスクリプトは、画像内のオブジェクトの数に関係なく、1つの説明しか返しません。

## ライセンス
このプロジェクトはMITライセンスの条件の下でライセンスされています。
