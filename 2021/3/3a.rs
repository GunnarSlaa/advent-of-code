use std::fs;
use std::convert::TryInto;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let data = fs::read_to_string(&args[1]).expect("Can't read file");
    let lines = data.split("\r\n");
    let lines_vec: Vec<&str> = lines.clone().collect();
    let lines_count = lines_vec.len();
    let line_size = lines_vec[0].len();
    let mut count_ones = vec![0; line_size];

    for line in lines{
        for (c, n) in line.chars().enumerate(){
            if n == '1' {count_ones[c] += 1}
        }
    }
    let gamma_str = count_ones.iter()
        .map(|x| (if x > &(lines_count / 2) {1} else {0}).to_string())
        .collect::<Vec<String>>()
        .join("");
    let gamma = usize::from_str_radix(&gamma_str, 2).unwrap();
    let epsilon = 2_usize.pow(line_size.try_into().unwrap()) - 1 - gamma;
    println!("Gamma: {}", gamma);
    println!("Epsilon: {}", epsilon);
    println!("Answer: {}", epsilon * gamma);
}