package main

import (
	"fmt"
)

func main() {
	// 初始化一个包含一些元素的哈希集合 hashset
	hashset := map[int]struct{}{
		1: {},
		2: {},
		3: {},
		4: {},
	}

	// 检查哈希集合是否为空，输出：false
	fmt.Println(len(hashset) == 0)

	// 获取哈希集合的大小，输出：4
	fmt.Println(len(hashset))

	// 查找指定元素是否存在
	// 输出：Element 3 found.
	if _, exists := hashset[3]; exists {
		fmt.Println("Element 3 found.")
	} else {
		fmt.Println("Element 3 not found.")
	}

	// 插入一个新的元素
	hashset[5] = struct{}{}

	// 删除一个元素
	delete(hashset, 2)
	// 输出：Element 2 not found.
	if _, exists := hashset[2]; exists {
		fmt.Println("Element 2 found.")
	} else {
		fmt.Println("Element 2 not found.")
	}

	// 遍历哈希集合
	// 输出（顺序可能不同）：
	// 1
	// 3
	// 4
	// 5
	for element := range hashset {
		fmt.Println(element)
	}
}
