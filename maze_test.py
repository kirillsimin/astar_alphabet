import unittest
import maze


class Testing(unittest.TestCase):

    def test_find_start(self):
        test_maze = [['#','#','#','_','#','#'],['#','_','_','_','_','#'],['#','_','#','#','#','#']]
        start = maze.find_start(test_maze)

        self.assertEqual(start, (0,3))

    def test_find_end(self):
        test_maze = [['#','#','#','_','#','#'],['#','_','_','_','_','#'],['#','_','#','#','#','#']]
        start = maze.find_end(test_maze)

        self.assertEqual(start, (2,1))

    def test_build_maze(self):
        text = '###_##\n#____#\n#_####'
        expected_maze = [['#','#','#','_','#','#'],['#','_','_','_','_','#'],['#','_','#','#','#','#']]

        result = maze.build_maze(text)

        self.assertEqual(result, expected_maze)

    def test_build_solved_maze(self):
        test_maze = [['#','#','#','_','#','#'],['#','_','_','_','_','#'],['#','_','#','#','#','#']]
        path = [(0, 3), (1, 3), (1, 2), (1, 1), (2, 1)]

        solved_maze = maze.build_solved_maze(test_maze, path)
        expected_solved_maze = [['#','#','#','a','#','#'],['#','d','c','b','_','#'],['#','e','#','#','#','#']]

        self.assertEqual(solved_maze, expected_solved_maze)


        

if __name__ == '__main__':
    unittest.main()
