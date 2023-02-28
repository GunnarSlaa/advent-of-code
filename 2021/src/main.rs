extern crate array2d;

#[allow(unused_imports)]
mod solutions;
mod help;

use solutions::*;
use help::parsing::*;
use help::grid::*;
use help::generic::*;

use std::fs;
use std::convert::TryInto;
use std::str::FromStr;
use array2d::Array2D;
use std::collections::HashMap;
use std::collections::HashSet;
use std::iter::FromIterator;

fn main(){
    let day = 14;
    let test_data = fs::read_to_string(format!("inputs/{day}/input_test")).expect("Can't read file");
    let data = fs::read_to_string(format!("inputs/{day}/input")).expect("Can't read file");
    let sol_test = solve(day, &test_data);
    let sol = solve(day, &data);
    println!("Part 1_test: {}", sol_test.0);
    println!("Part 2_test: {}", sol_test.1);
    println!("Part 1: {}", sol.0);
    println!("Part 2: {}", sol.1);
}