use std::fs;

fn main() {
    let data = fs::read_to_string("input").expect("Can't read file");
    let lines: Vec<i32> = data.split("\r\n").map(|x| x.parse::<i32>().unwrap_or(0)).collect();
    let mut previous = &lines[0] + &lines[1] + &lines[2];
    let mut count = 0;
    for c in 1..lines.len() {
        if c < 2 {continue;}
        let sum = &lines[c - 2] + &lines[c - 1] + &lines[c];
        if sum > previous {count+=1;}
        previous = sum;
    }
    println!("Count: {}", count)
}