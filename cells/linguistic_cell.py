import hashlib

class LinguisticCell:
    """Biến đổi văn bản thành vector ngữ nghĩa không gian 11 chiều trong [0.0, 1.0] bằng SHAKE-256"""
    @staticmethod
    def embed_text_11d(text):
        if not text:
            return [0.0] * 11
        clean_text = str(text).strip().lower()
        coords = []
        for d in range(11):
            seed = f"{clean_text}_nexus11_undeca_axis_{d}".encode()
            val = int(hashlib.shake_256(seed).hexdigest(4), 16) / 65535.0
            coords.append(round(val, 4))
        return coords
