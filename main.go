package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"ioutil"
	"strings"
)

func main() {
    cmd := exec.Command("lscpu")
    out, err := cmd.CombinedOutput()
    if err != nil {
        fmt.Printf("Error executing lscpu: %v\n", err)
        return
    }

    var cpuName string
    scanner := bufio.NewScanner(strings.NewReader(string(out)))

    for scanner.Scan() {
        line := scanner.Text()
        if strings.Contains(line, "Model name:") {
            cpuName = strings.TrimSpace(strings.TrimPrefix(line, "Model name:"))
            break
        }
    }

    if err := scanner.Err(); err != nil {
        fmt.Printf("Error reading output: %v\n", err)
        return
    }

    if cpuName != "" {
        fmt.Printf("CPU Model: %s\n", cpuName)
    } else {
        fmt.Println("CPU Model not found")
    }


	func getCPUTemp() {
		dirCheck := "/sys/class/thermal/" //directory to the thermal
		prefix := "thermal_zone"
	
		files, err := ioutil.ReadDir(dirCheck)
		if err != nil {
			log.Fatal(err)
		}
	
		for _, file := range files {
			if file.IsDir() {
				continue
			}
			if strings.HasPrefix(file.Name(), prefix) {
				fmt.Println(file.Name())
			}
		}
	}


}
