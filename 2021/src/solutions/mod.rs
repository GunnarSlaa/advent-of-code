mod day1;
mod day2;
mod day3;
mod day4;
mod day6;
mod day7;
mod day8;
mod day9;
mod day10;
mod day11;
mod day12;
mod day13;

use super::*;

pub(crate) fn solve(day: u32, input: &str) -> (String, String) {
    match day {
        1 => day1::solve(input),
        2 => day2::solve(input),
        3 => day3::solve(input),
        4 => day4::solve(input),
        6 => day6::solve(input),
        7 => day7::solve(input),
        8 => day8::solve(input),
        9 => day9::solve(input),
        10 => day10::solve(input),
        11 => day11::solve(input),
        12 => day12::solve(input),
        13 => day13::solve(input),
        _ => ("Not implemented".to_string(), "Not implemented".to_string()),
    }
}