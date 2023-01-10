from dataclasses import dataclass








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