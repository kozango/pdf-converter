from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image(filename, text, width=800, height=1100):
    # 新しい画像を作成（白背景）
    img = Image.new('RGB', (width, height), color='white')
    d = ImageDraw.Draw(img)
    
    # フォントの設定
    try:
        font = ImageFont.truetype("Arial", 40)
    except IOError:
        font = ImageFont.load_default()
    
    # テキストを描画
    d.text((width//4, height//2), f"Sample Image {text}", fill="black", font=font)
    
    # 画像を保存
    os.makedirs('test_images', exist_ok=True)
    img.save(os.path.join('test_images', filename))
    print(f"Created: test_images/{filename}")

# テスト用の画像を3つ作成
create_test_image("sample1.jpg", "1/3")
create_test_image("sample2.jpg", "2/3")
create_test_image("sample3.jpg", "3/3")
