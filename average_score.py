def compute_average_scores():
    N, X = map(int, input().split())
    
    scores = []
    for _ in range(X):
        scores.append(tuple(map(int, input().split())))
    
    average_scores = []
    for i in range(N):
        student_scores = [scores[j][i] for j in range(X)]
        average_score = sum(student_scores) / N
        average_scores.append(round(average_score, 1))
    
    return tuple(average_scores)

average_scores = compute_average_scores()
print(average_scores)