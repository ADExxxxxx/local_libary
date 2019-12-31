/*
题干:给定字典和一个起点单词, 一个终点单词,每次只能变换一个字母，
问起点单词是否可以到达终点单词？最短多少步。
如：
start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
*/

#include <iostream>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

template<class T>
void display(T iter){
    for(auto &it: iter){
        cout << "node is: " << it << endl;
    }
}

class Solution{
public:
    int LadderLength(const string &start, const string &end, const vector<string> &dict){
        
        // 缓存队列，current:用于存放当前距离的所有节点, next: 用于存放下一距离的所有节点
        queue<string> current, next;
        // 判重向量，表示当前节点是否已经被访问过
        vector<string> visited;

        int level = 0; //层次
        bool found = false; //flag表示是否找到结果

        current.push(start); //将起始节点放入队列

        auto state_is_target = [&](const string& str){return (str == end);};
        auto state_extend = [&](const string& str){
            vector<string> result;
            for (size_t i = 0; i < str.size(); i++){
                string new_word(str);
                for(char c = 'a'; c <= 'z'; c++){
                    if(c == new_word[i]) continue;

                    swap(c, new_word[i]);

                    if((count(dict.begin(), dict.end(), new_word) > 0 || new_word == end) 
                        && ! count(visited.begin(), visited.end(), new_word)){
                            result.push_back(new_word);
                            visited.push_back(new_word);
                    }
                    swap(c, new_word[i]);
                }
            }
            return result;
        };
        // 判断是否还有可扩展节点，若没有则结束
        // 判断是否找到相关结果
        while (!current.empty() && !found){
            ++level;
            while (!current.empty() && !found){
                const string str = current.front(); //记录当前节点
                current.pop(); // 当前节点出队

                const auto &new_state = state_extend(str);
                cout << "new state:" << endl;
                display(new_state);
                for(auto &state : new_state){
                    next.push(state); //将扩展的新节点添加进入下一层缓冲区
                    if(state_is_target(state)){
                        found = true;
                        break;
                    }
                }  
            }
            swap(next, current);   
        }
        if(found){
            return level;
        }
        else{
            return 0;
        }
        
    }
};

int main(){
    Solution sl;
    
    const string start = "hit";
    string end = "cog";
    const vector<string> dict = {"hot", "dot", "dog", "lot", "log"};
    
    int length;
    length = sl.LadderLength(start, end, dict);
    cout << "the shortest step is: " << length << endl;

    return 0;
}
