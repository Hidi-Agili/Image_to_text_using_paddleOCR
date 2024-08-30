from paddleocr import PaddleOCR

class OCRProcessor:
    def __init__(self, use_angle_cls=True, lang='en', use_space_char=True, show_log=False, enable_mkldnn=True, use_gpu=False):
        self.ocr = PaddleOCR(
            use_angle_cls=use_angle_cls, 
            lang=lang, 
            use_space_char=use_space_char, 
            show_log=show_log, 
            enable_mkldnn=enable_mkldnn, 
            use_gpu=None)

# The main block of code
    def process_image(self, img_path):
        result = self.ocr.ocr(img_path, cls=True)
        ocr_string = ""
        for i in range(len(result[0])):
            ocr_string = ocr_string + result[0][i][1][0] + " "
#        for line in result:
#            for _, text, _ in line:
#                ocr_string += text + " "
        return ocr_string

ocr_processor = OCRProcessor()
