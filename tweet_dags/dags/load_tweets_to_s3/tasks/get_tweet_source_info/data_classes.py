from dataclasses import dataclass
from typing import List







@dataclass
class TweetSourceInfo:
    author: str
    title: str 
    section_title: str 
    pages: str 
    link: str
    tags: str

    def get_invalid_fields(self) -> List[str]:
        invalid_fields: List[str] = []
        required_fields: List[str] = ['author', 'title', 'section_title', 'link', 'tags']
        for field in required_fields:
            value: str = getattr(self, field)
            if not value:
                invalid_fields.append(field)
        return invalid_fields