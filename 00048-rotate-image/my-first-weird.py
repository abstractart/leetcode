class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        visited = collections.defaultdict(lambda: collections.defaultdict(lambda: False))
        self.rotateInPlaceRec(matrix, 0, len(matrix) - 1, visited)
        
        
    def rotateInPlaceRec(self, image, start_index, end_index, visited):
        if start_index >= end_index:
            return image

        start = [start_index, start_index]
        curr_elem = start
        while(not visited[curr_elem[0]][curr_elem[1]]):
            prev_place = curr_elem
            prev_val = image[prev_place[0]][prev_place[1]]
            new_place = self.new_place_for(prev_place[0], prev_place[1], start_index, end_index)
            new_val = image[new_place[0]][new_place[1]]

            while(not visited[new_place[0]][new_place[1]]):
                image[new_place[0]][new_place[1]] = prev_val
                visited[new_place[0]][new_place[1]] = True
                prev_place = new_place
                prev_val = new_val
                new_place = self.new_place_for(prev_place[0], prev_place[1], start_index, end_index)
                new_val = image[new_place[0]][new_place[1]]

            curr_elem = self.next_step(curr_elem[0], curr_elem[1], start_index, end_index)
        return self.rotateInPlaceRec(image, start_index + 1, end_index - 1, visited)


    def next_step(self, i, j, start_index, end_index):
        if i == end_index:
            if j == start_index:
                return [i - 1, j]

            return [i, j - 1]
        elif i == start_index:
            if j == end_index:
                return [i + 1, j]

            return [i, j + 1]

        if j == end_index:
            if i == end_index:
                return [i, j - 1]

            return [i + 1, j]
        elif j == start_index:
            return [i - 1, j]

    def new_place_for(self, i, j, start_index, end_index):
        if i == start_index:
            return [j, end_index]

        if j == end_index:
            return [j, start_index + end_index - i]


        if i == end_index:
            return [j, start_index]

        if j == start_index:
            return [j, start_index + end_index - i]
