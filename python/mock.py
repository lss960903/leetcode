class SparseVector {
private:
    int binarySearch(vector<pair<int,int>> avec,int index){
        int left=0;
        int right=avec.size()-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(avec[mid].first>index){
                right=mid-1;
            }else if(avec[mid].first<index){
                left=mid+1;
            }else{
                return avec[mid].second;
            }
        }
        return 0;
    }
public:
    vector<pair<int,int>> pairVec;
    SparseVector(vector<int> &nums) {
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0){
                pairVec.push_back(make_pair(i,nums[i]));
            }
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        int res=0;
        if(vec.pairVec.size()>pairVec.size()){
            for(auto aPair:pairVec){
                res+=binarySearch(vec.pairVec,aPair.first)*aPair.second;
            }
        }else{
            for(auto aPair:vec.pairVec){
                res+=binarySearch(pairVec,aPair.first)*aPair.second;
            }
        }
        return res;
    }
};