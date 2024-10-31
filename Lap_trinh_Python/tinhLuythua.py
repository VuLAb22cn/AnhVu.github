def count_valid_parentheses(K, S):
    n = len(S)
    # Khởi tạo DP table
    dp = [[[0 for _ in range(K + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    
    dp[0][0][0] = 1  # Có một cách để có xâu rỗng

    for i in range(n):
        for depth in range(n + 1):
            for level in range(K + 1):
                if dp[i][depth][level] == 0:
                    continue
                
                if S[i] == '(' or S[i] == '?':
                    # Nếu là '('
                    if depth + 1 <= n:
                        dp[i + 1][depth + 1][max(level, depth + 1)] += dp[i][depth][level]

                if S[i] == ')' or S[i] == '?':
                    # Nếu là ')'
                    if depth > 0:
                        dp[i + 1][depth - 1][level] += dp[i][depth][level]

                if S[i] == '?':
                    # Thay thế '?' bằng '('
                    if depth + 1 <= n:
                        dp[i + 1][depth + 1][max(level, depth + 1)] += dp[i][depth][level]

                    # Thay thế '?' bằng ')'
                    if depth > 0:
                        dp[i + 1][depth - 1][level] += dp[i][depth][level]

    # Kết quả là các xâu có độ sâu bằng 0 và bậc bằng K
    return dp[n][0][K]

# Nhập đầu vào
K = int(input())
S = input()

# Tính toán và in ra kết quả
result = count_valid_parentheses(K, S)
print(result)
