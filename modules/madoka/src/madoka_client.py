class MadokaClient:
    def __init__(self, url: str):
        self._url = url

    def get_url(self) -> str:
        return self._url
    
    def is_ready(self) -> bool:
        return True
