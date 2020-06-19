#include <iostream>
#include <vector>

using namespace std;

vector<int> insert_sort(vector<int> vec){
    for (int i=1; i<vec.size(); i++){
        int k = vec[i];
	for (int j=i; j>0; j--){
	    if (vec[j-1] > k){
	        int a = vec[j-1];
		vec[j-1] = vec[j];
		vec[j] = a;
	    }
	}
    }
    	
    return vec;
}


int main(){
    vector<int> v1 = {3, 1, 2, 6, 5, 8, 9, 4, 7};
    for (auto i:v1) 
	cout << i << "  ";
    cout << "\n";
    vector<int> v2 = insert_sort(v1);
    for (auto i: v2)
	cout << i << "  ";
    cout << "\n";
    return 0;
}
