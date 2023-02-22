mod day1;
mod day2;
mod day3;
mod day4;
mod day6;
mod day7;

pub(crate) fn solve(day: u32, input: &str) -> (String, String) {
    match day {
        1 => day1::solve(input),
        2 => day2::solve(input),
        3 => day3::solve(input),
        4 => day4::solve(input),
        6 => day6::solve(input),
        7 => day7::solve(input),
        _ => ("Not implemented".to_string(), "Not implemented".to_string()),
    }
}