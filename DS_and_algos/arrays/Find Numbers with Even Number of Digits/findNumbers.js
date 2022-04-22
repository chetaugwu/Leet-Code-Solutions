var findNumbers = function(nums) {
    var count = 0
    for (i = 0; i<nums.length; i++){
        var mini_count = 0
        var temp = nums[i]
        while (temp>=1){
            temp = temp/10
            mini_count++   
        }
        if (mini_count%2 == 0){
            count++
        }
    }
    return count
};