#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M;
int lab[8][8];
vector<pair<int, int>> empty_spaces;
vector<pair<int, int>> virus_positions;
int max_safe_area = 0;

int main() {
    cin >> N >> M;
    for(int i=0; i<N; i++) {
        for(int j=0; j<M; j++) {
            cin >> lab[i][j];
            if(lab[i][j] == 0)
                empty_spaces.push_back({i,j});
            else if(lab[i][j] == 2)
                virus_positions.push_back({i,j});
        }
    }

    for(int i = 0; i < empty_spaces.size(); i++) {
        for(int j = i+1; j < empty_spaces.size(); j++) {
            for(int k = j+1; k < empty_spaces.size(); k++) {
                // Copy lab to temp_lab
                int temp_lab[8][8];
                for(int a = 0; a < N; a++) {
                    for(int b = 0; b < M; b++) {
                        temp_lab[a][b] = lab[a][b];
                    }
                }

                // Place walls
                auto [x1, y1] = empty_spaces[i];
                auto [x2, y2] = empty_spaces[j];
                auto [x3, y3] = empty_spaces[k];

                temp_lab[x1][y1] = 1;
                temp_lab[x2][y2] = 1;
                temp_lab[x3][y3] = 1;

                // Simulate virus spread
                queue<pair<int, int>> q;
                for(auto [vx, vy] : virus_positions) {
                    q.push({vx, vy});
                }

                int dx[] = { -1, 1, 0, 0 };
                int dy[] = { 0, 0, -1, 1 };

                while(!q.empty()) {
                    auto [x, y] = q.front(); q.pop();
                    for(int dir = 0; dir < 4; dir++) {
                        int nx = x + dx[dir];
                        int ny = y + dy[dir];
                        if(0 <= nx && nx < N && 0 <= ny && ny < M) {
                            if(temp_lab[nx][ny] == 0) {
                                temp_lab[nx][ny] = 2;
                                q.push({nx, ny});
                            }
                        }
                    }
                }

                // Count safe area
                int safe_area = 0;
                for(int a = 0; a < N; a++) {
                    for(int b = 0; b < M; b++) {
                        if(temp_lab[a][b] == 0)
                            safe_area++;
                    }
                }

                if(safe_area > max_safe_area)
                    max_safe_area = safe_area;
            }
        }
    }

    cout << max_safe_area << endl;
    return 0;
}
