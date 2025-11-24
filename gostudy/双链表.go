package main

import (
	"container/list"
	"fmt"
)

func main() {
	// 初始化链表
	lst := list.New()
	lst.PushBack(1)
	lst.PushBack(2)
	lst.PushBack(3)
	lst.PushBack(4)
	lst.PushBack(5)

	// 检查链表是否为空，输出：false
	fmt.Println(lst.Len() == 0)

	// 获取链表的大小，输出：5
	fmt.Println(lst.Len())

	// 在链表头部插入元素 0
	lst.PushFront(0)
	// 在链表尾部插入元素 6
	lst.PushBack(6)

	// 获取链表头部和尾部元素，输出：0 6
	front := lst.Front().Value.(int)
	back := lst.Back().Value.(int)
	fmt.Println(front, back)

	// 删除链表头部元素
	lst.Remove(lst.Front())
	// 删除链表尾部元素
	lst.Remove(lst.Back())

	// 在链表中插入元素
	// 移动到第三个位置
	third := lst.Front().Next().Next()
	lst.InsertBefore(99, third)

	// 删除链表中某个元素
	second := lst.Front().Next()
	lst.Remove(second)

	// 遍历链表
	// 输出：1 99 3 4 5
	for e := lst.Front(); e != nil; e = e.Next() {
		fmt.Print(e.Value.(int), " ")
	}
	fmt.Println()
}
