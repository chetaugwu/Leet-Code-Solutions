
/*
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var max = 0
    var count = 0
    for (let i = 0; i < nums.length; i++){
        if (nums[i] == 1){
            count++
            if (max < count){
                max = count
            }
        } else {
            count = 0
        }
    }
    return max
}