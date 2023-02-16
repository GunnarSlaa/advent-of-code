use std::fs;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let data = fs::read_to_string(&args[1]).expect("Can't read file");
    let mut numbers: Vec<i32> = data.split(",")
        .map(|x| x.parse::<i32>().unwrap_or(0))
        .collect();
    numbers.sort();
    let median = numbers[numbers.iter().len()/2];
    let cost: i32 = numbers.iter().map(|x| (median - x).abs()).sum();
    println!("{}", cost);
}