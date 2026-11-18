import tempfile
import unittest
from pathlib import Path
from PIL import Image
from main import extract_palette, render_css

class PaletteTests(unittest.TestCase):
    def test_extracts_requested_colors_and_css(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"colors.png"
            image=Image.new("RGB",(20,10))
            for x in range(20):
                for y in range(10): image.putpixel((x,y),(255,0,0) if x<10 else (0,0,255))
            image.save(path)
            palette=extract_palette(path,2)
            self.assertEqual(len(palette),2)
            self.assertIn("--palette-1:",render_css(palette))

if __name__=="__main__": unittest.main()
