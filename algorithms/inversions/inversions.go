package main
import (
	"fmt";
	"os";
	"bufio";
	"strconv"
)
func loadArray() []int{
	arr := make([]int,0 )
	file, err := os.Open(os.Args[1])
	scanner := bufio.NewScanner(file)
	for scanner.Scan(){
		val, err := strconv.Atoi(scanner.Text())	
		if err == nil{
			arr = append(arr, val)
		}
	}	
 
	if err != nil{
		panic(err)
	}
	return arr
}

func countInversions(arr []int) int{
	if len(arr) <=1{
		return 0
	}
	l := countInversions(arr[:len(arr)/2])
	r := countInversions(arr[(len(arr)/2)+1:])
	spl := countSplitInversions(arr)
	return l + r + spl
}


func countSplitInversions(arr[] int) int {
	return 1
}

func main(){
	arr := loadArray()
	count := countInversions(arr)
	fmt.Println(count)
}
