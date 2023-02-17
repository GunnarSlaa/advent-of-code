use std::convert::TryInto;

fn part1(lines: &Vec<&str>) -> u32{
    let lines_count = lines.len();
    let line_size = lines[0].len();
    let mut count_ones = vec![0; line_size];

    for line in lines.iter(){
        for (c, n) in line.chars().enumerate(){
            if n == '1' {count_ones[c] += 1}
        }
    }
    let gamma_str = count_ones.iter()
        .map(|x| (if x > &(lines_count / 2) {1} else {0}).to_string())
        .collect::<Vec<String>>()
        .join("");
    let gamma = u32::from_str_radix(&gamma_str, 2).unwrap();
    let epsilon: u32 = 2_u32.pow(line_size.try_into().unwrap()) - 1 - gamma;
    epsilon * gamma
}

fn part2(lines: &Vec<&str>) -> u32 {
    let mut lines_vec: Vec<&str> = lines.clone();
    let mut lines_count = lines_vec.len();
    let line_size = lines_vec[0].len();

    for column in 0..line_size {
        let count = lines_vec.clone().into_iter()
            .filter(|x| { &x[column..column + 1] == "1" })
            .collect::<Vec<&str>>()
            .len();
        let looking_for = if count * 2 >= lines_count { "1" } else { "0" };
        lines_vec = lines_vec.into_iter().filter(|x| { &x[column..column + 1] == looking_for }).collect();
        lines_count = lines_vec.len();
        if lines_count == 1 { break; }
    }
    let oxygen_rating = u32::from_str_radix(&lines_vec[0], 2).unwrap();

    lines_vec = lines.clone();
    lines_count = lines_vec.len();
    for column in 0..line_size {
        let count = lines_vec.clone().into_iter()
            .filter(|x| { &x[column..column + 1] == "1" })
            .collect::<Vec<&str>>()
            .len();
        let looking_for = if count * 2 < lines_count { "1" } else { "0" };
        lines_vec = lines_vec.into_iter().filter(|x| { &x[column..column + 1] == looking_for }).collect();
        lines_count = lines_vec.len();
        if lines_count == 1 { break; }
    }
    let co2_scrubber = u32::from_str_radix(&lines_vec[0], 2).unwrap();
    oxygen_rating * co2_scrubber
}

pub(crate) fn solve(input: &str) -> (String, String){
    let lines: Vec<&str> = input.split("\r\n").collect();
    (part1(&lines).to_string(), part2(&lines).to_string())
}