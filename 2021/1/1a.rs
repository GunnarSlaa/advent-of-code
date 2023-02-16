use std::fs;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let data = fs::read_to_string(&args[1]).expect("Can't read file");
    let lines: Vec<i32> = data.split("\r\n").map(|x| x.parse::<i32>().unwrap_or(0)).collect();
    let mut previous = &lines[0];
    let mut count = 0;
    for (c, num) in lines.iter().enumerate(){
        if c == 0 {continue;}
        if num > previous {count+=1;}
        previous = num;
    }
    println!("Count: {}", count)
}