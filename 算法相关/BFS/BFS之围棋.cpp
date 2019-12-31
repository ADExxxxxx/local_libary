#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>


using namespace std;

void bfs(vector<vector<char>> &board, int i, int j){
    typedef pair<int, int> state_t;
    queue<state_t> q;
    const int m = board.size();
    const int n = board[0].size();
    state_t start(i, j);

    auto is_valid = [&](const state_t &state){
        const int x = state.first;
        const int y = state.second;
        if(x < 0 || x >= m || y < 0 || y >= n || board[x][y] != 'o')    
            return false;
        return true;
    } ;

    auto state_extend = [&](const auto &cur){
        vector<state_t> result;
        const int x = cur.first;
        const int y = cur.second;

        state_t new_state[4] = {
            {x + 1, y}, {x - 1, y}, {x, y + 1}, {x, y - 1}
        };

        for (size_t i = 0; i < 4; i++)
        {
            if(is_valid(new_state[i])){
                board[new_state[i].first][new_state[i].second] = '+';
                result.push_back(new_state[i]);
            }
        }
        return result;
    };
    
    if(is_valid(start)){
        board[i][j] = '+';
        q.push(start);
    }
    while (!q.empty()){
        auto cur = q.front();
        q.pop();
        auto new_state = state_extend(cur);
        for(auto &s : new_state){
            q.push(s);
        }
    }
    

}

void display(vector<vector<char>> ve){
    for(auto &i: ve){
        for(auto &j: i){
            cout << j << "\t";
        }
        cout << endl;
    }
}

class Solution{
public:
    void solve(vector<vector<char>> &board){
        if(board.empty()) return;

        for (size_t i = 0; i < board.size(); i++)
        {
            bfs(board, i, 0);
            bfs(board, i, 4);
        }

        for (size_t i = 0; i < board[0].size(); i++)
        {
            bfs(board, 0, i);
            bfs(board, 4, i);
        }
        
        for(size_t i = 0; i < board.size(); i++){
            for(size_t j = 0; j < board[0].size(); j++){
                if(board[i][j] == '+'){
                    board[i][j] = 'o';
                }
                else
                {
                    board[i][j] = 'x'; 
                } 
            }
        }
    }
    
};



int main(){
    vector<vector<char>> board = 
                    {{'x', 'x', 'x', 'x', 'x'},
                    {'x', 'o', 'x', 'x', 'x'},
                    {'x', 'o', 'o', 'x', 'x'},
                    {'x', 'o', 'o', 'x', 'x'},
                    {'x', 'o', 'x', 'x', 'x'}};
    cout << "The Original: " << endl;
    display(board);
    Solution sl;
    sl.solve(board);
    cout << "The Solve: " << endl;
    display(board);
    return 0;
}