<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:ec4899&height=170&section=header&text=Image%20Palette%20Extractor&fontColor=ffffff&fontSize=38&animation=fadeIn" width="100%" alt="Image Palette Extractor banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=900&color=EC4899&center=true&vCenter=true&width=650&lines=Extract+dominant+image+colors;Export+CSS+variables+or+JSON;Keep+image+processing+local" alt="Typing introduction"/>
<p>Turn an image into a reusable color palette.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/image-palette-extractor?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/image-palette-extractor?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/image-palette-extractor?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/image-palette-extractor?style=for-the-badge" alt="Last commit"/></p>
<img src="assets/icon.svg" width="112" alt="Project icon"/>
</div>

## ✨ Overview
Image Palette Extractor samples an image locally, finds its most common representative colors with Pillow quantization, and exports the result as CSS custom properties or JSON.

## 🚀 Features
- ✨ Extract a configurable number of dominant colors
- ✨ Sort colors by their pixel frequency
- ✨ Export CSS variables or structured JSON
- ✨ Process images locally without uploads
- ✨ Accept common raster formats supported by Pillow

## 🎬 Demo
Run `python main.py photo.png --colors 8 --format css --output palette.css` to create a stylesheet palette.

## ⚡ Quick Start
```bash
python -m pip install -r requirements.txt
python main.py photo.png --colors 8 --format css --output palette.css
```

## 🧰 Tech Stack
Python 3.10+ and Pillow.

## 🗂️ Folder Structure
```text
.
├── main.py
├── requirements.txt
├── tests/test_main.py
├── assets/icon.svg
├── .gitignore
└── LICENSE
```

## 🧭 Roadmap
- [ ] Add a palette preview HTML export
- [ ] Add optional image sampling limits
- [ ] Add a simple color-name approximation

## 🤝 Contributing
Issues and focused pull requests are welcome. Include a small test image generated in code when adding behavior.

## 📄 License
Released under the [MIT License](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:ec4899&height=100&section=footer" width="100%" alt="Animated wave footer"/></div>
