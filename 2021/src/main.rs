mod solutions;

use solutions::*;
use std::fs;

fn main(){
    let day = 7;
    let test_data = fs::read_to_string(format!("inputs/{}/input_test", day.to_string())).expect("Can't read file");
    let data = fs::read_to_string(format!("inputs/{}/input", day.to_string())).expect("Can't read file");
    let sol_test = solve(day, &test_data);
    let sol = solve(day, &data);
    println!("Part 1_test: {}", sol_test.0);
    println!("Part 2_test: {}", sol_test.1);
    println!("Part 1: {}", sol.0);
    println!("Part 2: {}", sol.1);
}