dp = [[0 for x in range(6)] for y in range(100)]

def cube_tower(cubes, n, cur_cube, prev_cube, prev_top_face):
    if cur_cube == n - 1:
        answers = [0 for x in range(6)]
        max_answer = 0
        for i in range(6):
            answers[i] = cube_tower(cubes, n, cur_cube - 1, cur_cube, cubes[n - 1][i]) + 1
            if answers[i] > answers[max_answer]:
                max_answer = i
        return answers[max_answer]
    elif cur_cube == 0:
        if prev_top_face in cubes[cur_cube]:
            return 1
        else:
            return 0
    else:
        if prev_top_face in cubes[cur_cube]:
            answers = [0 for x in range(6)]
            max_answer = 0
            for i in range(6):
                if cubes[cur_cube][i] == prev_top_face:
                    if dp[cur_cube][i] > 0:
                        answers[i] = dp[cur_cube][i]
                    else:
                        if (i % 2) == 0:
                            answers[i] = cube_tower(cubes, n, cur_cube - 1, cur_cube, cubes[cur_cube][i + 1]) + 1
                            dp[cur_cube][i] = answers[i]
                        else:
                            answers[i] = cube_tower(cubes, n, cur_cube - 1, cur_cube, cubes[cur_cube][i - 1]) + 1
                            dp[cur_cube][i] = answers[i]
                    if answers[i] > answers[max_answer]:
                        max_answer = i
            return answers[max_answer]
        else:
            return cube_tower(cubes, n, cur_cube - 1, prev_cube, prev_top_face)

n = int(input())
cubes = {}
for i in range(n):
    cubes[i] = [int(x) for x in input().split()]
print(cube_tower(cubes, n, n - 1, n, 0))