import unittest
from test import calculate_roas

class TestUtils(unittest.TestCase):
    body = [['ladies clown wigs', 'Exact match', 'None', 'Shift - Shopping - GB - California Costumes - HIGH', 'Shift - Shopping - GB - California Costumes - HIGH - stream-december-massachusetts-maine - a09725c7cc0549b08eecba5ecd588692', '1', 'GBP', '0.35', '3', '0', '0'],
['80s icons fancy dress', 'Exact match', 'None', 'Shift - Shopping - GB - Rubies UK Masquerade - MEDIUM', 'Shift - Shopping - GB - Rubies UK Masquerade - MEDIUM - lake-fanta-winter-aspen - 603d19312ff54ad2955c81bfcaffecd5', '1', 'GBP', '0.18', '1', '0', '0'],
['merida princess dress', 'Exact match', 'None', 'Shift - Shopping - GB - Rubies UK Masquerade - MEDIUM', 'Shift - Shopping - GB - Rubies UK Masquerade - MEDIUM - glucose-ack-enemy-carbon - 60e9d409ea774cd1a727823d346c3671', '1', 'GBP', '0.2', '1', '0', '0'],
['eighties fancy dress', 'Exact match', 'None', 'Shift - Shopping - GB - Rubies UK Masquerade - MEDIUM', 'Shift - Shopping - GB - Rubies UK Masquerade - MEDIUM - carbon-may-oscar-nineteen - 3d2ec2ce11884a54b102756e7fd7f5c1', '3', 'GBP', '0.55', '106', '0', '0'],
['retro coulour suite', 'Exact match', 'None', 'Shift - Shopping - GB - OppoSuits - HIGH', 'Shift - Shopping - GB - OppoSuits - HIGH - hawaii-finch-juliet-red - 8c517ff9d87245aa8b9f3e467ec08482', '2', 'GBP', '0.2', '1', '0', '0'],
['eleven adult costume', 'Exact match', 'None', 'Shift - Shopping - GB - Franco - LOW', 'Shift - Shopping - GB - Franco - LOW - west-pluto-quebec-lemon - 32b86c14aa9c45c29d780757e2cd164e', '1', 'GBP', '0.07', '2', '0', '0'],
['womens long halloween costumes', 'Exact match', 'None', 'Shift - Shopping - GB - Fun World - HIGH', 'Shift - Shopping - GB - Fun World - HIGH - fix-bacon-carpet-magnesium - 505249030cfa47a1a3307dcc86158e9d', '1', 'GBP', '0.11', '4', '0', '0'],
['marie antoinette fancy dress uk', 'Exact match', 'None', 'Shift - Shopping - GB - Franco - MEDIUM', 'Shift - Shopping - GB - Franco - MEDIUM - alaska-summer-ten-snake - 76f4cd4c682147d89115bee00ec71614', '1', 'GBP', '0.07', '2', '0', '0']]

    
    def test_calculate_roas(self):
        response = []
        for row in self.body:
            response.append(calculate_roas(row) )
        print(response)
        print
        self.assertEquals(type(response), list)


if __name__ == '__main__':
    unittest.main()