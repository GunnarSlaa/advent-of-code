#![allow(dead_code)]

use std::fs;

fn main() {
    let data = fs::read_to_string("input").expect("Can't read file");
    let lines: Vec<i32> = data.split("\r\n").map(|x| x.parse::<i32>().unwrap_or(0)).collect();
    let mut previous = lines.first().unwrap_or(&0);
    let mut count = 0;
    for (c, num) in lines.iter().enumerate(){
        if c == 0 {continue;}
        if num > previous {count+=1;}
        previous = num;
    }
    println!("Count: {}", count)
}