package main

import (
	"fmt"
)

func main() {
	n := 10
	// 初始化切片，大小为 10，元素值都为 0
	nums := make([]int, n)

	// 输出：false
	fmt.Println(len(nums) == 0)

	// 输出：10
	fmt.Println(len(nums))

	// 在切片尾部插入一个元素 20
	// append 函数会返回一个新的切片，所以需要将返回值重新赋值给 nums
	nums = append(nums, 20)
	// 输出：11
	fmt.Println(len(nums))

	// 得到切片最后一个元素
	// 输出：20
	fmt.Println(nums[len(nums)-1])

	// 删除切片的最后一个元素
	nums = nums[:len(nums)-1]
	// 输出：10
	fmt.Println(len(nums))

	// 可以通过索引直接取值或修改
	nums[0] = 11
	// 输出：11
	fmt.Println(nums[0])

	// 在索引 3 处插入一个元素 99
	// ... 是展开操作符，表示将切片中的元素展开
	nums = append(nums[:3], append([]int{99}, nums[3:]...)...)

	// 删除索引 2 处的元素
	nums = append(nums[:2], nums[3:]...)

	// 交换 nums[0] 和 nums[1]
	nums[0], nums[1] = nums[1], nums[0]

	// 遍历切片
	// 输出：0 11 99 0 0 0 0 0 0 0
	for _, num := range nums {
		fmt.Print(num, " ")
	}
	fmt.Println()
}
