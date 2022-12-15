#!/usr/bin/env python
from dataclasses import dataclass
from bs4 import BeautifulSoup
import subprocess

@dataclass
class Snag:
    raw_tag: str
    snag_src: str
    snag_stdin: str
    snag_stdout: str

class SnagParser:
    
    global_snags: Snag = []
    
    def parse(self, content: str):
        
        snags = BeautifulSoup(content, 'html.parser').find_all('snag')
        for s in snags:
            
            tag = s
            src = s['src']
            stdin = s.string
            stdout = subprocess.run(src, stdin=stdin, stdout=subprocess.PIPE)
            snag_obj = Snag(s, s['src'], s.string)
        
        
        
        
        
if __name__ == "__main__":
    
    content = """<html>
    <head>
        <title>My Page</title>
    </head>
    <snag src="header.sgs">Test</snag>
    <snag src="footer.sgs">Toast</snag>
</html>"""
    SnagParser.parse(content)