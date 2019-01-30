'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual( 
                run_markdown('this line has no special handling'), 
                '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual( 
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')

    def test_h1(self):
        '''
        Convert lines starting with # to <h1> elements
        '''
        self.assertEqual( run_markdown('# Heada Hea'), '<h1>Heada Hea</h1>' )

    def test_h2(self):
        '''
        #Convert lines starting with # to <h2> elements
        '''
        self.assertEqual( run_markdown('## h2 header here'), '<h2>h2 header here</h2>' )

    def test_h3(self):
        '''
        #Convert lines starting with # to <h3> elements
        '''
        self.assertEqual( run_markdown('### nother header'), '<h3>nother header</h3>' )

    def test_blockquote_1(self):
        '''
        basic blockquote test
        '''
        self.assertEqual( run_markdown('> 1\n> 2\n> 3\n4'), '<blockquote>\r\n<p>1</p> <p>2</p> <p>3</p> </blockquote>\r\n<p>4</p>' )

    def test_blockquote_2(self):
        '''
        testing block quote with a header inside
        '''    
        self.assertEqual( run_markdown('> # header\n> paragraph\nquote over'),'<blockquote>\r\n<h1>header</h1>\r\n<p>paragraph</p> </blockquote>\r\n<p>quote over</p>' )

if __name__ == '__main__':
    unittest.main()

