from dataclasses import dataclass
from typing import List








@dataclass
class Tweet:
    content: str
    thread_num: int
    thread_order_num: int
    thread_caption: bool 
    source_author: str
    source_title: str 
    source_section_title: str
    source_link: str 
    tags: str
    source_pages: str = ''

    def to_list(self) -> List:
        lst: List = [
            self.content,
            self.thread_num,
            self.thread_order_num,
            self.thread_caption,
            self.source_author,
            self.source_title,
            self.source_section_title,
            self.source_pages,
            self.source_link,
            self.tags
        ]
        return lst