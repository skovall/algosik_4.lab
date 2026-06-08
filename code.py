import hashlib
import re

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.code_length = 4
    
    def _generate_code(self, long_url):
        hash_object = hashlib.md5(long_url.encode())
        hash = hash_object.hexdigest()
        code = hash[:self.code_length]
        return code
    
    def _is_valid_url(self, url):
        if not (url.startswith("http://") or url.startswith("https://")):
            return False
        if len(url.split("://")[1]) < 1:
            return False
        return True
    
    def add_url(self, long_url):
        if not self._is_valid_url(long_url):
            raise ValueError("Некорректный URL")
        
        short_code = self._generate_code(long_url)
        
        if short_code in self.url_mapping:
            if self.url_mapping[short_code] == long_url:
                return short_code
            else:
                self.code_length += 1
                short_code = self._generate_code(long_url)
        
        self.url_mapping[short_code] = long_url
        return short_code
    
    def get_url(self, short_code):
        if short_code in self.url_mapping:
            return self.url_mapping[short_code]
        return None
    
    def exists(self, short_code):
        return short_code in self.url_mapping
    
    def delete_url(self, short_code):
        if short_code in self.url_mapping:
            del self.url_mapping[short_code]
            return True
        return False
    
    def display_all(self):
        if not self.url_mapping:
            print("Сохранённых ссылок нет")
            return
        
        for code, url in self.url_mapping.items():
            print(f"{code} -> {url}")
