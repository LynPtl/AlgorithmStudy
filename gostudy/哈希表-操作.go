package main

import (
	"fmt"
)

func main() {
	// 初始化哈希表
	hashmap := make(map[int]string)
	hashmap[1] = "one"
	hashmap[2] = "two"
	hashmap[3] = "three"

	// 检查哈希表是否为空，输出：false
	fmt.Println(len(hashmap) == 0)

	// 获取哈希表的大小，输出：3
	fmt.Println(len(hashmap))

	// 查找指定键值是否存在
	// 输出：Key 2 -> two
	if val, exists := hashmap[2]; exists {
		fmt.Println("Key 2 ->", val)
	} else {
		fmt.Println("Key 2 not found.")
	}

	// 获取指定键对应的值，若不存在会返回空字符串
	// 输出：
	fmt.Println(hashmap[4])

	// 插入一个新的键值对
	hashmap[4] = "four"

	// 获取新插入的值，输出：four
	fmt.Println(hashmap[4])

	// 删除键值对
	delete(hashmap, 3)

	// 检查删除后键 3 是否存在
	// 输出：Key 3 not found.
	if val, exists := hashmap[3]; exists {
		fmt.Println("Key 3 ->", val)
	} else {
		fmt.Println("Key 3 not found.")
	}

	// 遍历哈希表
	// 输出（顺序可能不同）：
	// 1 -> one
	// 2 -> two
	// 4 -> four
	for key, value := range hashmap {
		fmt.Printf("%d -> %s\n", key, value)
	}
}
